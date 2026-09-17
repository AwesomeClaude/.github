import json
from pathlib import Path
import tempfile
import threading
import unittest
from urllib.request import urlopen
from urllib.error import HTTPError
from http.server import ThreadingHTTPServer
from server import Catalog, make_handler


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.path = self.root / 'nested' / 'events.jsonl'
        self.path.parent.mkdir()
        self.catalog = Catalog(self.root)

    def tearDown(self):
        self.tmp.cleanup()

    def test_discovery_append_partial_rotation_deletion(self):
        self.path.write_text('{"type":"text","part":{"text":"Hello"}}\n{"type":')
        r = self.catalog.scan()[0]
        self.assertEqual((r['count'], r['pending'], r['invalid']), (1, True, 0))
        with self.path.open('a') as f:
            f.write('"step_start"}\ninvalid\n[]\n')
        r = self.catalog.scan()[0]
        self.assertEqual((r['count'], r['pending'], r['invalid']), (2, False, 2))
        self.path.write_text('{"type":"error"}')
        self.assertEqual(self.catalog.scan()[0]['errors'], 1)
        second = self.root / 'new' / 'events.jsonl'
        second.parent.mkdir()
        second.write_text('')
        self.assertEqual(len(self.catalog.scan()), 2)
        self.path.unlink()
        self.assertEqual(len(self.catalog.scan()), 1)

    def test_usage_deduplication_and_symlinks(self):
        event = dict(type='step_finish', part=dict(id='p1', tokens=dict(total=123), cost=.1))
        self.path.write_text((json.dumps(event)+'\n')*2)
        (self.root/'linked').symlink_to(self.path.parent, target_is_directory=True)
        runs = self.catalog.scan()
        self.assertEqual(len(runs), 1)
        self.assertEqual((runs[0]['count'], runs[0]['tokens'], runs[0]['cost']), (2,123,.1))

    def test_http_and_path_confinement(self):
        self.path.write_text('{"type":"text"}\n')
        server = ThreadingHTTPServer(('127.0.0.1', 0), make_handler(self.catalog))
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        base = f'http://127.0.0.1:{server.server_port}'
        try:
            with urlopen(base+'/api/runs') as r:
                self.assertEqual(json.load(r)['runs'][0]['path'], 'nested/events.jsonl')
            with urlopen(base+'/api/run?path=nested/events.jsonl') as r:
                self.assertEqual(json.load(r)['count'], 1)
            with self.assertRaises(HTTPError) as error:
                urlopen(base+'/api/run?path=../../etc/passwd')
            self.assertEqual(error.exception.code, 404)
            with urlopen(base) as r:
                self.assertIn(b'Run Observatory', r.read())
        finally:
            server.shutdown()
            server.server_close()
            thread.join()


if __name__ == '__main__':
    unittest.main()
