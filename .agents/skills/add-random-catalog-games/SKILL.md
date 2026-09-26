---
name: add-random-catalog-games
description: Add a requested number of random, not-yet-cataloged GitHub games from the local games.json source to the production game catalog.
---

# Add random catalog games

Work from `/Users/igor/Documents/https-github-com-phirogue-sparkygames-https`. Read `/Users/igor/Documents/Codex/2026-09-08/find-games-last-week-made-with/games.json`. Use the user's requested count, or 10 if none is given. Select distinct eligible GitHub game destinations uniformly without replacement. Exclude destinations that already have `readme.json` in the catalog. Stop if the source is missing or fewer than the requested count are available; do not silently reduce the count.

Create a temporary URL list and pass it to the production catalog runner. Set `count` from the request before running:

```sh
set -eu
count=10
selection=$(mktemp)
trap 'rm -f "$selection"' EXIT
python3 - "$count" > "$selection" <<'PY'
import json, random, sys
from pathlib import Path

root = Path.cwd()
sys.path.insert(0, str(root / 'scripts'))
from games import game_url

source = Path('/Users/igor/Documents/Codex/2026-09-08/find-games-last-week-made-with/games.json')
entries = json.loads(source.read_text(encoding='utf-8'))
eligible = {}
for item in entries:
    if not isinstance(item, dict) or not isinstance(item.get('github_url'), str):
        continue
    try:
        url, destination = game_url(item['github_url'])
    except ValueError:
        continue
    if not (destination / 'readme.json').exists():
        eligible.setdefault(destination, url)
count = int(sys.argv[1])
if count < 1 or len(eligible) < count:
    raise SystemExit(f'Need {count} eligible new games; found {len(eligible)}')
for url in random.SystemRandom().sample(list(eligible.values()), count):
    print(url)
PY
printf 'Selected games:\n'
cat "$selection"
./scripts/games.sh --file "$selection"
```

Copy every live OpenCode session URL printed by the runner immediately into a visible response as a clickable Markdown link. After the run, inspect the catalog additions and `work/game-batches/` results. Report how many of the selected games were actually added and why any were skipped. Do not automatically select replacement games after failures. Commit the generated catalog pages, index, and ledger with the change; keep unrelated work out of the commit.
