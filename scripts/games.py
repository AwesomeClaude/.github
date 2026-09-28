#!/usr/bin/env python3
"""Analyze public game links, refresh reports, and rebuild the catalog."""

import argparse
import concurrent.futures
from datetime import datetime, timezone
import fcntl
import hashlib
import html
import json
import os
from pathlib import Path
import re
import shutil
import signal
import subprocess
import sys
import time
import urllib.request
from urllib.parse import quote, urlsplit

import test_oc
import screenshots


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


def no_source_destination(value):
    parsed = urlsplit(value.strip())
    if parsed.scheme not in ('http', 'https') or not parsed.hostname:
        raise ValueError(f'Invalid original game link: {value}')
    host = re.sub(r'[^a-z0-9]+', '-', parsed.hostname.lower()).strip('-')[:48]
    digest = hashlib.sha256(value.strip().encode()).hexdigest()[:12]
    return GAMES / 'no-source' / f'{host}--{digest}'


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
    if not isinstance(value, dict):
        raise ValueError(f'{name} must contain an integer score')
    number = value.get('score')
    if type(number) is not int or not 0 <= number <= 100:
        raise ValueError(f'{name}.score must be an integer between 0 and 100')
    return number


def catalog_path(slug):
    if not isinstance(slug, str) or not re.fullmatch(r'[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*', slug):
        raise ValueError('Invalid catalog slug')
    if any(part in ('.', '..', 'analysis') for part in slug.split('/')):
        raise ValueError('Invalid catalog slug')
    path = GAMES / slug
    if path.resolve() != path.absolute() or not path.resolve().is_relative_to(GAMES.resolve()):
        raise ValueError('Catalog path escapes games')
    return path


def report_destination(data):
    if data.get('catalog_slug'):
        return catalog_path(data['catalog_slug'])
    if data.get('repository_url'):
        return game_url(data['repository_url'])[1]
    return no_source_destination(data['source_url'])


def validate(data, expected_url=None):
    if not isinstance(data, dict):
        raise ValueError('Report must be a JSON object')
    url = data.get('repository_url')
    if url in (None, ''):
        normalized = None
    elif isinstance(url, str):
        normalized, _ = game_url(url)
    else:
        raise ValueError('repository_url must be a GitHub URL or null')
    data['repository_url'] = normalized
    source_url = data.get('source_url') or normalized
    if not isinstance(source_url, str) or not safe_url(source_url):
        raise ValueError('A game needs an original source_url')
    no_source_destination(source_url)
    data['source_url'] = source_url
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
    for review in data['fictional_reviews']:
        if not isinstance(review, dict) or type(review.get('rating')) is not int or not 0 <= review['rating'] <= 100:
            raise ValueError('Each fictional review rating must be an integer between 0 and 100')
    controls = data.get('controls')
    if controls is not None:
        if not isinstance(controls, dict) or set(controls) != {
                'mobile_controls', 'motion_controls', 'gamepad', 'keyboard_mouse'}:
            raise ValueError('controls must contain all four control types')
        if any(value not in ('supported', 'not_supported', 'unknown') for value in controls.values()):
            raise ValueError('Each control status must be supported, not_supported, or unknown')
    player_modes = data.get('player_modes')
    if player_modes is not None:
        if not isinstance(player_modes, dict) or set(player_modes) != {'human_players', 'modes'}:
            raise ValueError('player_modes must contain human_players and modes')
        players = player_modes['human_players']
        if players is not None and not (
                (type(players) is int and players > 0) or
                (isinstance(players, str) and players.strip())):
            raise ValueError('human_players must be a positive integer, nonempty range, or null')
        modes = player_modes['modes']
        allowed = {'single-player', 'local multiplayer', 'online multiplayer'}
        if not isinstance(modes, list) or any(not isinstance(mode, str) or mode not in allowed for mode in modes) or len(set(modes)) != len(modes):
            raise ValueError('player_modes.modes must list distinct supported modes')
    play_url = data.get('play_game_url')
    if play_url is not None and not safe_url(play_url):
        raise ValueError('play_game_url must be an HTTP(S) URL or null')
    data['links'] = labeled_links(data['links'],
        [{'label': 'Original submission', 'url': source_url},
         {'label': 'Source repository', 'url': normalized},
         {'label': 'Play game', 'url': play_url}])
    models = data.setdefault('creation_models', [])
    if isinstance(models, list):
        for model in models:
            if isinstance(model, dict) and not model.get('evidence_url') and model.get('url'):
                model['evidence_url'] = model.pop('url')
    if not isinstance(models, list) or any(not isinstance(m, dict) or
            not isinstance(m.get('name'), str) or not safe_url(m.get('evidence_url')) for m in models):
        raise ValueError('creation_models must contain names and evidence URLs')
    technologies = data.setdefault('technologies', [])
    if not isinstance(technologies, list):
        raise ValueError('technologies must be a list')
    for technology in technologies:
        if not isinstance(technology, dict) or not isinstance(technology.get('name'), str) or not technology['name'].strip():
            raise ValueError('Each technology needs a name')
        if not isinstance(technology.get('category'), str) or not technology['category'].strip():
            raise ValueError('Each technology needs a category')
        if not safe_url(technology.get('evidence_url')):
            raise ValueError('Each technology needs an evidence_url')
        version = technology.setdefault('version', None)
        if version is not None and (not isinstance(version, str) or not version.strip()):
            raise ValueError('Technology version must be a nonempty string or null')
    if data.get('catalog_slug'):
        catalog_path(data['catalog_slug'])
    return data


def labeled_links(*groups):
    links = {}
    for group in groups:
        for item in group:
            item = {'label': 'Related link', 'url': item} if isinstance(item, str) else item
            if not isinstance(item, dict) or not safe_url(item.get('url')):
                continue
            url = item['url']
            label = str(item.get('label') or 'Related link')
            if url not in links or links[url]['label'] == 'Related link' or label == 'Source repository':
                links[url] = {'label': label, 'url': url}
    return list(links.values())


def lines_list(items):
    return [f'- {markdown(item)}' for item in items if isinstance(item, str)]


def display_date(value):
    if not value:
        return 'Not established'
    try:
        date = datetime.fromisoformat(value.replace('Z', '+00:00'))
        if date.tzinfo is None:
            date = date.replace(tzinfo=timezone.utc)
        return date.astimezone(timezone.utc).strftime('%d %b %Y · %H:%M UTC')
    except (TypeError, ValueError):
        return markdown(value)


def game_readme(data, directory):
    title = markdown(data['title'])
    url = safe_url(data['repository_url'])
    graphic = data['screenshot_based_score']
    graphic_text = 'Not scored' if graphic is None else f"{graphic['score']}/100"
    links = []
    if data.get('play_game_url'):
        links.append(f"[Play the game]({safe_url(data['play_game_url'])})")
    links.append(f'[View source]({url})' if url else
                 f'[View original submission]({safe_url(data["source_url"])})')
    if data.get('previous_report_url'):
        links.append(f"[Previous report]({safe_url(data['previous_report_url'])})")
    out = [f'# {title}', '', ' · '.join(links), '']
    if not url:
        out += ['No verified source repository.', '']
    out += ['| Overall rating | Screenshot score |', '| :---: | :---: |',
            f"| **{data['rating']['score']}/100** | **{graphic_text}** |", '',
            '<details>', '<summary>Read the scoring rationale</summary>', '',
            '### Overall rating', '', markdown(data['rating'].get('reason', '')), '',
            '### Screenshot score', '',
            markdown(graphic.get('reason', '')) if graphic else 'No inspectable gameplay screenshot.',
            '', '</details>', '', '## At a glance', '', '| Detail | Value |', '| --- | --- |']
    for label, key in [('Repository created', 'repository_created_at'),
                       ('Added to catalog', 'catalog_added_at'), ('Last updated', 'catalog_updated_at')]:
        if data.get(key):
            out.append(f"| {label} | {display_date(data[key])} |")
    models = ', '.join(f"[{markdown(m['name'])}]({safe_url(m['evidence_url'])})"
                       for m in data.get('creation_models', []))
    out.append(f"| Documented creation models | {models or 'Not established'} |")
    out.append('')
    if data['screenshots']:
        out += ['## Screenshots', '']
        for shot in data['screenshots']:
            local = screenshots.local_path(directory, shot)
            if local:
                out += [f"![{markdown(data['title'])} gameplay]({local})", '']
            else:
                out += ['Screenshot unavailable; inspect the original source.', '']
            out += [markdown(shot.get('observation', '')), '',
                    f"[Original screenshot]({safe_url(shot['url'])})", '']
    for heading, key in [('Play', 'how_to_play'), ('Mechanics', 'mechanics'), ('Tags', 'tags')]:
        items = lines_list(data[key])
        if items:
            out += [f'## {heading}', '', *items, '']
    if data.get('controls') is not None:
        out += ['## Controls', '']
        labels = [('Mobile controls', 'mobile_controls'), ('Motion controls', 'motion_controls'),
                  ('Gamepad', 'gamepad'), ('Keyboard/mouse', 'keyboard_mouse')]
        statuses = {'supported': 'Supported', 'not_supported': 'Not supported',
                    'unknown': 'Not established'}
        out += [f'- {label}: {statuses[data["controls"][key]]}' for label, key in labels]
        out.append('')
    if data.get('player_modes') is not None:
        players = data['player_modes']['human_players']
        modes = data['player_modes']['modes']
        out += ['## Player modes', '',
                f'- Human players: {markdown(players) if players is not None else "Not established"}',
                f'- Modes: {markdown(", ".join(modes)) if modes else "Not established"}', '']
    if data.get('technologies'):
        out += ['## Technologies', '']
        for technology in data['technologies']:
            name = technology['name'] + (f" {technology['version']}" if technology.get('version') else '')
            out.append(f"- **{markdown(name)}** — {markdown(technology['category'])} "
                       f"([evidence]({safe_url(technology['evidence_url'])}))")
        out.append('')
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
                out.append(f"- {markdown(review.get('rating', '?'))}/100: {markdown(review.get('text', ''))}")
        out.append('')
    if data['links']:
        out += ['## Links', '']
        out += [f"- [{markdown(link['label'])}]({safe_url(link['url'])})" for link in data['links']]
        out.append('')
    return '\n'.join(out).rstrip() + '\n'


def write_atomic(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name + '.tmp')
    temp.write_text(content, encoding='utf-8')
    temp.replace(path)


def log(message):
    print(message, file=sys.stderr, flush=True)


def catalog_readme(entries, link_prefix=''):
    out = ['# Game catalog', '', 'Browse the rated games. Open each game page for evidence and play instructions.',
           'Browse games with or without public source code in the same ranking and screenshot gallery.', '',
           f'[![Submit your game]({link_prefix}assets/submit-your-game.png)]'
           '(https://github.com/AwesomeClaude/.github/issues/new?title=Submit%20your%20game&body=Paste%20one%20game%20URL%20per%20line%20below%3A%0A)', '',
           'Add games with `./scripts/games.sh <game-url> [more-urls...]` or '
           '`./scripts/games.sh --file links.txt`. Rebuild every page and this index with '
           '`./scripts/games.sh`. Inspect `games/history/` for per-run analysis outcomes and provenance. '
           'Inspect `work/game-batches/` for agent logs and rejected reports.', '', '## Games', '']
    for directory, data in entries:
        target = link_prefix + quote(str(directory.relative_to(ROOT) / 'README.md'), safe='/')
        graphic = data['screenshot_based_score']
        graphic_text = 'not scored' if graphic is None else f"{graphic['score']}/100"
        source_text = '' if data['repository_url'] else '; no verified source repository'
        out.append(f"- [{markdown(data['title'])}]({target}) — overall {data['rating']['score']}/100; screenshots {graphic_text}{source_text}")
    if not entries:
        out.append('No valid games yet.')
    gallery = [(directory, data) for directory, data in entries
               if data['screenshot_based_score'] is not None
               and any(screenshots.local_path(directory, shot) for shot in data['screenshots'])]
    gallery.sort(key=lambda item: (-item[1]['screenshot_based_score']['score'],
                                  item[1]['title'].casefold(), str(item[0])))
    out += ['', '## Screenshot gallery', '']
    if gallery:
        out.append('<table>')
        for index in range(0, len(gallery), 3):
            row = gallery[index:index + 3]
            out.append('<tr>')
            for directory, data in row:
                shot = next(shot for shot in data['screenshots'] if screenshots.local_path(directory, shot))
                target = html.escape(link_prefix + quote(str(directory.relative_to(ROOT) / 'README.md'), safe='/'), quote=True)
                screenshot = html.escape(link_prefix + quote(str(directory.relative_to(ROOT) / shot['local_path']), safe='/'), quote=True)
                title = html.escape(data['title'], quote=True)
                observation = html.escape(data['title'] + ' gameplay', quote=True)
                screenshot_score = data['screenshot_based_score']['score'] / 10
                out.append(
                    f'<td align="center" width="33%"><a href="{target}">'
                    f'<img src="{screenshot}" alt="{observation}" height="180"></a><br>'
                    f'<a href="{target}"><strong>{title}</strong></a> · 📸 {screenshot_score:.1f}/10</td>'
                )
            out.extend(['<td width="33%"></td>'] * (3 - len(row)))
            out.append('</tr>')
        out.extend(['</table>', ''])
    else:
        out.append('No scored screenshots yet.')
    return '\n'.join(out).rstrip() + '\n'


def rebuild(retry_screenshots=False):
    entries = []
    for path in sorted(GAMES.rglob('readme.json')) if GAMES.exists() else []:
        if 'analysis' in path.relative_to(GAMES).parts:
            continue
        try:
            data = validate(json.loads(path.read_text(encoding='utf-8')))
            expected = report_destination(data)
            if path.parent != expected:
                raise ValueError(f'Report belongs at {expected}')
            entries.append((path.parent, data))
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            log(f'Skip {path}: {exc}')
    def archive_entry(entry):
        directory, data = entry
        screenshots.archive(directory, data, retry=retry_screenshots)
        write_atomic(directory / 'readme.json', json.dumps(data, indent=2, ensure_ascii=False) + '\n')
        write_atomic(directory / 'README.md', game_readme(data, directory))
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        list(pool.map(archive_entry, entries))
    entries.sort(key=lambda item: (-item[1]['rating']['score'], item[1]['title'].casefold(), str(item[0])))
    write_atomic(ROOT / 'README.md', catalog_readme(entries))
    write_atomic(ROOT / 'profile' / 'README.md', catalog_readme(entries, '../'))
    print(f'Rebuilt {len(entries)} game pages, the root README, and the organization profile.', flush=True)


def inputs(args):
    values = list(args.links)
    if args.file:
        values += [line.strip() for line in args.file.read_text().splitlines()
                   if line.strip() and not line.lstrip().startswith('#')]
    if any(not safe_url(value) for value in values):
        raise ValueError('Require public HTTP(S) game links')
    return list(dict.fromkeys(values))


def prompt_for(url, template):
    return template.replace('{{repository_url}}', url).replace(
        '{{catalog_readme_path}}', str(ROOT / 'README.md'))


def prepare_analysis(links, args, output):
    WORK.mkdir(exist_ok=True)
    output.mkdir(parents=True, exist_ok=True)
    base = test_oc.ensure_server(args, WORK)
    batch = WORK / 'game-batches' / (str(os.getenv('GITHUB_RUN_ID', time.time_ns())) +
                                   '-' + os.getenv('GITHUB_RUN_ATTEMPT', '1'))
    (batch / 'records').mkdir(parents=True)
    template = args.prompt.read_text()
    if not template.strip():
        raise ValueError('Prompt must not be empty')
    runs = []
    for index, url in enumerate(links, 1):
        meta = test_oc.prepare(index, args, batch, base, prompt_for(url, template))
        result = json.loads((meta / 'result.json').read_text())
        runs.append({'input_url': url, 'meta': str(meta), 'live_url': result['live_url']})
    manifest = {'base': base, 'runs': runs}
    write_atomic(output / 'sessions.json', json.dumps(manifest, indent=2) + '\n')
    return manifest


def redact(text):
    # Commit diagnostic evidence, never common credential formats or known environment secrets.
    for key, value in os.environ.items():
        if len(value) >= 8 and re.search(r'TOKEN|PASSWORD|SECRET|API_KEY', key, re.I):
            text = text.replace(value, '[REDACTED]')
    text = re.sub(r'-----BEGIN [^-]*PRIVATE KEY-----.*?-----END [^-]*PRIVATE KEY-----',
                  '[REDACTED PRIVATE KEY]', text, flags=re.S)
    text = re.sub(r'(?:gh[pousr]_[A-Za-z0-9_]{20,}|github_pat_[A-Za-z0-9_]+|sk-[A-Za-z0-9_-]{20,})',
                  '[REDACTED]', text)
    text = re.sub(r'(?i)(authorization[\"\s:]+(?:bearer|basic)\s+)[^\s\"\\]+', r'\1[REDACTED]', text)
    return text


def repository_created(url):
    if not url:
        return None
    owner, repo = urlsplit(url).path.strip('/').split('/')[:2]
    headers = {'User-Agent': 'AwesomeClaude'}
    if os.getenv('GH_TOKEN'):
        headers['Authorization'] = 'Bearer ' + os.environ['GH_TOKEN']
    request = urllib.request.Request(f'https://api.github.com/repos/{owner}/{repo}', headers=headers)
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)['created_at']


def collect_analysis(run, result, base, args, output):
    url, meta = run['input_url'], Path(run['meta'])
    now = datetime.now(timezone.utc).isoformat()
    item = {'input_url': url, 'status': 'failed', 'reason': '',
            'analysis': {'analyzed_at': now, 'model': args.model,
                         'actions_run': os.getenv('ISSUE_CATALOG_RUN_URL'),
                         'session_id': result['session_id'], 'prompt_sha256': result['prompt_sha256']},
            'record': result['run']}
    evidence = output / 'records' / result['run']
    evidence.mkdir(parents=True, exist_ok=True)
    for name in ('prompt.txt', 'events.jsonl', 'stderr.log', 'result.json'):
        if (meta / name).is_file():
            write_atomic(evidence / name, redact((meta / name).read_text()))
    try:
        messages = test_oc.api(base, f"/session/{result['session_id']}/message", result['directory'])
        write_atomic(evidence / 'messages.json', redact(json.dumps(messages, indent=2)) + '\n')
    except Exception as exc:
        write_atomic(evidence / 'export-error.txt', str(exc))
    workspace = Path(result['directory'])
    for name in ('readme.json', 'rejection.json'):
        if (workspace / name).is_file():
            write_atomic(evidence / ('candidate-' + name), redact((workspace / name).read_text()))
    try:
        if result['status'] != 'finished':
            raise ValueError(f"OpenCode {result['status']}")
        workspace = Path(result['directory'])
        if (workspace / 'rejection.json').exists():
            rejection = json.loads((workspace / 'rejection.json').read_text())
            raise ValueError(str(rejection.get('reason', 'Not an inspectable game')))
        data = json.loads((workspace / 'readme.json').read_text())
        data['source_url'] = url
        modes = data.get('player_modes', {}).get('modes', [])
        data.get('player_modes', {})['modes'] = [m.replace('-multiplayer', ' multiplayer') for m in modes]
        validate(data)
        slug = data.get('catalog_slug')
        if slug and not (catalog_path(slug) / 'readme.json').is_file():
            raise ValueError('Selected existing catalog slug does not exist')
        data['repository_created_at'] = None
        data['analysis'] = item['analysis']
        write_atomic(evidence / 'report.json', json.dumps(data, indent=2) + '\n')
        item.update(status='analyzed', output=str(report_destination(data).relative_to(ROOT)), title=data['title'])
    except Exception as exc:
        item['reason'] = str(exc)[:500]
    return item


def analyze_links(args, output):
    manifest = json.loads((output / 'sessions.json').read_text())
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, len(manifest['runs']))) as pool:
        pending = [(run, pool.submit(test_oc.run_one, Path(run['meta']), manifest['base'], args.timeout))
                   for run in manifest['runs']]
        for run, future in pending:
            results.append(collect_analysis(run, future.result(), manifest['base'], args, output))
            write_atomic(output / 'outcomes.json', json.dumps(results, indent=2) + '\n')
    return results


def existing_report(data):
    destination = report_destination(data)
    if (destination / 'readme.json').exists():
        return destination
    # Recheck concrete identity against the latest catalog, including newly merged runs.
    for path in sorted(GAMES.rglob('readme.json')):
        if 'analysis' in path.relative_to(GAMES).parts:
            continue
        old = json.loads(path.read_text())
        if data.get('repository_url') and old.get('repository_url') and (
                game_url(data['repository_url'])[1].as_posix().casefold() ==
                game_url(old['repository_url'])[1].as_posix().casefold()):
            return path.parent
        if data.get('play_game_url') and data['play_game_url'] == old.get('play_game_url'):
            return path.parent
        if data['source_url'] == old.get('source_url', old.get('repository_url')):
            return path.parent
    return destination


def git_value(*args):
    result = subprocess.run(['git', *args], cwd=ROOT, capture_output=True, text=True, check=True)
    return result.stdout.strip()


def content_only(data):
    data = dict(data)
    data['screenshots'] = [{k: v for k, v in shot.items() if k not in {
        'local_path', 'sha256', 'downloaded_at', 'download_error', 'archive_url'}} for shot in data['screenshots']]
    return {k: v for k, v in data.items() if k not in {
        'analysis', 'catalog_added_at', 'catalog_updated_at', 'previous_report_url', 'catalog_slug'}}


def apply_results(artifact, outcomes):
    run_key = os.getenv('GITHUB_RUN_ID', str(time.time_ns())) + '-' + os.getenv('GITHUB_RUN_ATTEMPT', '1')
    repo = os.getenv('GITHUB_REPOSITORY', 'AwesomeClaude/.github')
    changed = set()
    history = []
    for item in outcomes:
        record = item.get('record')
        evidence = artifact / 'records' / record if record else None
        data = None
        destination = None
        if item['status'] == 'analyzed':
            try:
                data = validate(json.loads((evidence / 'report.json').read_text()))
                data['repository_created_at'] = repository_created(data['repository_url'])
            except Exception as exc:
                item.update(status='failed', reason=f'Repository metadata or report validation failed: {exc}')
        if item['status'] == 'analyzed':
            destination = existing_report(data)
            old_path = destination / 'readme.json'
            old = json.loads(old_path.read_text()) if old_path.exists() else None
            if old:
                old = validate(old)
                data['links'] = labeled_links(old['links'], data['links'])
                # Keep original submission stable; retain new submissions in labeled links.
                data['source_url'] = old['source_url']
            # Reuse durable snapshots across report refreshes, not model-provided paths.
            previous_shots = {shot['url']: shot for shot in old['screenshots']} if old else {}
            for shot in data['screenshots']:
                for key in ('local_path', 'sha256', 'downloaded_at', 'download_error', 'archive_url'):
                    shot.pop(key, None)
                previous = previous_shots.get(shot['url'])
                if previous and screenshots.local_path(destination, previous):
                    for key in ('local_path', 'sha256', 'downloaded_at', 'archive_url'):
                        if key in previous:
                            shot[key] = previous[key]
            screenshots.archive(destination, data, retry=True)
            data['catalog_slug'] = str(destination.relative_to(GAMES))
            status = 'added' if old is None else ('unchanged' if content_only(old) == content_only(data) else 'updated')
            item.update(status=status, output=str(destination.relative_to(ROOT)),
                        title=data['title'], before=old, report=data)
            if status != 'unchanged':
                now = item['analysis']['analyzed_at']
                first = git_value('log', '--diff-filter=A', '--format=%aI', '--', str(old_path.relative_to(ROOT))).splitlines() if old else []
                data['catalog_added_at'] = (old.get('catalog_added_at') or (first[-1] if first else now)) if old else now
                data['catalog_updated_at'] = now
                if old:
                    previous = git_value('log', '-1', '--format=%H', '--', str((destination / 'README.md').relative_to(ROOT)))
                    if previous:
                        data['previous_report_url'] = f'https://github.com/{repo}/blob/{previous}/{destination.relative_to(ROOT)}/README.md'
                write_atomic(old_path, json.dumps(data, indent=2, ensure_ascii=False) + '\n')
                changed.add(str(destination.relative_to(ROOT)))
            else:
                if old['screenshots'] != data['screenshots']:
                    old['screenshots'] = data['screenshots']
                    write_atomic(old_path, json.dumps(old, indent=2, ensure_ascii=False) + '\n')
                    changed.add(str(destination.relative_to(ROOT)))
                item['report'] = old
        else:
            for path in GAMES.rglob('readme.json'):
                if 'analysis' not in path.relative_to(GAMES).parts:
                    old = json.loads(path.read_text())
                    urls = [l['url'] for l in labeled_links(old.get('links', []))]
                    if item['input_url'] in urls + [old.get('source_url'), old.get('repository_url')]:
                        destination = path.parent
                        item.update(output=str(destination.relative_to(ROOT)), report=old, title=old['title'])
                        break
        logs = (destination or GAMES) / 'analysis' / run_key / (record or 'incomplete')
        if evidence and evidence.exists():
            for file in evidence.iterdir():
                if file.is_file():
                    write_atomic(logs / file.name, redact(file.read_text()))
        log_entry = {k: v for k, v in item.items() if k not in ('before', 'report')}
        log_entry['logs'] = str(logs.relative_to(ROOT)) if evidence else None
        history.append(log_entry)
        write_atomic(GAMES / 'history' / f'{run_key}.jsonl',
                     ''.join(json.dumps(entry, ensure_ascii=False) + '\n' for entry in history))
    if changed:
        rebuild()
    return changed


def analyze(items, args):
    output = WORK / ('catalog-' + str(time.time_ns()))
    prepare_analysis(items, args, output)
    results = analyze_links(args, output)
    apply_results(output, results)
    for item in results:
        print(f"{item['status'].title()}: {item['input_url']}", flush=True)
    return not any(item['status'] == 'failed' for item in results)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('links', nargs='*', help='Public game URLs')
    parser.add_argument('--retry-screenshots', action='store_true', help='Retry unavailable screenshot sources')
    parser.add_argument('--file', type=Path, help='Read additional URLs, one per line')
    parser.add_argument('--timeout', type=float, default=900, help='Seconds per agent')
    parser.add_argument('--prompt', type=Path, default=ROOT / 'prompt.md')
    parser.add_argument('--model', default=test_oc.MODEL)
    parser.add_argument('--executable', default='opencode')
    parser.add_argument('--server', help='Existing local OpenCode server URL')
    parser.add_argument('--web-base', help='Existing live-session URL base')
    parser.add_argument('--port', type=int, default=4096)
    args = parser.parse_args()
    if not 0 < args.timeout < float('inf'):
        parser.error('timeout must be positive and finite')
    try:
        items = inputs(args)
        WORK.mkdir(exist_ok=True)
        with (WORK / 'games.lock').open('w') as lock:
            try:
                fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError:
                raise RuntimeError('Another game catalog run is active')
            succeeded = True
            if items:
                executable = shutil.which(args.executable)
                if not executable or not shutil.which('git'):
                    raise RuntimeError('Require opencode and git on PATH')
                args.executable = str(Path(executable).resolve())
                succeeded = analyze(items, args)
            rebuild(retry_screenshots=args.retry_screenshots)
        return 0 if succeeded else 1
    except (OSError, ValueError, RuntimeError) as exc:
        log(str(exc))
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
