import fcntl
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import tempfile
import threading
import time
import unittest

import test_oc as runner


class RunnerTests(unittest.TestCase):
    REPO = 'https://github.com/bridge-mind/turbo-kart-rally/tree/main'

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='oc tests ')
        self.root = Path(self.temp.name)
        (self.root / 'scripts').mkdir()
        for name in ['test-oc.sh', 'test_oc.py']:
            shutil.copy2(runner.ROOT / 'scripts' / name, self.root / 'scripts' / name)
        (self.root / 'prompt.md').write_text('Analyze {{repository_url}}; cite {{repository_url}}')
        self.release = self.root / 'release'
        self.fake = self.root / 'fake-oc'
        self.fake.write_text(f'''#!{sys.executable}
import pathlib, time, sys
assert pathlib.Path('.git').is_dir()
deadline = time.monotonic() + 15
while not pathlib.Path({str(self.release)!r}).exists() and time.monotonic() < deadline:
    time.sleep(.05)
pathlib.Path('readme.json').write_text('not JSON')
''')
        self.fake.chmod(0o755)
        self.requests = []
        owner = self

        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                self.send_json({'healthy': True})

            def do_POST(self):
                self.rfile.read(int(self.headers.get('Content-Length', '0')))
                owner.requests.append(self.path)
                if self.path == '/session' and (getattr(owner, 'fail_session', False) or
                    len(owner.requests) == getattr(owner, 'fail_at', 0)):
                    self.send_error(500)
                else:
                    self.send_json({'id': f'ses_{len(owner.requests)}'})

            def send_json(self, value):
                data = json.dumps(value).encode()
                self.send_response(200)
                self.send_header('Content-Length', str(len(data)))
                self.end_headers()
                self.wfile.write(data)

            def log_message(self, *_):
                pass

        self.server = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.base = f'http://127.0.0.1:{self.server.server_port}'
        self.batch = self.root / 'work/oc-batch-test'

    def tearDown(self):
        if not self.unlocked():
            pid = self.batch / 'worker.pid'
            if pid.exists():
                os.kill(int(pid.read_text()), signal.SIGTERM)
            self.wait_for(self.unlocked)
        self.server.shutdown()
        self.server.server_close()
        self.thread.join()
        self.temp.cleanup()

    def launch(self, *flags):
        return subprocess.run(['/bin/sh', str(self.root / 'scripts/test-oc.sh'),
            '--server', self.base, '--executable', str(self.fake), '--repo', self.REPO, *flags],
            cwd='/', capture_output=True, text=True, timeout=10)

    def unlocked(self):
        path = self.root / 'work/oc-batch.lock'
        if not path.exists():
            return True
        with path.open('a') as lock:
            try:
                fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
                return True
            except BlockingIOError:
                return False

    def wait_for(self, predicate):
        deadline = time.monotonic() + 10
        while time.monotonic() < deadline:
            if predicate():
                return
            time.sleep(.05)
        self.fail('Timed out waiting for detached worker')

    def results(self):
        return [json.loads(p.read_text()) for p in sorted((self.batch / 'records').glob('run-*/result.json'))]

    def test_detached_default_three_urls_lock_and_archive(self):
        completed = self.launch()
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertEqual(completed.stdout.count(' live]('), 3)
        self.assertFalse(self.unlocked())
        for path in (self.batch / 'records').glob('run-*/prompt.txt'):
            self.assertEqual(path.read_text(), f'Analyze {self.REPO}; cite {self.REPO}')
        self.assertNotEqual(self.launch().returncode, 0)
        self.release.touch()
        self.wait_for(self.unlocked)
        self.assertTrue(all(r['status'] == 'finished' for r in self.results()))
        self.assertFalse(list(self.batch.glob('summary.*')))
        self.assertEqual(self.launch('--runs', '1').returncode, 0)
        self.wait_for(self.unlocked)
        self.assertTrue((self.root / 'work/oc-previous-batches/batch-001/run-001/readme.json').exists())

    def test_prompt_overrides_both_forms(self):
        prompt = self.root / 'custom prompt.md'
        prompt.write_text('custom exact prompt')
        self.release.touch()
        for flags in [('--prompt', str(prompt)), (f'--prompt={prompt}',)]:
            completed = self.launch('--runs', '1', *flags)
            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.wait_for(self.unlocked)
            self.assertEqual((self.batch / 'records/run-001/prompt.txt').read_text(), 'custom exact prompt')

    def test_repository_url_required_and_validated(self):
        command = ['/bin/sh', str(self.root / 'scripts/test-oc.sh'),
            '--server', self.base, '--executable', str(self.fake)]
        missing = subprocess.run(command, capture_output=True, text=True)
        self.assertNotEqual(missing.returncode, 0)
        self.assertIn('Require --repo', missing.stderr)
        invalid = self.launch('--repo', 'https://example.com/owner/repo')
        self.assertNotEqual(invalid.returncode, 0)
        self.assertIn('Require a GitHub repository URL', invalid.stderr)
        self.assertFalse(self.batch.exists())

    def test_timeout_aborts_session(self):
        self.assertEqual(self.launch('--runs', '1', '--timeout', '.2').returncode, 0)
        self.wait_for(self.unlocked)
        self.assertEqual(self.results()[0]['status'], 'timeout')
        self.assertTrue(any(p.endswith('/abort') for p in self.requests))

    def test_worker_signal_aborts_and_unlocks(self):
        self.assertEqual(self.launch('--runs', '1').returncode, 0)
        self.wait_for(lambda: self.results()[0]['status'] == 'running')
        os.kill(int((self.batch / 'worker.pid').read_text()), signal.SIGTERM)
        self.wait_for(self.unlocked)
        self.assertEqual(self.results()[0]['status'], 'interrupted')
        self.assertTrue(any(p.endswith('/abort') for p in self.requests))

    def test_report_content_and_presence_do_not_affect_status(self):
        self.release.touch()
        self.assertEqual(self.launch('--runs', '1').returncode, 0)
        self.wait_for(self.unlocked)
        self.assertEqual(self.results()[0]['status'], 'finished')
        self.fake.write_text(f'#!{sys.executable}\npass\n')
        self.assertEqual(self.launch('--runs', '1').returncode, 0)
        self.wait_for(self.unlocked)
        self.assertEqual(self.results()[0]['status'], 'finished')
        self.assertFalse((self.batch / 'run-001/readme.json').exists())

    def test_nonzero_exit_fails(self):
        self.fake.write_text(f'#!{sys.executable}\nimport sys; sys.exit(7)\n')
        self.assertEqual(self.launch('--runs', '1').returncode, 0)
        self.wait_for(self.unlocked)
        self.assertEqual(self.results()[0]['status'], 'failed')
        self.assertEqual(self.results()[0]['exit_code'], 7)

    def test_session_startup_failure(self):
        self.fail_session = True
        completed = self.launch()
        self.assertNotEqual(completed.returncode, 0)
        self.assertTrue(self.unlocked())
        self.assertFalse((self.batch / 'worker.pid').exists())

    def test_partial_session_startup_failure_aborts_created_sessions(self):
        self.fail_at = 2
        self.assertNotEqual(self.launch().returncode, 0)
        self.assertTrue(any(p.endswith('/abort') for p in self.requests))
        self.assertTrue(self.unlocked())
        self.assertEqual(self.results()[0]['status'], 'failed')

    def test_worker_startup_failure(self):
        script = self.root / 'scripts/test_oc.py'
        script.write_text(script.read_text().replace('return worker(args)', 'return 1'))
        completed = self.launch('--runs', '1')
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn('Worker failed to start', completed.stderr)
        self.assertTrue(self.unlocked())
        self.assertTrue(any(p.endswith('/abort') for p in self.requests))

    def test_five_concurrent_runs(self):
        completed = self.launch('--runs', '5')
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertEqual(completed.stdout.count(' live]('), 5)
        self.wait_for(lambda: all(r['status'] == 'running' for r in self.results()))
        self.release.touch()
        self.wait_for(self.unlocked)
        self.assertTrue(all(r['status'] == 'finished' for r in self.results()))

    def test_archive_numbering_and_symlinks(self):
        work = self.root / 'archive-test'
        work.mkdir()
        current = runner.archive(work)
        (current / 'evidence').write_text('keep')
        (work / 'oc-previous-batches/batch-007').mkdir()
        runner.archive(work)
        self.assertEqual((work / 'oc-previous-batches/batch-008/evidence').read_text(), 'keep')
        current.rmdir()
        current.symlink_to(self.root, target_is_directory=True)
        with self.assertRaises(ValueError):
            runner.archive(work)

    def test_url(self):
        self.assertEqual(runner.live_url('http://localhost:4096/', '/tmp/run', 'ses_1'),
                         'http://localhost:4096/L3RtcC9ydW4/session/ses_1')


if __name__ == '__main__':
    unittest.main()
