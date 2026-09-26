#!/usr/bin/env python3
"""Analyze new GitHub games, then rebuild the game catalog."""

import argparse
import concurrent.futures
from datetime import datetime, timezone
import fcntl
import json
import os
from pathlib import Path
import re
import shutil
import signal
import subprocess
import sys
from urllib.parse import quote, urlsplit

import test_oc


ROOT = Path(__file__).resolve().parent.parent
GAMES = ROOT / 'games'
WORK = ROOT / 'work'


def game_url(value):
    parsed = urlsplit(value.strip())
    parts = [part for part in parsed.path.strip('/').split('/') if part]
    if parsed.scheme != 'https' or parsed.netloc.lower() != 'github.com' or parsed.query or parsed.fragment:
        raise ValueError(f'Not a plain HTTPS GitHub game link: {value}')
    if len(parts) < 2 or not all(re.fullmatch(r'[A-Za-z0-9_.-]+', p) for p in parts):
        raise ValueError(f'Invalid GitHub game link: {value}')
    owner, repo = parts[:2]
    repo = repo.removesuffix('.git')
    if not owner or not repo:
        raise ValueError(f'Invalid GitHub game link: {value}')
    if len(parts) > 2:
        if len(parts) < 4 or parts[2] != 'tree':
            raise ValueError(f'Use a repository URL or /tree/<branch>/<game-directory>: {value}')
        game_parts = parts[4:]
    else:
        game_parts = []
    if any(p in ('.', '..') for p in game_parts):
        raise ValueError(f'Unsafe game directory: {value}')
    normalized = f'https://github.com/{owner}/{repo}'
    if len(parts) > 2:
        normalized += '/tree/' + '/'.join(parts[3:])
    directory = GAMES / f'{owner}--{repo}'
    if game_parts:
        directory = directory.joinpath(*game_parts)
    return normalized, directory


def markdown(value):
    return re.sub(r'([\\`*_{}\[\]<>|])', r'\\\1', str(value).replace('\n', ' '))


def safe_url(value):
    if not isinstance(value, str):
        return None
    parsed = urlsplit(value)
    if parsed.scheme not in ('http', 'https') or not parsed.netloc:
        return None
    return quote(value, safe=':/?#[]@!$&\'*+,;=%-._~')


def score(value, name, nullable=False):
    if value is None and nullable:
        return None
    if not isinstance(value, dict) or isinstance(value.get('score'), bool):
        raise ValueError(f'{name} must contain a numeric score')
    number = value.get('score')
    if not isinstance(number, (int, float)) or not 0 <= number <= 10:
        raise ValueError(f'{name}.score must be between 0 and 10')
    return number


def validate(data, expected_url=None):
    if not isinstance(data, dict):
        raise ValueError('Report must be a JSON object')
    url = data.get('repository_url')
    normalized, _ = game_url(url) if isinstance(url, str) else (None, None)
    if expected_url and normalized != expected_url:
        raise ValueError(f'Report URL does not match input: {url}')
    if not isinstance(data.get('title'), str) or not data['title'].strip():
        raise ValueError('Report must have a title')
    score(data.get('rating'), 'rating')
    score(data.get('screenshot_based_score'), 'screenshot_based_score', nullable=True)
    if not isinstance(data.get('screenshots'), list):
        raise ValueError('Report must have a screenshots list')
    for shot in data['screenshots']:
        if not isinstance(shot, dict) or not safe_url(shot.get('url')):
            raise ValueError('Each screenshot must have an HTTP(S) URL')
    for key in ('source_analysis', 'how_to_play', 'mechanics', 'tags', 'fictional_reviews', 'links'):
        if not isinstance(data.get(key), list):
            raise ValueError(f'Report must have a {key} list')
    return data


def lines_list(items):
    return [f'- {markdown(item)}' for item in items if isinstance(item, str)]


def game_readme(data):
    title = markdown(data['title'])
    url = safe_url(data['repository_url'])
    graphic = data['screenshot_based_score']
    graphic_text = 'not scored' if graphic is None else f"{graphic['score']}/10"
    out = [f'# {title}', '', f'[Open the game source]({url})', '',
           f"**Overall rating:** {data['rating']['score']}/10. {markdown(data['rating'].get('reason', ''))}", '',
           f"**Screenshot score:** {graphic_text}. " +
           (markdown(graphic.get('reason', '')) if graphic else 'No inspectable gameplay screenshot.'), '']
    if data['screenshots']:
        out += ['## Screenshots', '']
        for shot in data['screenshots']:
            out += [f"![{markdown(shot.get('observation', title))}]({safe_url(shot['url'])})", '',
                    markdown(shot.get('observation', '')), '']
    for heading, key in [('Play', 'how_to_play'), ('Mechanics', 'mechanics'), ('Tags', 'tags')]:
        items = lines_list(data[key])
        if items:
            out += [f'## {heading}', '', *items, '']
    if isinstance(data.get('reconstructed_prompt'), str):
        out += ['## Reconstructed prompt', '', markdown(data['reconstructed_prompt']), '']
    if data['source_analysis']:
        out += ['## Source evidence', '']
        for item in data['source_analysis']:
            if isinstance(item, dict) and safe_url(item.get('url')):
                out.append(f"- {markdown(item.get('finding', 'Evidence'))} ([source]({safe_url(item['url'])}))")
        out.append('')
    if data['fictional_reviews']:
        out += ['## Fictional reviews', '', 'Treat these as illustrative, not real user reviews.', '']
        for review in data['fictional_reviews']:
            if isinstance(review, dict):
                out.append(f"- {markdown(review.get('rating', '?'))}/5: {markdown(review.get('text', ''))}")
        out.append('')
    if data['links']:
        out += ['## Links', '']
        out += [f'- [{markdown(link)}]({safe_url(link)})' for link in data['links'] if safe_url(link)]
        out.append('')
    return '\n'.join(out).rstrip() + '\n'


def write_atomic(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name + '.tmp')
    temp.write_text(content, encoding='utf-8')
    temp.replace(path)


def log(message):
    print(message, file=sys.stderr, flush=True)


def rebuild():
    entries = []
    for path in sorted(GAMES.rglob('readme.json')) if GAMES.exists() else []:
        try:
            data = validate(json.loads(path.read_text(encoding='utf-8')))
            _, expected = game_url(data['repository_url'])
            if path.parent != expected:
                raise ValueError(f'Report belongs at {expected}')
            write_atomic(path.with_name('README.md'), game_readme(data))
            entries.append((path.parent, data))
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            log(f'Skip {path}: {exc}')
    entries.sort(key=lambda item: (-item[1]['rating']['score'], item[1]['title'].casefold(), str(item[0])))
    out = ['# Game catalog', '', 'Browse the rated games. Open each game page for evidence and play instructions.', '',
           'Add games with `./scripts/games.sh <github-game-url> [more-urls...]` or '
           '`./scripts/games.sh --file links.txt`. Rebuild every page and this index with '
           '`./scripts/games.sh`. Inspect `games/added.jsonl` for dated additions. '
           'Inspect `work/game-batches/` for agent logs and rejected reports.', '', '## Games', '']
    for directory, data in entries:
        target = quote(str(directory.relative_to(ROOT) / 'README.md'), safe='/')
        graphic = data['screenshot_based_score']
        graphic_text = 'not scored' if graphic is None else f"{graphic['score']}/10"
        out.append(f"- [{markdown(data['title'])}]({target}) — overall {data['rating']['score']}/10; screenshots {graphic_text}")
    if not entries:
        out.append('No valid games yet.')
    gallery = [(directory, data) for directory, data in entries
               if data['screenshot_based_score'] is not None and data['screenshots']]
    gallery.sort(key=lambda item: (-item[1]['screenshot_based_score']['score'],
                                  item[1]['title'].casefold(), str(item[0])))
    out += ['', '## Screenshot gallery', '']
    for directory, data in gallery:
        shot = data['screenshots'][0]
        target = quote(str(directory.relative_to(ROOT) / 'README.md'), safe='/')
        out += [f"### [{markdown(data['title'])}]({target}) — {data['screenshot_based_score']['score']}/10", '',
                f"![{markdown(shot.get('observation', data['title']))}]({safe_url(shot['url'])})", '']
    if not gallery:
        out.append('No scored screenshots yet.')
    write_atomic(ROOT / 'README.md', '\n'.join(out).rstrip() + '\n')
    print(f'Rebuilt {len(entries)} game pages and the root README.', flush=True)


def inputs(args):
    values = list(args.links)
    if args.file:
        values += [line.strip() for line in args.file.read_text(encoding='utf-8').splitlines()
                   if line.strip() and not line.lstrip().startswith('#')]
    unique = {}
    for value in values:
        url, directory = game_url(value)
        if directory in unique and unique[directory] != url:
            raise ValueError(f'Two links target the same game location: {directory}')
        unique[directory] = url
    return [(url, directory) for directory, url in unique.items()]


def analyze(items, args):
    WORK.mkdir(exist_ok=True)
    batch = WORK / 'game-batches' / (datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ') + f'-{os.getpid()}')
    batch.mkdir(parents=True)
    (batch / 'records').mkdir()
    base = test_oc.ensure_server(args, WORK)
    prompt_template = args.prompt.read_text(encoding='utf-8')
    if not prompt_template.strip():
        raise ValueError('Prompt must not be empty')
    prepared = []
    try:
        for index, (url, directory) in enumerate(items, 1):
            prompt = prompt_template.replace('{{repository_url}}', url)
            meta = test_oc.prepare(index, args, batch, base, prompt)
            prepared.append((url, directory, meta))
        def stop(*_):
            test_oc.STOP.set()
        previous = signal.signal(signal.SIGINT, stop)
        try:
            with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as pool:
                futures = [pool.submit(test_oc.run_one, meta, base, args.timeout)
                           for _, _, meta in prepared]
                for (url, directory, meta), future in zip(prepared, futures):
                    result = future.result()
                    if result['status'] != 'finished':
                        log(f"Skip {url}: agent {result['status']}; inspect {meta / 'result.json'}")
                        continue
                    report = Path(result['directory']) / 'readme.json'
                    try:
                        data = validate(json.loads(report.read_text(encoding='utf-8')), url)
                        directory.mkdir(parents=True, exist_ok=True)
                        write_atomic(directory / 'readme.json', json.dumps(data, indent=2, ensure_ascii=False) + '\n')
                        write_atomic(directory / 'README.md', game_readme(data))
                        record = {'added_at': datetime.now(timezone.utc).isoformat(),
                                  'source_url': url, 'output': str(directory.relative_to(ROOT)),
                                  'title': data['title'], 'rating_score': data['rating']['score'],
                                  'screenshot_based_score': None if data['screenshot_based_score'] is None
                                  else data['screenshot_based_score']['score'],
                                  'session_id': result['session_id'], 'model': args.model,
                                  'prompt_sha256': result['prompt_sha256']}
                        with (GAMES / 'added.jsonl').open('a', encoding='utf-8') as ledger:
                            ledger.write(json.dumps(record, ensure_ascii=False) + '\n')
                        print(f"Added {data['title']}: {directory.relative_to(ROOT)}", flush=True)
                    except (OSError, ValueError, json.JSONDecodeError) as exc:
                        log(f'Skip {url}: cannot publish readme.json: {exc}; inspect {report}')
        finally:
            signal.signal(signal.SIGINT, previous)
            test_oc.STOP.clear()
    except BaseException:
        for _, _, meta in prepared:
            result = json.loads((meta / 'result.json').read_text())
            if result['status'] in ('queued', 'running'):
                test_oc.abort(base, result)
        raise


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('links', nargs='*', help='Repository or game-directory GitHub URLs')
    parser.add_argument('--file', type=Path, help='Read additional URLs, one per line')
    parser.add_argument('--jobs', type=int, default=3, help='Maximum concurrent agents')
    parser.add_argument('--timeout', type=float, default=900, help='Seconds per agent')
    parser.add_argument('--prompt', type=Path, default=ROOT / 'prompt.md')
    parser.add_argument('--model', default=test_oc.MODEL)
    parser.add_argument('--executable', default='opencode')
    parser.add_argument('--server', help='Existing local OpenCode server URL')
    parser.add_argument('--web-base', help='Existing protected live-session URL base')
    parser.add_argument('--port', type=int, default=4096)
    args = parser.parse_args()
    if args.jobs < 1 or not 0 < args.timeout < float('inf'):
        parser.error('jobs and timeout must be positive and finite')
    try:
        items = inputs(args)
        WORK.mkdir(exist_ok=True)
        with (WORK / 'games.lock').open('w') as lock:
            try:
                fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError:
                raise RuntimeError('Another game catalog run is active')
            new = [(url, directory) for url, directory in items if not (directory / 'readme.json').exists()]
            for url, _ in items:
                if not any(url == candidate for candidate, _ in new):
                    print(f'Already added: {url}', flush=True)
            if new:
                executable = shutil.which(args.executable)
                if not executable or not shutil.which('git'):
                    raise RuntimeError('Require opencode and git on PATH')
                args.executable = str(Path(executable).resolve())
                analyze(new, args)
            rebuild()
        return 0
    except (OSError, ValueError, RuntimeError) as exc:
        log(str(exc))
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
