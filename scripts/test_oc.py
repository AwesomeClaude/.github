#!/usr/bin/env python3
"""Launch detached OpenCode runs and print their live session URLs."""
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
import select
import sys
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


def abort(base, result):
    try:
        api(base, f'/session/{result["session_id"]}/abort', result['directory'], {})
    except Exception as exc:
        result['abort_error'] = str(exc)


def prepare(index, args, batch, base, prompt):
    name = f'run-{index:03d}'
    directory = batch / name
    directory.mkdir()
    subprocess.run(['git', 'init', '-q', str(directory)], check=True)
    meta = batch / 'records' / name
    meta.mkdir(parents=True)
    (meta / 'prompt.txt').write_text(prompt, encoding='utf-8')
    session = api(base, '/session', directory, {'title': f'OC batch {name}'})['id']
    result = {'run': name, 'directory': str(directory), 'status': 'queued',
              'session_id': session, 'live_url': live_url(args.web_base or base, directory, session),
              'prompt_sha256': hashlib.sha256(prompt.encode()).hexdigest()}
    save(meta / 'result.json', result)
    save(meta / 'command.json', [args.executable, 'run', '--auto', '--attach', base,
         '--dir', str(directory), '--session', session, '--model', args.model, '--format', 'json', '--', prompt])
    print(f'[{name} live]({result["live_url"]})', flush=True)
    return meta


def run_one(meta, base, timeout):
    result = json.loads((meta / 'result.json').read_text())
    directory = Path(result['directory'])
    started = time.monotonic()
    process = None
    try:
        if STOP.is_set():
            result['status'] = 'interrupted'
            abort(base, result)
        else:
            command = json.loads((meta / 'command.json').read_text())
            with (meta / 'events.jsonl').open('w') as out, (meta / 'stderr.log').open('w') as err:
                process = subprocess.Popen(command, cwd=directory, stdout=out, stderr=err,
                                           stdin=subprocess.DEVNULL, start_new_session=True)
                result.update(status='running', cli_pid=process.pid)
                save(meta / 'result.json', result)
                while process.poll() is None:
                    if STOP.is_set() or time.monotonic() - started >= timeout:
                        result['status'] = 'interrupted' if STOP.is_set() else 'timeout'
                        abort(base, result)
                        stop_group(process)
                        break
                    time.sleep(.1)
                result['exit_code'] = process.returncode
            if result['status'] == 'running':
                result['status'] = 'finished' if process.returncode == 0 else 'failed'
    except Exception as exc:
        result.update(status='failed', error=str(exc))
        abort(base, result)
        if process:
            stop_group(process)
    result['elapsed_seconds'] = round(time.monotonic() - started, 2)
    save(meta / 'result.json', result)
    return result


def worker(args):
    # Inherit the launcher's open-file description: keep its flock after it exits.
    with os.fdopen(args.lock_fd, 'w'):
        runs = sorted((args.worker / 'records').glob('run-*'))
        for sig in (signal.SIGINT, signal.SIGTERM):
            signal.signal(sig, lambda *_: STOP.set())
        (args.worker / 'worker.pid').write_text(str(os.getpid()) + '\n')
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(runs)) as pool:
            futures = [pool.submit(run_one, meta, args.server, args.timeout) for meta in runs]
            with os.fdopen(args.ready_fd, 'w') as ready:
                ready.write('ready\n')
            results = [future.result() for future in futures]
    return 0 if all(r['status'] == 'finished' for r in results) else 1


def launch(args, prompt):
    work = ROOT / 'work'
    work.mkdir(exist_ok=True)
    with (work / 'oc-batch.lock').open('w') as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise RuntimeError('A batch is already active; wait for it to finish')
        base = ensure_server(args, work)
        batch = archive(work)
        (batch / 'records').mkdir()
        process = None
        try:
            for index in range(1, args.runs + 1):
                prepare(index, args, batch, base, prompt)
            read_fd, write_fd = os.pipe()
            try:
                with (batch / 'worker.log').open('ab') as log:
                    process = subprocess.Popen([sys.executable, str(Path(__file__).resolve()),
                        '--worker', str(batch), '--server', base, '--timeout', str(args.timeout),
                        '--lock-fd', str(lock.fileno()), '--ready-fd', str(write_fd)],
                        stdin=subprocess.DEVNULL, stdout=log, stderr=log, start_new_session=True,
                        pass_fds=(lock.fileno(), write_fd))
                os.close(write_fd)
                write_fd = None
                readable, _, _ = select.select([read_fd], [], [], 15)
                if not readable or os.read(read_fd, 64) != b'ready\n':
                    raise RuntimeError(f'Worker failed to start; inspect {batch / "worker.log"}')
            finally:
                os.close(read_fd)
                if write_fd is not None:
                    os.close(write_fd)
        except BaseException:
            if process:
                stop_group(process)
            for meta in (batch / 'records').glob('run-*'):
                path = meta / 'result.json'
                if path.exists():
                    result = json.loads(path.read_text())
                    abort(base, result)
                    result.update(status='failed', error='Batch launch did not complete')
                    save(path, result)
            raise
    # Success means launched, never completed. The detached worker owns the lock.
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--runs', type=int, default=3)
    parser.add_argument('--timeout', type=float, default=900, help='Seconds per run')
    parser.add_argument('--prompt', type=Path, default=ROOT / 'prompt.md')
    parser.add_argument('--repo', help='GitHub repository URL, optionally with /tree/<branch>')
    parser.add_argument('--model', default=MODEL)
    parser.add_argument('--executable', default='opencode')
    parser.add_argument('--server', help='Existing local OpenCode server URL')
    parser.add_argument('--web-base', help='Existing protected web/tunnel URL for live links')
    parser.add_argument('--port', type=int, default=4096)
    parser.add_argument('--worker', type=Path, help=argparse.SUPPRESS)
    parser.add_argument('--lock-fd', type=int, help=argparse.SUPPRESS)
    parser.add_argument('--ready-fd', type=int, help=argparse.SUPPRESS)
    args = parser.parse_args()
    if args.worker:
        return worker(args)
    if not args.repo:
        parser.error('Require --repo')
    if not re.fullmatch(r'https://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+(?:/tree/[A-Za-z0-9_./-]+)?/?', args.repo):
        parser.error('Require a GitHub repository URL, optionally with /tree/<branch>')
    args.repo = args.repo.rstrip('/')
    if args.runs <= 0 or not 0 < args.timeout < float('inf'):
        parser.error('runs and timeout must be positive and finite')
    executable = shutil.which(args.executable)
    if not executable or not shutil.which('git'):
        parser.error('Require opencode and git on PATH')
    args.executable = str(Path(executable).resolve())
    try:
        prompt = args.prompt.read_text(encoding='utf-8')
        if not prompt.strip():
            parser.error('Prompt must not be empty')
        prompt = prompt.replace('{{repository_url}}', args.repo)
        return launch(args, prompt)
    except KeyboardInterrupt:
        return 130
    except (OSError, ValueError, RuntimeError) as exc:
        parser.exit(1, f'{exc}\n')


if __name__ == '__main__':
    raise SystemExit(main())
