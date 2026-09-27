#!/usr/bin/env python3
"""Publish validated issue reports, merge the catalog PR, and report the result."""

import argparse
import json
import os
from pathlib import Path
import subprocess
import time
from urllib.parse import quote

import games


def command(*args, check=True):
    result = subprocess.run(args, check=False, text=True, capture_output=True, timeout=120)
    if check and result.returncode:
        raise RuntimeError(f'{args[0]} {args[1]} failed: {result.stderr.strip()[:1000]}')
    return result


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
        if item['status'] != 'added':
            continue
        relative = safe_output(item['output'])
        source = artifact / 'publish' / relative / 'readme.json'
        if source.is_symlink() or not source.is_file():
            item.update(status='failed', reason='Report artifact missing')
            continue
        try:
            data = json.loads(source.read_text(encoding='utf-8'))
            games.validate(data)
            expected = games.report_destination(data)
            if relative != expected.relative_to(games.ROOT):
                raise ValueError('Report artifact path mismatch')
        except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
            item.update(status='failed', reason=str(exc)[:500])
            continue
        destination = games.ROOT / relative / 'readme.json'
        if destination.exists():
            item.update(status='already_cataloged', reason='Added by another run')
            continue
        games.write_atomic(destination, json.dumps(data, indent=2, ensure_ascii=False) + '\n')
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


def issue_comment(summary, link, run_url, repo, branch, published, merge_status):
    lines = [f'Issue catalog run: [Actions log]({run_url}).']
    if link:
        lines.append(f'Catalog changes: {link}.')
    else:
        lines.append('No catalog changes were published.')
    if merge_status:
        lines.append(merge_status)
    if summary.get('error'):
        lines.append(f'Notice: {games.markdown(summary["error"])}')
    groups = [
        ('added', 'Validated games'),
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
            if status == 'added' and item['output'] in published and link:
                relative = safe_output(item['output'])
                readme_url = (f'https://github.com/{repo}/blob/{quote(branch, safe="/")}/'
                              f'{quote(str(relative), safe="/")}/README.md')
                game_title = games.markdown(item.get('title') or relative.name)
                lines.append(f'- [{game_title}]({readme_url}) — [Original link]({original})')
                continue
            note = item.get('reason') or item.get('output') or item.get('title') or ''
            lines.append(f'- [Original link]({original}) — {games.markdown(note)[:600]}')
    return '\n'.join(lines) + '\n'


def merge_pr(repo, pr_url, head, title, body):
    for attempt in range(3):
        result = command('gh', 'pr', 'merge', pr_url, '--repo', repo, '--auto', '--squash',
                         '--match-head-commit', head, '--subject', title, '--body', body,
                         check=False)
        state = command('gh', 'pr', 'view', pr_url, '--repo', repo,
                        '--json', 'state,autoMergeRequest', check=False)
        if state.returncode == 0:
            details = json.loads(state.stdout)
            if details['state'] == 'MERGED':
                return 'Merged automatically into the default catalog branch.'
            if details.get('autoMergeRequest'):
                return 'Auto-merge enabled; waiting for the repository’s merge requirements.'
        if result.returncode == 0:
            return 'Merge requested; check the pull request for its current status.'
        if attempt < 2:
            time.sleep(5)
    return f'Automatic merge failed; inspect the pull request. {games.markdown(result.stderr.strip())[:600]}'


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
    run_url = os.getenv('ISSUE_CATALOG_RUN_URL') or f'https://github.com/{repo}/actions/runs/{run_id}'
    base = os.getenv('CATALOG_BASE_BRANCH', 'main')
    attempt = os.getenv('GITHUB_RUN_ATTEMPT', '1')
    branch = f'codex/issue-{issue}-run-{run_id}-attempt-{attempt}'
    published = set()
    link = None
    pr_url = None
    merge_status = None
    try:
        # Apply validated additions to the latest catalog, not the issue event's stale checkout.
        command('git', 'fetch', 'origin', base)
        command('git', 'switch', '--detach', f'origin/{base}')
        published = publish_files(args.artifact, summary) if summary_path.is_file() else set()
        if published:
            command('git', 'config', 'user.name', 'github-actions[bot]')
            command('git', 'config', 'user.email', '41898282+github-actions[bot]@users.noreply.github.com')
            command('git', 'switch', '-c', branch)
            command('git', 'add', '--', 'README.md', 'games')
            title = f'Add games from issue #{issue}'
            body = (f'Context: Issue #{issue} requested analysis of public game links.\n\n'
                    f'Decision: Publish {len(published)} validated reports through a catalog PR and '
                    f'automatically merge eligible results. Include games with optional source code '
                    f'in the same ranking and gallery instead of splitting the catalog.\n\n'
                    f'Verification: Inspect the production analysis and per-game evidence at {run_url}. '
                    f'Validate report structure and destinations; rebuild the combined catalog. '
                    f'Caveat: Generated claims are limited to the evidence the analysis could inspect.\n\n'
                    f'Issue: #{issue}\nRun-ID: {run_id}\n'
                    f'Chat-ID: {os.environ["CATALOG_CHAT_ID"]}')
            command('git', 'commit', '-m', title, '-m', body)
            head = command('git', 'rev-parse', 'HEAD').stdout.strip()
            command('git', 'push', '--set-upstream', 'origin', branch)
            branch_url = f'https://github.com/{repo}/tree/{branch}'
            link = f'[branch]({branch_url})'
            print(f'Published branch: {branch_url}', flush=True)
            pr = command('gh', 'pr', 'create', '--repo', repo, '--base', base, '--head', branch,
                         '--title', title, '--body', body, check=False)
            if pr.returncode == 0:
                pr_url = pr.stdout.strip()
                link = f'[pull request]({pr_url})'
                print(f'Published pull request: {pr_url}', flush=True)
                if os.getenv('CATALOG_AUTO_MERGE', 'true').lower() == 'false':
                    merge_status = 'Automatic merge is disabled for this repository’s catalog workflow.'
                elif summary.get('error') or any(item['status'] == 'failed' for item in summary['outcomes']) or os.getenv('ANALYSIS_SUCCEEDED') != 'true':
                    merge_status = 'Left the pull request open because analysis or validation did not fully succeed.'
                else:
                    merge_status = merge_pr(repo, pr_url, head, title, body)
            else:
                summary['error'] = f'PR creation failed; inspect the published branch: {pr.stderr.strip()[:600]}'
    except (OSError, ValueError, KeyError, RuntimeError, subprocess.TimeoutExpired) as exc:
        summary['error'] = f'Catalog publication failed: {exc}'
    comment = issue_comment(summary, link, run_url, repo, branch, published, merge_status)
    result = command('gh', 'issue', 'comment', str(issue), '--repo', repo, '--body', comment)
    summary['publication'] = {'branch': branch if link else None, 'pull_request': pr_url,
                              'merge_status': merge_status, 'comment': result.stdout.strip()}
    games.write_atomic(summary_path, json.dumps(summary, indent=2, ensure_ascii=False) + '\n')
    print(comment, flush=True)
    print(f'Issue report: {result.stdout.strip()}', flush=True)
    return int(bool(summary.get('error')) or any(item['status'] == 'failed' for item in summary['outcomes'])
               or bool(merge_status and merge_status.startswith('Automatic merge failed')))


if __name__ == '__main__':
    raise SystemExit(main())
