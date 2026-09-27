#!/usr/bin/env python3
"""Open one catalog issue for 10 random, accessible games from games.json.

Run: python3 scripts/submit-random-games.py [--dataset /path/to/games.json]
The default dataset is the local game-discovery dataset referenced by AGENTS.md.
"""

import argparse
import json
from pathlib import Path
import secrets
import subprocess
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DATASET = Path('/Users/igor/Documents/Codex/2026-09-08/find-games-last-week-made-with/games.json')
DEFAULT_REPO = 'agents-dev/Astra-Top-Games'
COUNT = 10


def repository_url(value):
    if not isinstance(value, str):
        return None
    parsed = urlsplit(value)
    parts = parsed.path.strip('/').split('/')
    if (parsed.scheme != 'https' or parsed.netloc.lower() != 'github.com'
            or len(parts) != 2 or not all(parts) or parsed.query or parsed.fragment):
        return None
    return f'https://github.com/{parts[0]}/{parts[1].removesuffix(".git")}'


def existing_repositories():
    urls = set()
    for path in (ROOT / 'games').glob('**/readme.json'):
        report = json.loads(path.read_text(encoding='utf-8'))
        url = repository_url(report.get('repository_url'))
        if url:
            urls.add(url.casefold())
    return urls


def accessible(url):
    parts = urlsplit(url).path.strip('/')
    result = subprocess.run(['gh', 'api', f'repos/{parts}', '--jq', '.private, .archived'],
                            capture_output=True, text=True, timeout=30)
    return result.returncode == 0 and result.stdout.splitlines() == ['false', 'false']


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dataset', type=Path, default=DEFAULT_DATASET)
    parser.add_argument('--repo', default=DEFAULT_REPO, help='Destination owner/repository')
    args = parser.parse_args()

    data = json.loads(args.dataset.read_text(encoding='utf-8'))
    existing = existing_repositories()
    candidates = []
    seen = set(existing)
    for game in data:
        url = repository_url(game.get('github_url'))
        if (not url or url.casefold() in seen or not game.get('is_independent_game')
                or not game.get('verification_status', '').startswith('verified_source')):
            continue
        seen.add(url.casefold())
        candidates.append((game['name'], url))

    secrets.SystemRandom().shuffle(candidates)
    selected = []
    for name, url in candidates:
        if accessible(url):
            selected.append((name, url))
            print(f'Selected: {name} — {url}', flush=True)
            if len(selected) == COUNT:
                break
    if len(selected) < COUNT:
        raise SystemExit(f'Only {len(selected)} accessible, uncataloged source games found; no issue created.')

    body = '\n'.join(url for _, url in selected)
    result = subprocess.run(['gh', 'issue', 'create', '--repo', args.repo,
                             '--title', 'Analyze 10 randomly selected games', '--body', body],
                            check=True, text=True, capture_output=True, timeout=60)
    print(result.stdout.strip())


if __name__ == '__main__':
    main()
