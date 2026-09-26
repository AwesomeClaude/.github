#!/usr/bin/env python3
"""Publish an issue catalog artifact on a review branch and comment on the issue."""

import argparse
import json
import os
from pathlib import Path
import subprocess

import games


def command(*args, check=True):
    return subprocess.run(args, check=check, text=True, capture_output=True)


def safe_output(value):
    path = Path(value)
    if path.is_absolute() or len(path.parts) < 2 or path.parts[0] != 'games':
        raise ValueError(f'Unsafe artifact path: {value}')
    if any(part in ('.', '..') for part in path.parts):
        raise ValueError(f'Unsafe artifact path: {value}')
    return path


def publish_files(artifact, summary):
    published = set()
    for item in summary['outcomes']:
        if item['status'] not in ('added', 'no_source'):
            continue
        relative = safe_output(item['output'])
        source = artifact / 'publish' / relative / 'readme.json'
        if source.is_symlink() or not source.is_file():
            item.update(status='failed', reason='Report artifact missing')
            continue
        try:
            data = json.loads(source.read_text(encoding='utf-8'))
            if item['status'] == 'no_source':
                games.validate(data, allow_no_source=True)
                expected = games.no_source_destination(data['source_url'])
            else:
                games.validate(data)
                _, expected = games.game_url(data['repository_url'])
            if relative != expected.relative_to(games.ROOT):
                raise ValueError('Report artifact path mismatch')
        except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
            item.update(status='failed', reason=str(exc)[:500])
            continue
        destination = games.ROOT / relative / 'readme.json'
        if destination.exists():
            item.update(status='already_cataloged', reason='Added by another run')
            continue
        games.write_atomic(destination, source.read_text(encoding='utf-8'))
        published.add(str(relative))
    if published:
        ledger = games.GAMES / 'added.jsonl'
        with ledger.open('a', encoding='utf-8') as out:
            for line in (artifact / 'ledger.jsonl').read_text(encoding='utf-8').splitlines():
                row = json.loads(line)
                if row.get('output') in published:
                    out.write(json.dumps(row, ensure_ascii=False) + '\n')
        games.rebuild()
    return published


def issue_comment(summary, link, run_url):
    lines = [f'Issue catalog run: [Actions log]({run_url}).']
    if link:
        lines.append(f'Catalog changes: {link}.')
    else:
        lines.append('No catalog changes were published.')
    if summary.get('error'):
        lines.append(f'Input: {games.markdown(summary["error"])}')
    groups = [
        ('added', 'GitHub-source games'),
        ('no_source', 'Games without GitHub source'),
        ('already_cataloged', 'Already cataloged'),
        ('not_game', 'Not game projects'),
        ('inaccessible', 'Could not inspect'),
        ('failed', 'Failed games'),
    ]
    for status, title in groups:
        items = [item for item in summary['outcomes'] if item['status'] == status]
        if not items:
            continue
        lines.extend(['', f'### {title}'])
        for item in items:
            original = games.safe_url(item['input_url'])
            note = item.get('reason') or item.get('output') or item.get('title') or ''
            lines.append(f'- [Original link]({original}) — {games.markdown(note)[:600]}')
    return '\n'.join(lines) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--artifact', type=Path, required=True)
    args = parser.parse_args()
    repo = os.environ['GITHUB_REPOSITORY']
    run_id = os.environ['GITHUB_RUN_ID']
    summary_path = args.artifact / 'summary.json'
    if summary_path.is_file():
        summary = json.loads(summary_path.read_text(encoding='utf-8'))
    else:
        summary = {'issue_number': int(os.environ['ISSUE_NUMBER']), 'outcomes': [],
                   'error': 'The analysis job did not produce a result artifact.'}
    issue = summary['issue_number']
    run_url = f'https://github.com/{repo}/actions/runs/{run_id}'
    try:
        published = publish_files(args.artifact, summary) if summary_path.is_file() else set()
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        published = set()
        summary['error'] = f'Could not prepare catalog publication: {exc}'
    branch = f'codex/issue-{issue}-run-{run_id}'
    link = None
    if published:
        command('git', 'config', 'user.name', 'github-actions[bot]')
        command('git', 'config', 'user.email', '41898282+github-actions[bot]@users.noreply.github.com')
        command('git', 'switch', '-c', branch)
        command('git', 'add', '--', 'README.md', 'Readme-nosrc.md', 'games')
        command('git', 'diff', '--cached', '--check')
        command('git', 'commit', '-m', f'Add games from issue #{issue}', '-m',
                f'Context: Issue #{issue} requested catalog analysis of public links.\n\n'
                f'Decision: Publish only validated generated reports on a review branch, not directly to the default branch. '
                f'Additions: {len(published)}. Verification: the production analysis completed and the catalog was rebuilt. '
                f'Known caveat: claims in generated reports require human editorial review.\n\n'
                f'Issue: #{issue}\nRun-ID: {run_id}\nChat-ID: 01a0dbeb-cd22-74a3-9140-d15455968a0d')
        command('git', 'push', '--set-upstream', 'origin', branch)
        branch_url = f'https://github.com/{repo}/tree/{branch}'
        link = f'[branch]({branch_url})'
        pr = command('gh', 'pr', 'create', '--repo', repo, '--base', 'main', '--head', branch,
                     '--title', f'Add games requested in issue #{issue}',
                     '--body', f'Collect verified game reports from issue #{issue}.\n\n'
                               f'Analysis run: {run_url}', check=False)
        if pr.returncode == 0:
            link = f'[pull request]({pr.stdout.strip()})'
        else:
            summary['outcomes'].append({'input_url': f'https://github.com/{repo}/issues/{issue}',
                                        'status': 'failed', 'reason': f'PR creation failed: {pr.stderr.strip()[:300]}'})
    comment = issue_comment(summary, link, run_url)
    command('gh', 'issue', 'comment', str(issue), '--repo', repo, '--body', comment)
    print(comment)


if __name__ == '__main__':
    main()
