#!/bin/sh
set -eu

# Reanalyze supplied links; rebuild the catalog when no links are supplied.

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
exec python3 "$script_dir/games.py" "$@"
