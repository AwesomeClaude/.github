# Astra-Top-Games instructions

## AgentsWeb runner testing

For SSH requests here, use the live AgentsWeb Actions runner and `~/.ssh/aiplay-agentsweb`; use `a2` only if named. Verify SSH before editing runner YAML.

## Issue catalog workflow

Open a real test issue automatically after changing the issue catalog workflow. Publish the review PR or branch fallback and the issue report, including branch README links for added games, before the owner-only 30-minute SSH hold. Keep the same worker and tunnel alive during the hold, including after analysis or publication failure. Skip the hold for non-owner issues. Report PR and issue-comment links as soon as they appear; do not wait for the hold to end.

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
