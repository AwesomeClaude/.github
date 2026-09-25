# Launch OpenCode batches

Run `./scripts/test-oc.sh --repo https://github.com/owner/repository` from any directory. Pass a `/tree/branch` URL to target a branch. Replace every `{{repository_url}}` token in the repository's `prompt.md` with the supplied URL; pass `--prompt /absolute/path/to/prompt.md` to override the template. Set concurrency with `--runs 3`, the per-run deadline with `--timeout 900`, and the model with `--model provider/model`. Keep Muse Spark as the default model.

Wait only for session creation and the detached worker's startup acknowledgement. Read each printed session link immediately. Treat launcher exit 0 as successful launch, not successful analysis. Inspect per-run results after launch. Keep the worker alive after closing the terminal; refuse another batch while its lock is held.

Use `--server http://127.0.0.1:4096` to attach to a server, or start/reuse the loopback server on `--port 4096`. Keep the server available for session inspection. Inspect `work/oc-server/server.json` and `server.log` for a managed server. Supply `--web-base https://your-protected-tunnel.example` only for an existing protected tunnel. Set `OPENCODE_SERVER_PASSWORD` and optionally `OPENCODE_SERVER_USERNAME` for server authentication.

## Inspect outputs

Use this layout:

```text
work/
  oc-batch-test/
    run-001/
      .git/
      readme.json
    records/
      run-001/
        prompt.txt
        command.json
        events.jsonl
        stderr.log
        result.json
    worker.pid
    worker.log
  oc-previous-batches/
    batch-NNN/
  oc-server/
```

Read `result.json` for the session link, state, and exit code. Treat `finished` as a successful OpenCode process, not a review of its output. Ask Codex to use `$review-oc-reports` to read `readme.json` directly, compare it with the example in `prompt.md`, and assess claims and screenshots manually. Preserve the exact prompt and its SHA-256. Keep diagnostic logs outside agent workspaces. Treat per-run Git repositories as discovery boundaries, not filesystem sandboxes.

## Preserve history and stop runs

Move the completed current batch into `work/oc-previous-batches/batch-NNN` before launching another. Increment the highest existing number; preserve every archived file. Refuse symlink batch/archive paths. Treat archived session links as historical: inspect archived files directly instead of resuming against reused directories.

Inspect the PID in `worker.pid` and confirm it still belongs to this batch before sending SIGTERM. Abort attached server sessions and stop CLI process groups on worker termination or per-run timeout. Leave the server running. Inspect `worker.log` if startup acknowledgement fails.

## Test changes

Run `python3 -m unittest discover -s scripts -p test_oc_runner.py -v`. Exercise prompt overrides, detached execution, live URLs, lock ownership, archive preservation, startup failure, timeout, and termination against fake local sessions.
