import argparse
import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import games


def report(url, title='Puzzle', overall=6, visual=8):
    return {
        'repository_url': url, 'title': title,
        'source_analysis': [{'finding': 'Visible source', 'url': url}],
        'screenshots': [{'url': 'https://example.com/gameplay.png', 'observation': 'Gameplay'}],
        'screenshot_based_score': {'score': visual, 'reason': 'Coherent art'},
        'reconstructed_prompt': 'Build a puzzle game', 'how_to_play': ['Open the game'],
        'mechanics': ['Move blocks'], 'tags': ['puzzle'],
        'rating': {'score': overall, 'reason': 'Small scope'},
        'fictional_reviews': [{'rating': 4, 'text': 'Fictional review'}],
        'links': [url],
    }


class GamesTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.patches = [patch.object(games, 'ROOT', self.root),
                        patch.object(games, 'GAMES', self.root / 'games'),
                        patch.object(games, 'WORK', self.root / 'work')]
        for item in self.patches:
            item.start()

    def tearDown(self):
        for item in reversed(self.patches):
            item.stop()
        self.temp.cleanup()

    def test_url_locations_and_bad_urls(self):
        root = games.game_url('https://github.com/acme/arcade')
        nested = games.game_url('https://github.com/acme/arcade/tree/main/games/puzzle')
        self.assertEqual(root[1], games.GAMES / 'acme--arcade')
        self.assertEqual(nested[1], games.GAMES / 'acme--arcade/games/puzzle')
        with self.assertRaises(ValueError):
            games.game_url('https://github.com/acme/arcade/tree/main/../other')
        with self.assertRaises(ValueError):
            games.game_url('https://example.com/acme/arcade')

    def test_rebuild_all_pages_and_sort_gallery_by_visual_score(self):
        a = 'https://github.com/acme/arcade'
        b = 'https://github.com/acme/arcade/tree/main/games/puzzle'
        for url, title, overall, visual in [(a, 'Root', 9, 3), (b, 'Puzzle', 4, 8)]:
            directory = games.game_url(url)[1]
            directory.mkdir(parents=True, exist_ok=True)
            (directory / 'readme.json').write_text(json.dumps(report(url, title, overall, visual)))
        bad = games.GAMES / 'bad/readme.json'
        bad.parent.mkdir()
        bad.write_text('{broken')
        with contextlib.redirect_stderr(io.StringIO()) as errors:
            games.rebuild()
        self.assertIn('Skip', errors.getvalue())
        self.assertTrue((games.GAMES / 'acme--arcade/README.md').exists())
        self.assertTrue((games.GAMES / 'acme--arcade/games/puzzle/README.md').exists())
        index = (games.ROOT / 'README.md').read_text()
        list_part, gallery_part = index.split('## Screenshot gallery')
        self.assertLess(list_part.index('[Root]'), list_part.index('[Puzzle]'))
        self.assertLess(gallery_part.index('[Puzzle]'), gallery_part.index('[Root]'))
        self.assertFalse((games.GAMES / 'added.jsonl').exists())

    def test_null_visual_score_has_no_gallery_tile(self):
        url = 'https://github.com/acme/game'
        data = report(url)
        data['screenshot_based_score'] = None
        directory = games.game_url(url)[1]
        directory.mkdir(parents=True)
        (directory / 'readme.json').write_text(json.dumps(data))
        games.rebuild()
        self.assertIn('not scored', (games.ROOT / 'README.md').read_text())
        self.assertIn('No scored screenshots yet.', (games.ROOT / 'README.md').read_text())

    def test_bad_rating_is_logged_not_published(self):
        data = report('https://github.com/acme/game')
        data['rating'] = {'grade': 'AA'}
        with self.assertRaisesRegex(ValueError, 'rating.score'):
            games.validate(data)

    def test_inputs_file_and_duplicate_locations(self):
        file = self.root / 'links.txt'
        file.write_text('# comment\nhttps://github.com/acme/game\n')
        args = argparse.Namespace(links=['https://github.com/acme/game/'], file=file)
        self.assertEqual(len(games.inputs(args)), 1)
        args.links = ['https://github.com/acme/game/tree/main']
        with self.assertRaisesRegex(ValueError, 'same game location'):
            games.inputs(args)

    def test_analyze_publishes_valid_game_and_logs_bad_json(self):
        good = 'https://github.com/acme/arcade'
        bad = 'https://github.com/acme/arcade/tree/main/games/bad'
        prompt = self.root / 'prompt.md'
        prompt.write_text('Analyze {{repository_url}}')
        args = argparse.Namespace(prompt=prompt, jobs=2, timeout=1, server='http://localhost',
                                  port=4096, executable='fake', model='fake', web_base=None)

        def prepare(index, unused_args, batch, unused_base, text):
            meta = batch / 'records' / f'run-{index:03d}'
            meta.mkdir(parents=True)
            directory = batch / f'run-{index:03d}'
            directory.mkdir()
            (directory / 'readme.json').write_text(json.dumps(report(good)) if index == 1 else '{bad')
            (meta / 'result.json').write_text(json.dumps({'status': 'queued', 'session_id': f'ses_{index}',
                                                          'directory': str(directory), 'prompt_sha256': 'hash'}))
            self.assertIn(good if index == 1 else bad, text)
            return meta

        def run_one(meta, unused_base, unused_timeout):
            result = json.loads((meta / 'result.json').read_text())
            result['status'] = 'finished'
            return result

        with patch.object(games.test_oc, 'ensure_server', return_value='http://localhost'), \
             patch.object(games.test_oc, 'prepare', side_effect=prepare), \
             patch.object(games.test_oc, 'run_one', side_effect=run_one), \
             contextlib.redirect_stderr(io.StringIO()) as errors:
            games.analyze([games.game_url(good), games.game_url(bad)], args)
        self.assertIn('cannot publish readme.json', errors.getvalue())
        self.assertTrue((games.GAMES / 'acme--arcade/readme.json').exists())
        self.assertFalse((games.GAMES / 'acme--arcade/games/bad/readme.json').exists())
        ledger = (games.GAMES / 'added.jsonl').read_text().splitlines()
        self.assertEqual(len(ledger), 1)
        self.assertEqual(json.loads(ledger[0])['source_url'], good)


if __name__ == '__main__':
    unittest.main()
