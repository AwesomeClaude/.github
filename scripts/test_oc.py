#!/usr/bin/env python3
"""Run repeatable OpenCode batches; keep logs outside each agent workspace."""
import argparse
import base64
import concurrent.futures
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import signal
import subprocess
import threading
import time
import urllib.request

ROOT = Path(__file__).resolve().parent.parent
MODEL = 'opencode/muse-spark-1.3-contributor-free'
STOP = threading.Event()


def save(path, value):
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(json.dumps(value, indent=2) + '\n')
    tmp.replace(path)


def archive(work):
    current, previous = work / 'oc-batch-test', work / 'oc-previous-batches'
    if current.is_symlink() or previous.is_symlink():
        raise ValueError('Refuse symlink batch/archive paths')
    previous.mkdir(parents=True, exist_ok=True)
    if current.exists():
        numbers = [int(p.name[6:]) for p in previous.iterdir()
                   if re.fullmatch(r'batch-\d+', p.name)]
        destination = previous / f'batch-{max(numbers, default=0) + 1:03d}'
        current.rename(destination)
        print(f'Archived: {destination}', flush=True)
    current.mkdir()
    return current


def api(base, path, directory=None, payload=None):
    headers = {'Content-Type': 'application/json'}
    if directory:
        headers['x-opencode-directory'] = str(directory)
    password = os.getenv('OPENCODE_SERVER_PASSWORD')
    if password:
        credentials = os.getenv('OPENCODE_SERVER_USERNAME', 'opencode') + ':' + password
        headers['Authorization'] = 'Basic ' + base64.b64encode(credentials.encode()).decode()
    request = urllib.request.Request(base + path, headers=headers,
        data=None if payload is None else json.dumps(payload).encode())
    with urllib.request.urlopen(request, timeout=10) as response:
        return json.load(response)


def live_url(base, directory, session):
    encoded = base64.urlsafe_b64encode(str(directory).encode()).decode().rstrip('=')
    return f'{base.rstrip("/")}/{encoded}/session/{session}'


def ensure_server(args, work):
    base = (args.server or f'http://127.0.0.1:{args.port}').rstrip('/')
    def healthy():
        try:
            return api(base, '/global/health').get('healthy') is True
        except Exception:
            return False
    if healthy():
        return base
    if args.server:
        raise RuntimeError(f'OpenCode server unavailable: {base}')
    runtime = work / 'oc-server'
    runtime.mkdir(exist_ok=True)
    with (runtime / 'server.log').open('ab') as log:
        process = subprocess.Popen([args.executable, 'serve', '--hostname', '127.0.0.1',
            '--port', str(args.port)], cwd=runtime, stdout=log, stderr=log,
            stdin=subprocess.DEVNULL, start_new_session=True)
    save(runtime / 'server.json', {'pid': process.pid, 'base_url': base})
    for _ in range(100):
        if healthy():
            return base
        if process.poll() is not None or STOP.is_set():
            break
        time.sleep(.2)
    if process.poll() is None:
        process.terminate()
        process.wait(timeout=10)
    raise RuntimeError(f'Server failed to start; inspect {runtime / "server.log"}')


def validate(directory, events):
    reports = [p for p in directory.rglob('*') if p.is_file() and not p.is_symlink()
               and p.suffix.lower() == '.md' and '.git' not in p.parts
               and p.name.upper() != 'AGENTS.MD']
    reports.sort(key=lambda p: p.stat().st_size, reverse=True)
    text = reports[0].read_text(errors='replace') if reports else ''
    patterns = {
        'source_analysis': r'source|architecture', 'screenshots': r'screenshot',
        'reconstruction_prompt': r'reverse.engineer|reconstruct|creation prompt',
        'how_to_play': r'how to play', 'mechanics': r'mechanics', 'tags': r'\btags\b',
        'rating': r'\bAAA\b', 'synthetic_reviews': r'synthetic|fictional|simulated',
        'links': r'https://github.com/phirogue/SparkyGames',
    }
    checks = {key: bool(re.search(pattern, text, re.I)) for key, pattern in patterns.items()}
    checks['three_ratings'] = len(re.findall(r'\b[0-5](?:\.\d+)?\s*/\s*5\b', text)) >= 3
    checks['substantial_report'] = len(text.split()) >= 600
    evidence, errors = [], []
    if events.exists():
        for line in events.read_text(errors='replace').splitlines():
            try:
                event = json.loads(line)
            except ValueError:
                continue
            if event.get('type') == 'error':
                errors.append(event)
            part = event.get('part', {})
            if event.get('type') == 'tool_use':
                state = part.get('state', {})
                if state.get('status') == 'error':
                    errors.append({'tool': part.get('tool'), 'error': state.get('error')})
                if re.search(r'\.png|\.jpe?g|\.webp', json.dumps(state.get('input', {})), re.I):
                    evidence.append({'tool': part.get('tool'), 'status': state.get('status'),
                                     'input': state.get('input')})
    return {'report_generated': bool(text.strip()),
            'reports': [str(p.relative_to(directory)) for p in reports],
            'structural_pass': all(checks.values()), 'checks': checks,
            'quality_pass': None, 'quality_note': 'Require human factual and visual review; structural checks do not prove quality.',
            'image_related_tool_calls': evidence, 'tool_errors': errors}


def stop_group(process):
    if process.poll() is None:
        try:
            os.killpg(process.pid, signal.SIGTERM)
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            os.killpg(process.pid, signal.SIGKILL)
            process.wait()
        except ProcessLookupError:
            pass


def run_one(index, args, batch, base, prompt, publish):
    name = f'run-{index:03d}'
    directory = (batch / name).resolve()
    directory.mkdir()
    # Git boundaries prevent accidental parent-repository discovery, not filesystem access.
    subprocess.run(['git', 'init', '-q', str(directory)], check=True)
    meta = batch / 'records' / name
    meta.mkdir(parents=True)
    (meta / 'prompt.txt').write_text(prompt)
    result = {'run': name, 'directory': str(directory), 'status': 'starting',
              'prompt_sha256': hashlib.sha256(prompt.encode()).hexdigest()}
    started = time.monotonic()
    process = None
    session = None
    try:
        session = api(base, '/session', directory, {'title': f'OC batch {name}'})['id']
        result.update(session_id=session, live_url=live_url(args.web_base or base, directory, session))
        print(f'[{name} live]({result["live_url"]})', flush=True)
        result['status'] = 'running'
        save(meta / 'result.json', result)
        publish(result)
        command = [args.executable, 'run', '--auto', '--attach', base, '--dir', str(directory),
                   '--session', session, '--model', args.model, '--format', 'json', '--', prompt]
        save(meta / 'command.json', command)
        with (meta / 'events.jsonl').open('w') as out, (meta / 'stderr.log').open('w') as err:
            process = subprocess.Popen(command, cwd=directory, stdout=out, stderr=err,
                                       stdin=subprocess.DEVNULL, start_new_session=True)
            while process.poll() is None:
                if STOP.is_set() or time.monotonic() - started >= args.timeout:
                    result['status'] = 'interrupted' if STOP.is_set() else 'timeout'
                    # Attached runs execute on the server; killing the CLI alone is insufficient.
                    try:
                        api(base, f'/session/{session}/abort', directory, {})
                    except Exception as exc:
                        result['abort_error'] = str(exc)
                    stop_group(process)
                    break
                time.sleep(.2)
            result['exit_code'] = process.returncode
        if result['status'] == 'running':
            result['status'] = 'finished' if process.returncode == 0 else 'failed'
    except Exception as exc:
        result.update(status='failed', error=str(exc))
        if process:
            stop_group(process)
    result.update(elapsed_seconds=round(time.monotonic() - started, 2),
                  validation=validate(directory, meta / 'events.jsonl'))
    save(meta / 'result.json', result)
    publish(result)
    print(f'{name}: {result["status"]}; report={result["validation"]["report_generated"]}; '
          f'structure={result["validation"]["structural_pass"]}', flush=True)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--runs', type=int, default=10)
    parser.add_argument('--parallel', type=int, default=3)
    parser.add_argument('--timeout', type=float, default=900, help='Seconds per run')
    parser.add_argument('--prompt', type=Path, default=Path(__file__).with_name('oc-analysis-prompt.txt'))
    parser.add_argument('--model', default=MODEL)
    parser.add_argument('--executable', default='opencode')
    parser.add_argument('--server', help='Existing local OpenCode server URL')
    parser.add_argument('--web-base', help='Existing protected web/tunnel URL for live links; does not create a tunnel')
    parser.add_argument('--port', type=int, default=4096)
    args = parser.parse_args()
    if min(args.runs, args.parallel, args.timeout) <= 0:
        parser.error('runs, parallel, and timeout must be positive')
    if not shutil.which(args.executable) or not shutil.which('git'):
        parser.error('Require opencode and git on PATH')
    prompt = args.prompt.read_text()
    if not prompt.strip():
        parser.error('Prompt must not be empty')
    work = ROOT / 'work'
    work.mkdir(exist_ok=True)
    for sig in (signal.SIGINT, signal.SIGTERM):
        signal.signal(sig, lambda *_: STOP.set())
    with (work / 'oc-batch.lock').open('w') as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            parser.error('A batch is already active; refuse to archive it')
        base = ensure_server(args, work)
        batch = archive(work)
        summary_lock, results = threading.Lock(), {}
        def publish(result):
            with summary_lock:
                results[result['run']] = dict(result)
                ordered = [results[k] for k in sorted(results)]
                save(batch / 'summary.json', {'runs_requested': args.runs, 'parallel': args.parallel,
                     'server': base, 'results': ordered})
                lines = ['# OpenCode batch', '', 'Inspect live sessions and require human review before accepting quality.', '',
                         '| Run | State | Report | Structure | Session |', '|---|---|---|---|---|']
                for item in ordered:
                    v = item.get('validation', {})
                    link = f'[Live]({item["live_url"]})' if item.get('live_url') else '—'
                    lines.append(f'| {item["run"]} | {item["status"]} | {v.get("report_generated", "—")} | {v.get("structural_pass", "—")} | {link} |')
                (batch / 'summary.md').write_text('\n'.join(lines) + '\n')
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.parallel) as pool:
            futures = set()
            next_index = 1
            while (next_index <= args.runs and not STOP.is_set()) or futures:
                while not STOP.is_set() and next_index <= args.runs and len(futures) < args.parallel:
                    futures.add(pool.submit(run_one, next_index, args, batch, base, prompt, publish))
                    next_index += 1
                if futures:
                    done, futures = concurrent.futures.wait(futures, timeout=.5,
                        return_when=concurrent.futures.FIRST_COMPLETED)
                    for future in done:
                        future.result()
        print(f'Summary: {batch / "summary.md"}\nKeep server running to inspect sessions.', flush=True)
        if STOP.is_set():
            return 130
        return 0 if all(r['status'] == 'finished' and r['validation']['structural_pass'] for r in results.values()) else 1


if __name__ == '__main__':
    raise SystemExit(main())
