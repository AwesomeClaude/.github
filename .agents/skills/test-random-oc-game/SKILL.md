---
name: test-random-oc-game
description: Launch scripts/test-oc.sh for one random GitHub game from the local games.json catalog.
---

# Test a random catalog game

Work from `/Users/igor/Documents/https-github-com-phirogue-sparkygames-https`. Read `/Users/igor/Documents/Codex/2026-09-08/find-games-last-week-made-with/games.json`; stop if it is missing or has no eligible GitHub URLs. Select one distinct `github_url` at random, without favoring duplicate entries:

```sh
set -eu
repo=$(python3 - <<'PY'
import json, re, secrets
from pathlib import Path

source = Path('/Users/igor/Documents/Codex/2026-09-08/find-games-last-week-made-with/games.json')
entries = json.loads(source.read_text(encoding='utf-8'))
pattern = re.compile(r'https://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+(?:/tree/[A-Za-z0-9_./-]+)?/?')
urls = sorted({item['github_url'].rstrip('/') for item in entries
               if isinstance(item, dict) and isinstance(item.get('github_url'), str)
               and pattern.fullmatch(item['github_url'])})
if not urls:
    raise SystemExit('No eligible GitHub game URLs in games.json')
print(secrets.choice(urls))
PY
)
printf 'Selected game: %s\n' "$repo"
./scripts/test-oc.sh --repo "$repo" --port 4098
```

Check that the local OpenCode server on port 4098 is healthy and matches the installed OpenCode version before launching. If it does not, choose a free loopback port and replace `4098` in the command. If the launcher fails, report the failure; do not select a different game automatically.

Copy every printed live session URL immediately into a visible chat response as a clickable Markdown link. Include all run links again in the final response. Return after launch; inspect per-run results only when asked for outcomes. Do not change the catalog or run `games.sh`.
