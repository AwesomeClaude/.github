# Astra-Top-Games instructions

## AgentsWeb runner testing

Treat an unqualified request to connect to SSH in this repository as a request for the current AgentsWeb GitHub Actions runner. Locate its live run and connect through its published tunnel endpoint with `~/.ssh/aiplay-agentsweb`; verify `hostname`, `id -un`, and `pwd`. If no runner is live, ask whether to start a new five-hour run. Use `a2` only when the user explicitly names it.

Connect over SSH to an existing AgentsWeb runner and verify it before writing or changing a runner workflow YAML. Reuse the verified tunnel format and key path.

## OpenCode smoke command

Run `opencode run -m opencode/muse-spark-1.3-contributor-free hi` to verify the Muse Spark 1.3 model.

## OpenCode source

Use the local OpenCode source checkout at `../ChatGPT/opencode`. Refer to [the upstream repository](https://github.com/anomalyco/opencode) for its GitHub page.

## OpenCode test links

Copy every live OpenCode session URL printed by `scripts/test-oc.sh` immediately into a visible chat response as a clickable Markdown link. Include every run link again in the final response. Return after launch; inspect per-run `result.json` only when asked for outcomes.

## Wiki index

- Read [OpenCode batch testing](wiki/oc-batch-testing.md) before changing the batch runner.

## Verification

- Don't write or run unit tests, mock tests, or static analysis.
- Don't use mockups instead of a real end-to-end run.
- Don't ask the user to test or analyze; do it directly.
- Don't finish without running and analyzing the end-to-end flow.
