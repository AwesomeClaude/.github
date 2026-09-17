#!/bin/sh
set -eu

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
prompt_file=$(CDPATH= cd -- "$script_dir/.." && pwd)/prompt.md

use_default=true
for argument in "$@"; do
    case "$argument" in
        --prompt|--prompt=*) use_default=false ;;
    esac
done

if "$use_default"; then
    set -- --prompt "$prompt_file" "$@"
fi

exec python3 "$script_dir/test_oc.py" "$@"
