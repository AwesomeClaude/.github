# Launch game analyses

Install dependencies with `python3 -m pip install -r scripts/requirements-test-oc.txt`.
Run `./scripts/test-oc.sh` to print three OpenCode session links and return while analysis continues in the background.

Edit `prompt.md` to change the request. Require each run to write `readme.json` matching `schemas/readme.schema.json`.
Validate a report with `python3 scripts/validate_readme.py /absolute/path/to/readme.json`.

Read [batch instructions](wiki/oc-batch-testing.md) for lifecycle and result paths. Open the [event viewer](wiki/oc-event-viewer.md) to inspect logs.
