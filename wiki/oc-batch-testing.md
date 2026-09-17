# Run OpenCode batch tests

Run `./scripts/test-oc.sh` from the project to launch three runs concurrently using the canonical `prompt.md`. Use `--runs 10` to launch all ten runs concurrently. Supply `--prompt /absolute/path/to/prompt.md` only when intentionally using a different prompt. Keep the default Muse Spark model or supply `--model provider/model`. Set the per-run deadline with `--timeout 900`.

Use `--server http://127.0.0.1:4096` to attach to an existing local server. Otherwise let the runner start or reuse a loopback server on `--port 4096`. Keep that server running after completion to inspect sessions. Inspect `work/oc-server/server.json` and `server.log` for a server started by this script. Supply `--web-base https://your-protected-tunnel.example` only for an existing tunnel; create and protect that tunnel separately. Set `OPENCODE_SERVER_PASSWORD` and optionally `OPENCODE_SERVER_USERNAME` when using server authentication.

## Preserve batches

Expect the next invocation to move `work/oc-batch-test` into `work/oc-previous-batches/batch-NNN`, using the highest existing number plus one. Preserve every archived file. Keep existing legacy `work/oc-generations` untouched. Refuse simultaneous batch invocations and symlink archive paths. Leave original analyses and published reports untouched.

Inspect this layout:

```text
work/
  oc-batch-test/
    run-001/.git/
    run-002/.git/
    run-003/.git/
    records/run-001/
      prompt.txt
      command.json
      events.jsonl
      stderr.log
      result.json
    summary.json
    summary.md
  oc-previous-batches/
    batch-001/
  oc-server/
```

Initialize each run as its own Git repository before creating the session. Launch all requested runs concurrently; default to three runs. Preserve the prompt unchanged and record its SHA-256. Keep the runner's logs outside agent workspaces. Treat Git boundaries as repository-discovery isolation, not a filesystem sandbox; use an OS/container sandbox for untrusted workloads. Expect `--auto` permission behavior; do not assume it prevents access to neighboring files or baseline reports.

## Inspect live progress

Open each printed session URL immediately after session creation. Inspect session IDs, original directories, and URLs in per-run metadata and both rolling summaries. Use the same base64url-directory/session-ID URL format as OhMyGithub. Treat archived links as historical references: moving a directory does not migrate the session's recorded workspace. Inspect archived reports/logs directly; do not resume an archived session against a reused current-batch directory.

Press Ctrl-C to stop scheduling, abort this batch's active server sessions, and terminate their CLI process groups. Apply the same cleanup on per-run timeout. Leave the web server available for inspection.

## Validate results

Separate `report_generated`, `structural_pass`, and `quality_pass`. Require human review for factual accuracy, implemented-versus-planned distinctions, screenshot inspection, and comparison quality. Read image-related tool calls as evidence candidates, not proof of visual understanding. Inspect tool errors even when OpenCode exits zero. Expect exit 1 for failed runs or reports that fail structural checks, and exit 130 for interruption.

Run `python3 -m unittest discover -s scripts -p test_oc_runner.py -v` to test numbering, archive preservation, symlink refusal, live URL encoding, three parallel Git workspaces, timeout abort, and missing-report validation.
