#!/usr/bin/env python3
"""Read-only OpenCode JSONL viewer; no third-party dependencies."""
import argparse
import json
import os
from pathlib import Path
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse


class Catalog:
    def __init__(self, root):
        self.root = Path(root).resolve()
        self.cache = {}
        self.lock = threading.Lock()

    def scan(self):
        found = {}
        for directory, dirs, files in os.walk(self.root, followlinks=False):
            dirs[:] = [d for d in dirs if not Path(directory, d).is_symlink()]
            if 'events.jsonl' in files:
                path = Path(directory, 'events.jsonl')
                if not path.is_symlink():
                    found[path.relative_to(self.root).as_posix()] = path
        result = []
        for name, path in found.items():
            try:
                st = path.stat()
                signature = (st.st_ino, st.st_size, st.st_mtime_ns)
                cached = self.cache.get(name)
                if cached and cached['signature'] == signature:
                    result.append(cached)
                    continue
                events, invalid, pending = [], 0, False
                with path.open('rb') as source:
                    for line in source:
                        if not line.strip():
                            continue
                        try:
                            event = json.loads(line)
                            if not isinstance(event, dict):
                                raise ValueError('Expected an object')
                            events.append(event)
                        except (ValueError, UnicodeDecodeError):
                            if line.endswith(b'\n'):
                                invalid += 1
                            else:
                                pending = True
                parts = {}
                for i, e in enumerate(events):
                    p = e.get('part')
                    p = p if isinstance(p, dict) else {}
                    parts[(e.get('sessionID'), p.get('id', i))] = (e, p)
                tokens = cost = messages = tools = errors = 0
                for e, p in parts.values():
                    t = e.get('type')
                    messages += t == 'text'
                    tools += t == 'tool_use'
                    state = p.get('state') or {}
                    errors += t == 'error' or (isinstance(state, dict) and state.get('status') == 'error')
                    if t == 'step_finish':
                        usage = p.get('tokens') or {}
                        if isinstance(usage, dict):
                            value = usage.get('total')
                            if value is None:
                                value = sum(usage.get(k, 0) or 0 for k in ('input', 'output', 'reasoning'))
                                value += sum((usage.get('cache') or {}).values())
                            tokens += value
                        cost += p.get('cost', 0) or 0
                item = dict(path=name, signature=signature, modified=st.st_mtime,
                            events=events, count=len(events), messages=messages,
                            tools=tools, errors=errors, tokens=tokens, cost=cost,
                            invalid=invalid, pending=pending)
                self.cache[name] = item
                result.append(item)
            except (OSError, TypeError, ValueError):
                continue
        self.cache = {r['path']: r for r in result}
        return sorted(result, key=lambda r: r['modified'], reverse=True)


def make_handler(catalog):
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            url = urlparse(self.path)
            if url.path == '/':
                data = Path(__file__).with_name('index.html').read_bytes()
                mime = 'text/html; charset=utf-8'
            elif url.path in ('/api/runs', '/api/run'):
                with catalog.lock:
                    runs = catalog.scan()
                    if url.path == '/api/runs':
                        body = dict(root=str(catalog.root), runs=[{k: v for k, v in r.items() if k not in ('events', 'signature')} for r in runs])
                    else:
                        name = parse_qs(url.query).get('path', [''])[0]
                        body = next((r for r in runs if r['path'] == name), None)
                        if body is None:
                            self.send_error(404)
                            return
                data = json.dumps(body).encode()
                mime = 'application/json'
            else:
                self.send_error(404)
                return
            self.send_response(200)
            self.send_header('Content-Type', mime)
            self.send_header('Cache-Control', 'no-store')
            self.send_header('Content-Length', str(len(data)))
            self.send_header('Content-Security-Policy', "default-src 'self'; script-src 'unsafe-inline'; style-src 'unsafe-inline'; connect-src 'self'; base-uri 'none'; frame-ancestors 'none'")
            self.end_headers()
            self.wfile.write(data)

        def log_message(self, *args):
            pass
    return Handler


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', default=os.getcwd(), help='Directory to scan (default: launch directory)')
    parser.add_argument('--port', type=int, default=8765)
    args = parser.parse_args()
    if not Path(args.root).is_dir():
        parser.error('--root must be a directory')
    server = ThreadingHTTPServer(('127.0.0.1', args.port), make_handler(Catalog(args.root)))
    print(f'OpenCode viewer: http://127.0.0.1:{server.server_port} — root: {Path(args.root).resolve()}', flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
