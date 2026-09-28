"""Archive public screenshot bytes without credentials or private-network access."""

from datetime import datetime, timezone
import hashlib
import ipaddress
from pathlib import Path
import re
import socket
import subprocess
import tempfile
from urllib.parse import urljoin, urlsplit
import warnings

from PIL import Image

MAX_BYTES = 8 * 1024 * 1024
Image.MAX_IMAGE_PIXELS = 25_000_000
FORMATS = {'PNG': '.png', 'JPEG': '.jpg', 'WEBP': '.webp', 'GIF': '.gif'}
LOCAL_PATH = re.compile(r'screenshots/[a-f0-9]{64}\.(?:png|jpg|webp|gif)\Z')


def local_path(directory, shot):
    name = shot.get('local_path', '')
    if not isinstance(name, str) or not LOCAL_PATH.fullmatch(name):
        return None
    path = directory / name
    if path.resolve().parent != (directory / 'screenshots').absolute() or not path.is_file():
        return None
    if path.stat().st_size > MAX_BYTES:
        return None
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    return name if digest == shot.get('sha256') == path.stem else None


def download(url, target):
    """Pin each connection to a validated public IP, including all redirects."""
    for _ in range(6):
        parsed = urlsplit(url)
        host = parsed.hostname
        if (parsed.scheme not in ('http', 'https') or not host or parsed.username
                or parsed.password or parsed.port not in (None, 80, 443)):
            raise ValueError('Require a public HTTP(S) image URL without credentials')
        port = parsed.port or (443 if parsed.scheme == 'https' else 80)
        addresses = list(dict.fromkeys(row[4][0] for row in socket.getaddrinfo(
            host, port, type=socket.SOCK_STREAM)))
        if not addresses or any(not ipaddress.ip_address(ip).is_global for ip in addresses):
            raise ValueError('Reject private or non-global screenshot destination')
        ip = addresses[0]
        address = f'[{ip}]' if ':' in ip else ip
        headers = target.with_suffix('.headers')
        result = subprocess.run([
            'curl', '-q', '--silent', '--show-error', '--noproxy', '*',
            '--proto', '=http,https', '--max-time', '20', '--connect-timeout', '8',
            '--max-filesize', str(MAX_BYTES), '--resolve', f'{host}:{port}:{address}',
            '--user-agent', 'AwesomeClaude-screenshot-archive', '--dump-header', str(headers),
            '--output', str(target), '--write-out', '%{http_code}', '--url', url,
        ], capture_output=True, text=True, timeout=25)
        if result.returncode:
            raise ValueError(f'Image transfer failed (curl {result.returncode})')
        status = int(result.stdout)
        if status in (301, 302, 303, 307, 308):
            locations = re.findall(r'^location:\s*(.*?)\s*$', headers.read_text(), re.I | re.M)
            if not locations:
                raise ValueError('Image redirect has no location')
            url = urljoin(url, locations[-1])
            continue
        if status != 200:
            raise ValueError(f'Image source returned HTTP {status}')
        if target.stat().st_size > MAX_BYTES:
            raise ValueError('Image exceeds the 8 MiB limit')
        with warnings.catch_warnings():
            warnings.simplefilter('error', Image.DecompressionBombWarning)
            with Image.open(target) as picture:
                extension = FORMATS.get(picture.format)
                if not extension or picture.width * picture.height > Image.MAX_IMAGE_PIXELS:
                    raise ValueError('Unsupported image format or dimensions')
                picture.verify()
            # Decode the displayed frame as well as checking the container.
            with Image.open(target) as picture:
                picture.load()
        return extension
    raise ValueError('Too many image redirects')


def archive(directory, data, retry=False):
    """Keep original URLs; render only validated, content-addressed local copies."""
    for shot in data['screenshots']:
        if local_path(directory, shot):
            shot.pop('download_error', None)
            continue
        for key in ('local_path', 'sha256', 'downloaded_at'):
            shot.pop(key, None)
        if shot.get('download_error') and not retry:
            continue
        try:
            with tempfile.TemporaryDirectory(prefix='catalog-image-') as temp:
                source = Path(temp) / 'image'
                extension = download(shot.get('archive_url', shot['url']), source)
                digest = hashlib.sha256(source.read_bytes()).hexdigest()
                name = f'screenshots/{digest}{extension}'
                destination = directory / name
                destination.parent.mkdir(parents=True, exist_ok=True)
                if destination.parent.resolve() != destination.parent.absolute():
                    raise ValueError('Reject symlinked screenshot directory')
                destination.write_bytes(source.read_bytes())
            shot.update(local_path=name, sha256=digest,
                        downloaded_at=datetime.now(timezone.utc).isoformat())
            shot.pop('download_error', None)
        except (OSError, ValueError, subprocess.SubprocessError, SyntaxError,
                Image.DecompressionBombError, Image.DecompressionBombWarning) as exc:
            shot['download_error'] = str(exc)[:240]
            print(f'Screenshot unavailable: {data["title"]}: {shot["url"]}: {exc}', flush=True)
    return data
