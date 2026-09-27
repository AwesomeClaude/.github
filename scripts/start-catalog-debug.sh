#!/bin/bash
set -euo pipefail
port="${1:-4096}"
runtime="$PWD/work/catalog-debug"
mkdir -p "$runtime"
if ! command -v cloudflared >/dev/null; then
  curl -fsSL --connect-timeout 10 --max-time 45 https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -o "$runtime/cloudflared"
  chmod +x "$runtime/cloudflared"
  binary="$runtime/cloudflared"
else
  binary="$(command -v cloudflared)"
fi
nohup "$binary" tunnel --url "http://127.0.0.1:$port" --no-autoupdate > "$runtime/tunnel.log" 2>&1 < /dev/null &
pid=$!
echo "$pid" > "$runtime/tunnel.pid"
for ((i=0; i<45; i++)); do
  url=$(grep -Eo 'https://[a-z0-9-]+\.trycloudflare\.com' "$runtime/tunnel.log" | head -1 || true)
  if [[ -n "$url" ]]; then
    echo "$url"
    exit 0
  fi
  kill -0 "$pid" 2>/dev/null || break
  sleep 1
done
kill "$pid" 2>/dev/null || true
exit 1
