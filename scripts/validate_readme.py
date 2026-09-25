#!/usr/bin/env python3
"""Validate one game readme against its JSON Schema."""
import argparse
import json
from pathlib import Path
import sys

try:
    from jsonschema import Draft202012Validator, FormatChecker
except ImportError:
    raise SystemExit('Install dependencies: python3 -m pip install -r scripts/requirements-test-oc.txt')

SCHEMA = Path(__file__).resolve().parent.parent / 'schemas' / 'readme.schema.json'


def load_schema(path=SCHEMA):
    schema = json.loads(Path(path).read_text(encoding='utf-8'))
    Draft202012Validator.check_schema(schema)
    return schema


def unique_object(pairs):
    value = {}
    for key, item in pairs:
        if key in value:
            raise ValueError(f'Duplicate key: {key}')
        value[key] = item
    return value


def reject_constant(value):
    raise ValueError(f'Invalid JSON constant: {value}')


def validate(path, schema=None):
    path = Path(path)
    try:
        if path.is_symlink() or not path.is_file():
            raise ValueError('Require a regular readme.json file, not a symlink')
        value = json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=unique_object,
                           parse_constant=reject_constant)
        validator = Draft202012Validator(schema if schema is not None else load_schema(),
                                        format_checker=FormatChecker())
        errors = []
        for error in validator.iter_errors(value):
            location = '$' + ''.join(f'[{p}]' if isinstance(p, int) else f'.{p}'
                                    for p in error.absolute_path)
            errors.append(f'{location}: {error.message}')
        return sorted(errors)
    except (OSError, ValueError) as exc:
        return [f'$: {exc}']


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('report', type=Path)
    args = parser.parse_args()
    errors = validate(args.report)
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print(f'Valid: {args.report}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
