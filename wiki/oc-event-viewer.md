# Inspect OpenCode event logs

Run `./scripts/oc-viewer.sh` from the directory to scan. Invoke the launcher by absolute path when scanning another directory. Open `http://127.0.0.1:8765`.

Pass `--root /path/to/runs` to override the launch directory. Pass `--port 8766` to select another port. Install Python 3 before launching; install no additional packages.

Find every `events.jsonl` beneath the root, including hidden directories. Ignore symlink files and directories. Filter by relative path and click a run to inspect text, tool inputs and outputs, step results, or raw events.

Allow two seconds plus scan time for refreshes. Interpret “Recent activity” as a file modification within 30 seconds, not proof of a running process. Read token totals as summed step usage, including repeated context, not unique conversation tokens. Inspect cost in step cards. Expect user prompts to be absent from CLI output; do not invent missing messages.

Expand source events to inspect original JSON. Disable Follow or scroll away from the bottom to retain your reading position. Expect plain-text rendering of message content, including Markdown source.

Treat the viewer as local and read-only. Keep the loopback binding. Expect malformed complete lines to be counted and skipped; allow incomplete final lines to finish. Expect changed files to be reparsed and selected runs to be transferred in full; use narrower roots for very large trees or logs.

Run `python3 -m unittest discover -s scripts/oc-viewer -v` to check discovery, appends, partial lines, truncation, deletion, token deduplication, symlink exclusion, HTTP responses, and path confinement.
