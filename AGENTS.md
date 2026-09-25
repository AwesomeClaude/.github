# Astra-Top-Games instructions

## AgentsWeb runner testing

Connect over SSH to an existing AgentsWeb runner and verify it before writing or changing a runner workflow YAML. Reuse the verified tunnel format and key path.

## OpenCode smoke command

Run `opencode run -m opencode/muse-spark-1.3-contributor-free hi` to verify the Muse Spark 1.3 model.

## OpenCode test links

Copy every live OpenCode session URL printed by `scripts/test-oc.sh` immediately into a visible chat response as a clickable Markdown link. Return after launch; inspect per-run `result.json` only when asked for outcomes.

## Wiki index

- Read [OpenCode batch testing](wiki/oc-batch-testing.md) before changing the batch runner.

- Read [OpenCode event viewer](wiki/oc-event-viewer.md) to launch and verify the local log dashboard.
