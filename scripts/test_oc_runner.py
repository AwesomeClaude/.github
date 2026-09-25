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
from validate_readme import load_schema, validate


def report():
    source = 'https://github.com/phirogue/SparkyGames'
    claim = {'description': 'A deterministic combat engine.', 'basis': 'observed', 'sources': [source]}
    return dict(schema_version=1, repository_url=source, title='Example game',
                source_analysis=[claim], screenshots=[], reconstructed_prompt='Build a game.',
                how_to_play=['Choose an action.'], mechanics=[claim], tags=['strategy'],
                rating={'grade': 'AA', 'rationale': 'A playable vertical slice.'},
                reviews=[{'fictional': True, 'rating': n, 'text': 'Illustrative review.'} for n in [3, 4, 5]],
                links=[source], limitations=['No screenshots inspected.'])


class SchemaTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.path = Path(self.temp.name) / 'readme.json'
        self.schema = load_schema()

    def tearDown(self):
        self.temp.cleanup()

    def check(self, value):
        self.path.write_text(json.dumps(value))
        return validate(self.path, self.schema)

    def test_valid(self):
        self.assertEqual(self.check(report()), [])

    def test_invalid_fields(self):
        for key, value in [('title', '  '), ('tags', []), ('schema_version', 2),
                           ('repository_url', 'javascript:alert(1)'), ('mechanics', []),
                           ('screenshots', [{'url': 'https://example.com/x.png', 'findings': 'Unseen'}])]:
            with self.subTest(key=key):
                data = report()
                data[key] = value
                self.assertTrue(self.check(data))
        data = report()
        del data['source_analysis']
        self.assertTrue(self.check(data))
        data = report()
        data['extra'] = True
        self.assertTrue(self.check(data))

    def test_reviews_and_grades(self):
        for count in [0, 2, 4]:
            data = report()
            data['reviews'] = [data['reviews'][0]] * count
            self.assertTrue(self.check(data))
        for rating in [-1, 6, True, '5']:
            data = report()
            data['reviews'][0]['rating'] = rating
            self.assertTrue(self.check(data))
        data = report()
        data['reviews'][0]['fictional'] = False
        self.assertTrue(self.check(data))
        data = report()
        data['rating']['grade'] = 'AA+'
        self.assertTrue(self.check(data))

    def test_bad_json_missing_file_symlink_and_cli(self):
        self.assertTrue(validate(self.path, self.schema))
        for content in ['not json', '{"title":"a","title":"b"}', '{"rating":NaN}', '```json\n{}\n```']:
            self.path.write_text(content)
            self.assertTrue(validate(self.path, self.schema))
        self.check(report())
        command = [sys.executable, str(runner.ROOT / 'scripts/validate_readme.py'), str(self.path)]
        self.assertEqual(subprocess.run(command, capture_output=True).returncode, 0)
        self.path.write_text('{}')
        self.assertEqual(subprocess.run(command, capture_output=True).returncode, 1)
        self.path.unlink()
        self.path.symlink_to(runner.SCHEMA)
        self.assertTrue(validate(self.path, self.schema))


class RunnerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='oc tests ')
        self.root = Path(self.temp.name)
        (self.root / 'scripts').mkdir()
        for name in ['test-oc.sh', 'test_oc.py', 'validate_readme.py']:
            shutil.copy2(runner.ROOT / 'scripts' / name, self.root / 'scripts' / name)
        shutil.copytree(runner.ROOT / 'schemas', self.root / 'schemas')
        (self.root / 'prompt.md').write_text('exact default prompt')
        self.release = self.root / 'release'
        self.fake = self.root / 'fake-oc'
        self.fake.write_text(f'''#!{sys.executable}
import json, pathlib, time, sys
assert pathlib.Path('.git').is_dir()
assert pathlib.Path('readme.schema.json').is_file()
deadline = time.monotonic() + 15
while not pathlib.Path({str(self.release)!r}).exists() and time.monotonic() < deadline:
    time.sleep(.05)
pathlib.Path('readme.json').write_text(json.dumps({report()!r}))
print(json.dumps({{"type":"step_finish"}}))
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
            '--server', self.base, '--executable', str(self.fake), *flags],
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

    def test_detached_default_three_urls_lock_validation_and_archive(self):
        completed = self.launch()
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertEqual(completed.stdout.count(' live]('), 3)
        self.assertFalse(self.unlocked())
        self.assertFalse(list(self.batch.glob('run-*/readme.json')))
        for path in (self.batch / 'records').glob('run-*/prompt.txt'):
            self.assertEqual(path.read_text(), 'exact default prompt')
        self.assertNotEqual(self.launch().returncode, 0)
        self.release.touch()
        self.wait_for(self.unlocked)
        self.assertTrue(all(r['status'] == 'passed' and r['validation']['valid'] for r in self.results()))
        self.assertFalse(list(self.batch.glob('summary.*')))
        original = (self.batch / 'run-001/readme.json').read_bytes()
        self.assertEqual(self.launch('--runs', '1').returncode, 0)
        self.wait_for(self.unlocked)
        self.assertEqual((self.root / 'work/oc-previous-batches/batch-001/run-001/readme.json').read_bytes(), original)

    def test_prompt_overrides_both_forms(self):
        prompt = self.root / 'custom prompt.md'
        prompt.write_text('custom exact prompt')
        self.release.touch()
        for flags in [('--prompt', str(prompt)), (f'--prompt={prompt}',)]:
            completed = self.launch('--runs', '1', *flags)
            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.wait_for(self.unlocked)
            self.assertEqual((self.batch / 'records/run-001/prompt.txt').read_text(), 'custom exact prompt')

    def test_timeout_aborts_session(self):
        self.assertEqual(self.launch('--runs', '1', '--timeout', '.2').returncode, 0)
        self.wait_for(self.unlocked)
        self.assertEqual(self.results()[0]['status'], 'timeout')
        self.assertTrue(any(p.endswith('/abort') for p in self.requests))
        self.assertFalse(self.results()[0]['validation']['valid'])

    def test_worker_signal_aborts_and_unlocks(self):
        self.assertEqual(self.launch('--runs', '1').returncode, 0)
        self.wait_for(lambda: self.results()[0]['status'] == 'running')
        os.kill(int((self.batch / 'worker.pid').read_text()), signal.SIGTERM)
        self.wait_for(self.unlocked)
        self.assertEqual(self.results()[0]['status'], 'interrupted')
        self.assertTrue(any(p.endswith('/abort') for p in self.requests))

    def test_missing_and_invalid_reports_fail(self):
        for content in ['', "import pathlib; pathlib.Path('readme.json').write_text('{}')"]:
            self.fake.write_text(f'#!{sys.executable}\n{content}\n')
            self.assertEqual(self.launch('--runs', '1').returncode, 0)
            self.wait_for(self.unlocked)
            self.assertEqual(self.results()[0]['status'], 'failed')
            self.assertFalse(self.results()[0]['validation']['valid'])

    def test_nonzero_exit_with_valid_report_still_fails(self):
        with self.fake.open('a') as script:
            script.write('sys.exit(7)\n')
        self.release.touch()
        self.assertEqual(self.launch('--runs', '1').returncode, 0)
        self.wait_for(self.unlocked)
        self.assertEqual(self.results()[0]['status'], 'failed')
        self.assertEqual(self.results()[0]['exit_code'], 7)
        self.assertTrue(self.results()[0]['validation']['valid'])

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

    def test_agent_schema_change_cannot_weaken_validation(self):
        self.fake.write_text(f'#!{sys.executable}\nimport pathlib\n'
                            "pathlib.Path('readme.schema.json').write_text('{}')\n"
                            "pathlib.Path('readme.json').write_text('{}')\n")
        self.assertEqual(self.launch('--runs', '1').returncode, 0)
        self.wait_for(self.unlocked)
        self.assertEqual(self.results()[0]['status'], 'failed')

    def test_five_concurrent_runs(self):
        completed = self.launch('--runs', '5')
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertEqual(completed.stdout.count(' live]('), 5)
        self.wait_for(lambda: all(r['status'] == 'running' for r in self.results()))
        self.release.touch()
        self.wait_for(self.unlocked)
        self.assertTrue(all(r['status'] == 'passed' for r in self.results()))

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
