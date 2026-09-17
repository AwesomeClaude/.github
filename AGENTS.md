# Astra-Top-Games instructions

## AgentsWeb runner testing

Connect over SSH to an existing AgentsWeb runner and verify it before writing or changing a runner workflow YAML. Reuse the verified tunnel format and key path.

## OpenCode smoke command

Run `opencode run -m opencode/muse-spark-1.3-contributor-free hi` to verify the Muse Spark 1.3 model.

## OpenCode test links

When running `scripts/test-oc.sh`, immediately copy every live OpenCode session URL printed by the runner into a visible chat response as a clickable Markdown link. Do not wait for the batch to finish. Continue reporting later URLs as they appear, and include the final batch summary link after completion.

## Wiki index

- Read [OpenCode batch testing](wiki/oc-batch-testing.md) before changing the batch runner.
