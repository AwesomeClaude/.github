#!/bin/sh
set -eu

# Reanalyze links; archive screenshots and rebuild the catalog without links.
# Install scripts/requirements-catalog.txt first; retry missing images with --retry-screenshots.
# Also refresh the compact submit-game button in the root and profile READMEs.

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
exec python3 "$script_dir/games.py" "$@"
