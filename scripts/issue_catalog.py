#!/usr/bin/env python3
"""Collect game reports from public issue links without trusting issue prose."""

import argparse
import concurrent.futures
from datetime import datetime, timezone
import ipaddress
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import signal
import time
from urllib.parse import quote, urlsplit, urlunsplit

import games
import test_oc


URL_PATTERN = re.compile(r'https?://[^\s<>"\'`]+', re.IGNORECASE)
MAX_PUBLIC_LINKS = 10
MAX_ANALYSIS_SECONDS = 270 * 60


def public_link(value):
    value = value.rstrip('.,;:!?)]}')
    parsed = urlsplit(value)
    host = parsed.hostname
    if parsed.scheme not in ('http', 'https') or not host or parsed.username or parsed.password:
        return None
    if len(value) > 2048 or host.lower() == 'localhost' or host.lower().endswith(('.local', '.internal')):
        return None
    try:
        if not ipaddress.ip_address(host).is_global:
            return None
    except ValueError:
        pass
    return urlunsplit(parsed._replace(fragment=''))


def issue_links(body):
    links = {}
    for match in URL_PATTERN.finditer(body or ''):
        url = public_link(match.group())
        if url:
            links.setdefault(url, None)
    return list(links)


def issue_input(path):
    payload = json.loads(path.read_text(encoding='utf-8'))
    issue = payload['issue']
    owner = issue['user']['login'].casefold() == os.getenv(
        'ISSUE_CATALOG_DEBUG_OWNER', payload['repository']['owner']['login']).casefold()
    links = issue_links(issue.get('body'))
    summary = {'issue_number': issue['number'], 'owner': owner, 'links': links, 'outcomes': []}
    if not links:
        summary['error'] = 'No public HTTP(S) links found in the issue body.'
    elif not owner and len(links) > MAX_PUBLIC_LINKS:
        summary['error'] = f'Non-owner issues may contain at most {MAX_PUBLIC_LINKS} distinct links; found {len(links)}.'
    return summary


def preflight(args):
    summary = issue_input(args.event)
    args.output.mkdir(parents=True, exist_ok=True)
    if not summary.get('error'):
        summary['outcomes'] = [outcome(url, 'failed', 'Analysis did not complete')
                               for url in summary['links']]
    games.write_atomic(args.output / 'summary.json', json.dumps(summary, indent=2, ensure_ascii=False) + '\n')
    games.write_atomic(args.output / 'outcomes.json', '[]\n')
    ready = 'false' if summary.get('error') else 'true'
    if os.getenv('GITHUB_OUTPUT'):
        with Path(os.environ['GITHUB_OUTPUT']).open('a', encoding='utf-8') as out:
            out.write(f'ready={ready}\n')
    print(f'ready={ready} links={len(summary["links"])}', flush=True)


def command(*args, check=True):
    result = subprocess.run(args, check=False, text=True, capture_output=True, timeout=120)
    if check and result.returncode:
        raise RuntimeError(f'{args[0]} {args[1]} failed: {result.stderr.strip()[:1000]}')
    return result


def outcome(url, status, reason='', **extra):
    return {'input_url': url, 'status': status, 'reason': reason, **extra}


def debug_tunnel(args):
    try:
        result = command('bash', str(games.ROOT / 'scripts/start-catalog-debug.sh'), str(args.port))
        args.web_base = result.stdout.strip().splitlines()[-1]
        if not re.fullmatch(r'https://[a-z0-9-]+\.trycloudflare\.com', args.web_base):
            raise ValueError('Tunnel did not return a public URL')
        return True
    except Exception as exc:
        print(f'Live debugging unavailable: {exc}', flush=True)
        return False


def prepare(args):
    summary = issue_input(args.event)
    if summary.get('error'):
        return
    args.executable = shutil.which(args.executable) or args.executable
    args.output.mkdir(parents=True, exist_ok=True)
    games.WORK.mkdir(exist_ok=True)
    test_oc.ensure_server(args, games.WORK)
    debug = summary['owner'] and debug_tunnel(args)
    games.prepare_analysis(summary['links'], args, args.output)
    summary['debug_available'] = bool(debug)
    summary['outcomes'] = [outcome(url, 'failed', 'Analysis did not complete') for url in summary['links']]
    games.write_atomic(args.output / 'summary.json', json.dumps(summary, indent=2) + '\n')


def debug_comment(args, expired=False):
    summary = json.loads((args.output / 'summary.json').read_text())
    if not summary.get('owner'):
        return
    body = Path(os.environ['RUNNER_TEMP']) / 'issue-started.md'
    text = body.read_text()
    if expired:
        pid_path = games.WORK / 'catalog-debug' / 'tunnel.pid'
        if pid_path.exists():
            try:
                os.kill(int(pid_path.read_text()), signal.SIGTERM)
            except ProcessLookupError:
                pass
        text += '\n**Debug session links expired.** The 30-minute debug hold has ended.\n'
    elif summary.get('debug_available'):
        sessions = json.loads((args.output / 'sessions.json').read_text())
        text += '\n### Temporary public OpenCode sessions\nNo login or password. Available through analysis and the 30-minute debug hold.\n'
        for index, run in enumerate(sessions['runs'], 1):
            text += f"- [Game {index} session]({run['live_url']}) — [Submitted link]({games.safe_url(run['input_url'])})\n"
    else:
        text += '\n**Live debugging unavailable.** Game analysis will continue normally.\n'
    comment_id = os.environ['ISSUE_START_COMMENT_ID']
    payload = args.output / 'comment-update.json'
    games.write_atomic(payload, json.dumps({'body': text}))
    command('gh', 'api', '--method', 'PATCH',
            f"repos/{os.environ['GITHUB_REPOSITORY']}/issues/comments/{comment_id}", '--input', str(payload))


def run(args):
    summary = json.loads((args.output / 'summary.json').read_text())
    summary['outcomes'] = games.analyze_links(args, args.output)
    games.write_atomic(args.output / 'summary.json', json.dumps(summary, indent=2) + '\n')


def age_text(value):
    if not value:
        return 'Not established'
    created = datetime.fromisoformat(value.replace('Z', '+00:00'))
    hours = max(0, int((datetime.now(timezone.utc) - created).total_seconds() // 3600))
    age = f'{hours} hours' if hours < 24 else f'{hours // 24} days'
    return f'{created:%Y-%m-%d %H:%M UTC} — {age} ago'


def score_text(report, key):
    value = report.get(key)
    return str(value['score']) if value else 'not scored'


def issue_comment(summary, link, run_url, repo, branch, merge_status):
    lines = [f'Issue catalog run: [Actions log]({run_url}).',
             f'Catalog changes: {link}.' if link else 'No catalog changes were published.']
    counts = {status: sum(item['status'] == status for item in summary['outcomes'])
              for status in ('added', 'updated', 'unchanged', 'failed')}
    lines.append('**Results:** ' + ' · '.join(f'{count} {status}' for status, count in counts.items()))
    if counts['failed']:
        lines.append('Failed submissions retain diagnostics; valid reports publish independently.')
    if merge_status:
        lines.append(merge_status)
    if summary.get('error'):
        lines.append(f"Notice: {games.markdown(summary['error'])}")
    for item in summary['outcomes']:
        status = item['status'].title()
        report = item.get('report', {})
        title = games.markdown(item.get('title') or item['input_url'])
        lines.extend(['', f'### {status} — {title}'])
        links = [f"[Submission]({games.safe_url(item['input_url'])})"]
        if item.get('output'):
            ref = branch if link else os.getenv('CATALOG_BASE_BRANCH', 'main')
            url = f"https://github.com/{repo}/blob/{quote(ref, safe='/')}/{quote(item['output'], safe='/')}/README.md"
            links.insert(0, f'[Report]({url})')
        for label, key in [('Play', 'play_game_url'), ('Source', 'repository_url')]:
            if games.safe_url(report.get(key)):
                links.append(f'[{label}]({games.safe_url(report[key])})')
        if item['status'] == 'updated' and report.get('previous_report_url'):
            links.append(f"[Previous report]({report['previous_report_url']})")
        lines.append(' · '.join(links))
        if report:
            scores = []
            for label, key in [('Overall', 'rating'), ('Graphics', 'screenshot_based_score')]:
                value = score_text(report, key)
                if item['status'] == 'updated':
                    value = score_text(item['before'], key) + ' → ' + value
                scores.append(f'{label} {value}')
            lines.append('**Scores:** ' + ' · '.join(scores))
            missing = sum(bool(shot.get('download_error')) for shot in report['screenshots'])
            if missing:
                lines.append(f'**Screenshots:** {missing} unavailable; retained source URLs and download diagnostics.')
            if report.get('creation_models'):
                lines.append('**Built with:** ' + ', '.join(
                    f"[{games.markdown(m['name'])}]({games.safe_url(m['evidence_url'])})" for m in report['creation_models']))
            if report.get('repository_url'):
                lines.append('**Repository created:** ' + age_text(report.get('repository_created_at')))
        if item['status'] == 'unchanged':
            lines.append('Reanalyzed; report content unchanged.')
        if item.get('reason'):
            lines.append(games.markdown(item['reason']))
    return '\n'.join(lines) + '\n'


def acquire_publication_lock(repo, base):
    # GitHub ref creation is atomic; serialize only fetch/apply/PR/merge, never analysis or hold.
    ref = 'refs/heads/codex/catalog-publication-lock'
    for _ in range(90):
        head = command('gh', 'api', f'repos/{repo}/git/ref/heads/{base}', '--jq', '.object.sha').stdout.strip()
        attempt = command('gh', 'api', '--method', 'POST', f'repos/{repo}/git/refs',
                          '-f', f'ref={ref}', '-f', f'sha={head}', check=False)
        if attempt.returncode == 0:
            return
        if 'Reference already exists' not in attempt.stderr:
            raise RuntimeError(f'Cannot acquire publication lock: {attempt.stderr[:500]}')
        time.sleep(10)
    raise RuntimeError('Publication lock remained busy for 15 minutes; inspect codex/catalog-publication-lock')


def publish(args):
    repo, run_id = os.environ['GITHUB_REPOSITORY'], os.environ['GITHUB_RUN_ID']
    summary_path = args.output / 'summary.json'
    summary = json.loads(summary_path.read_text()) if summary_path.exists() else {
        'issue_number': int(os.environ['ISSUE_NUMBER']), 'outcomes': [], 'error': 'No analysis results'}
    # Recover completed games when a later analysis or export was interrupted.
    outcomes_path = args.output / 'outcomes.json'
    if outcomes_path.exists():
        completed = json.loads(outcomes_path.read_text())
        if completed:
            by_url = {item['input_url']: item for item in completed}
            summary['outcomes'] = [by_url.get(item['input_url'], item) for item in summary['outcomes']]
    if os.getenv('ANALYSIS_SUCCEEDED') != 'true' and not summary.get('error'):
        summary['error'] = 'Analysis pipeline did not complete; inspect the Actions log.'
    base = os.getenv('CATALOG_BASE_BRANCH', 'main')
    run_url = os.getenv('ISSUE_CATALOG_RUN_URL') or f'https://github.com/{repo}/actions/runs/{run_id}'
    branch = f"codex/issue-{summary['issue_number']}-run-{run_id}-attempt-{os.getenv('GITHUB_RUN_ATTEMPT', '1')}"
    link = pr_url = merge_status = None
    locked = False
    try:
        acquire_publication_lock(repo, base)
        locked = True
        command('git', 'fetch', 'origin', base)
        command('git', 'switch', '--detach', f'origin/{base}')
        games.apply_results(args.output, summary['outcomes'])
        command('git', 'add', '--', 'README.md', 'profile/README.md', 'games')
        if command('git', 'diff', '--cached', '--quiet', check=False).returncode:
            command('git', 'config', 'user.name', 'github-actions[bot]')
            command('git', 'config', 'user.email', '41898282+github-actions[bot]@users.noreply.github.com')
            command('git', 'switch', '-c', branch)
            title = f"Refresh games from issue #{summary['issue_number']}"
            counts = {status: sum(i['status'] == status for i in summary['outcomes'])
                      for status in ('added', 'updated', 'unchanged', 'failed')}
            body = (f"Context: Reanalyze issue links; preserve game identity and labeled historical links.\n\n"
                    f"Changes: {json.dumps(counts)}. Commit reports, analysis evidence and refresh provenance; "
                    f"rebuild the unified catalog. Preserve existing reports on failure.\n\n"
                    f"Verification: Inspect live analysis at {run_url}. Model findings remain evidence-limited. "
                    f"Logs are redacted before publication. Git retains prior report versions.\n\n"
                    f"Issue: #{summary['issue_number']}\nRun-ID: {run_id}\n"
                    f"Chat-ID: {os.environ['CATALOG_CHAT_ID']}")
            command('git', 'commit', '-m', title, '-m', body)
            head = command('git', 'rev-parse', 'HEAD').stdout.strip()
            command('git', 'push', '--set-upstream', 'origin', branch)
            link = f'[branch](https://github.com/{repo}/tree/{branch})'
            print(f'Published branch: {link}', flush=True)
            if os.getenv('CATALOG_AUTO_MERGE', 'true').lower() == 'false':
                pr = command('gh', 'pr', 'create', '--repo', repo, '--base', base, '--head', branch,
                             '--title', title, '--body', body, check=False)
                if pr.returncode:
                    raise RuntimeError('Manual-mode PR creation failed: ' + pr.stderr[:500])
                pr_url = pr.stdout.strip()
                link = f'[pull request]({pr_url})'
                merge_status = 'Manual merge enabled; left the PR open for review.'
                print(f'Published pull request: {pr_url}', flush=True)
            elif summary.get('error'):
                merge_status = 'Kept the recovery branch because the analysis pipeline did not complete.'
            else:
                # The branch has one publication commit on the latest base. Advance main
                # without force; reject concurrent changes rather than merge stale indexes.
                command('git', 'fetch', 'origin', base)
                parent = command('git', 'rev-parse', f'{head}^').stdout.strip()
                latest = command('git', 'rev-parse', f'origin/{base}').stdout.strip()
                if latest != parent:
                    raise RuntimeError('Default branch changed during publication; retained the recovery branch.')
                command('git', 'push', 'origin', f'{head}:refs/heads/{base}')
                link = f'[published commit](https://github.com/{repo}/commit/{head})'
                merge_status = 'Merged the catalog branch directly into the default branch.'
                print(f'Published directly: {link}', flush=True)
    except Exception as exc:
        summary['error'] = f'Catalog publication failed: {exc}'
    finally:
        if locked:
            command('gh', 'api', '--method', 'DELETE',
                    f'repos/{repo}/git/refs/heads/codex/catalog-publication-lock', check=False)
    for item in summary['outcomes']:
        if item['status'] == 'analyzed':
            item.update(status='failed', reason='Publication did not complete')
    comment = issue_comment(summary, link, run_url, repo, branch, merge_status)
    result = command('gh', 'issue', 'comment', str(summary['issue_number']), '--repo', repo, '--body', comment)
    summary['publication'] = {'pull_request': pr_url, 'comment': result.stdout.strip(), 'merge_status': merge_status}
    games.write_atomic(summary_path, json.dumps(summary, indent=2) + '\n')
    print(f'Issue report: {result.stdout.strip()}', flush=True)
    return int(bool(summary.get('error'))
               or bool(merge_status and merge_status.startswith('Automatic merge failed')))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--event', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--executable', default='opencode')
    parser.add_argument('--model', default=test_oc.MODEL)
    parser.add_argument('--prompt', type=Path, default=games.ROOT / 'prompt.md')
    parser.add_argument('--timeout', type=float, default=900)
    parser.add_argument('--port', type=int, default=4096)
    parser.add_argument('--server')
    parser.add_argument('--web-base')
    parser.add_argument('--phase', choices=['preflight', 'prepare', 'debug-comment', 'analyze', 'publish', 'expire'], required=True)
    args = parser.parse_args()
    if args.timeout <= 0:
        parser.error('timeout must be positive')
    return {'preflight': preflight, 'prepare': prepare, 'debug-comment': debug_comment,
            'analyze': run, 'publish': publish, 'expire': lambda a: debug_comment(a, expired=True)}[args.phase](args)


if __name__ == '__main__':
    raise SystemExit(main())
