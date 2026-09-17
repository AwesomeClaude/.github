import argparse
import concurrent.futures
import json
from pathlib import Path
import tempfile
import threading
import time
import unittest
from unittest.mock import patch
import test_oc as runner


class RunnerTests(unittest.TestCase):
    def setUp(self):
        runner.STOP.clear()
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def test_archive_keeps_contents_and_numbering(self):
        current = runner.archive(self.root)
        (current / 'evidence').write_text('keep')
        (self.root / 'oc-previous-batches' / 'batch-007').mkdir()
        runner.archive(self.root)
        self.assertEqual((self.root / 'oc-previous-batches/batch-008/evidence').read_text(), 'keep')
        self.assertEqual(list(current.iterdir()), [])

    def test_archive_refuses_symlink(self):
        (self.root / 'oc-batch-test').symlink_to(self.root, target_is_directory=True)
        with self.assertRaises(ValueError):
            runner.archive(self.root)

    def test_url(self):
        self.assertEqual(runner.live_url('http://localhost:4096/', '/tmp/run', 'ses_1'),
                         'http://localhost:4096/L3RtcC9ydW4/session/ses_1')

    def fake(self, slow=False):
        executable = self.root / 'fake-oc'
        executable.write_text('''#!/usr/bin/env python3
import pathlib, time, sys, json
assert pathlib.Path('.git').is_dir()
assert sys.argv[-1] == 'exact prompt'
''' + ('time.sleep(20)\n' if slow else '''time.sleep(.35)
pathlib.Path('analysis.md').write_text('# Source architecture screenshots reverse-engineered prompt how to play mechanics tags AAA\\nfictional reviews 4/5 3/5 5/5 https://github.com/phirogue/SparkyGames\\n' + 'evidence ' * 650)
print(json.dumps({'type': 'step_finish'}))
'''))
        executable.chmod(0o755)
        return argparse.Namespace(executable=str(executable), model='fake', web_base=None,
                                  timeout=.15 if slow else 10)

    def test_three_parallel_git_workspaces(self):
        args = self.fake()
        published = []
        start = time.monotonic()
        with patch.object(runner, 'api', return_value={'id': 'ses_fake'}):
            with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
                results = list(pool.map(lambda i: runner.run_one(i, args, self.root, 'http://localhost:4096',
                                                          'exact prompt', lambda r: published.append(dict(r))), range(1, 4)))
        self.assertLess(time.monotonic() - start, 2)
        self.assertEqual(len([r for r in published if r['status'] == 'running']), 3)
        for result in results:
            self.assertEqual(result['exit_code'], 0)
            self.assertTrue(result['validation']['structural_pass'])
            self.assertIsNone(result['validation']['quality_pass'])

    def test_cli_defaults_and_all_requested_workers(self):
        for count, flags in [(3, []), (5, ['--runs', '5'])]:
            with self.subTest(count=count):
                args = self.fake()
                prompt = self.root / 'prompt.txt'
                prompt.write_text('exact prompt')
                real_pool = concurrent.futures.ThreadPoolExecutor
                with patch.object(runner, 'ROOT', self.root), \
                     patch.object(runner, 'ensure_server', return_value='http://localhost:4096'), \
                     patch.object(runner, 'api', return_value={'id': 'ses_fake'}), \
                     patch('sys.argv', ['test_oc.py', '--executable', args.executable,
                                        '--prompt', str(prompt)] + flags), \
                     patch.object(runner.concurrent.futures, 'ThreadPoolExecutor', wraps=real_pool) as pool:
                    self.assertEqual(runner.main(), 0)
                    pool.assert_called_once_with(max_workers=count)
                summary = json.loads((self.root / 'work/oc-batch-test/summary.json').read_text())
                self.assertEqual(len(summary['results']), count)
                self.assertEqual(summary['concurrency'], count)

    def test_timeout_aborts_server_session(self):
        with patch.object(runner, 'api', return_value={'id': 'ses_fake'}) as api:
            result = runner.run_one(1, self.fake(True), self.root, 'http://localhost:4096',
                                    'exact prompt', lambda _: None)
        self.assertEqual(result['status'], 'timeout')
        self.assertFalse(result['validation']['report_generated'])
        self.assertTrue(any('/abort' in call.args[1] for call in api.call_args_list))

    def test_zero_exit_without_report_fails_validation(self):
        self.assertFalse(runner.validate(self.root, self.root / 'missing')['structural_pass'])


if __name__ == '__main__':
    unittest.main()
