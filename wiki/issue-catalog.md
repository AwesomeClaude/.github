# Publish issue game links

Post the banner and “I’m on it. Analyzing the links may take 10–30 minutes.” as the first job step. Link to the current attempt’s analysis job; use the run URL if job lookup fails. Pin the banner URL to the workflow commit. Keep the issue body unchanged.

Put every qualifying game in the root catalog and screenshot gallery. Treat `repository_url` as optional; normalize an omitted, null, or empty value to null. Require an original `source_url`; reuse the repository URL for existing repository-only reports. Verify every supplied source repository. Preserve existing game directories and original-link-derived directories. Use one validation and publication path for all added games.

Fetch the latest default branch before applying report artifacts. Create a catalog PR and request a squash auto-merge with an exact head-commit match. Enable repository auto-merge. Set repository variable `ISSUE_CATALOG_AUTO_MERGE=false` to leave new catalog PRs open. Respect required checks and reviews. Leave partial or failed analyses open. Report merge failures on the issue and fail the publication step. Keep published branches available for the game README links.

Publish the final report before uploading diagnostics and starting the owner-only 30-minute hold. Keep the worker and SSH tunnel alive through that hold, including on failure. Preserve the configured Chat-ID in generated and squash commit messages as the automation’s implementation provenance.

## Verify the live flow

Verify SSH on a live AgentsWeb runner before editing workflow YAML. Deploy the workflow to the default branch. Open an owner-authored test issue with a real source-backed game and a real game without verified source. Inspect the startup comment, banner response, and job link. SSH into the issue worker during analysis; inspect OpenCode records, logs, and processes. Inspect the final reports and combined catalog. Confirm the catalog PR merges automatically and its issue links resolve. Report the PR and comment URLs immediately. Return while the same worker remains in its 30-minute hold.

Keep credentials out of the analysis step. Use the workflow token only for the acknowledgment and publication steps. Account for GitHub runner queue time before the first comment; treat the 10–30-minute estimate as guidance, not a deadline.

## Reuse the live regression evidence

Use [issue #12](https://github.com/agents-dev/Astra-Top-Games/issues/12) and [Actions job 108524405448](https://github.com/agents-dev/Astra-Top-Games/actions/runs/36285154991/job/108524405448) as the first production E2E record. Inspect its [startup comment](https://github.com/agents-dev/Astra-Top-Games/issues/12#issuecomment-5851568458) for the rendered banner, 10–30-minute estimate, and direct job link. Inspect the [final comment](https://github.com/agents-dev/Astra-Top-Games/issues/12#issuecomment-5851587711) and merged [catalog PR #13](https://github.com/agents-dev/Astra-Top-Games/pull/13) for publication and automatic merge.

Compare [2048](https://github.com/agents-dev/Astra-Top-Games/blob/main/games/gabrielecirulli--2048/README.md) and [Infinite Craft](https://github.com/agents-dev/Astra-Top-Games/blob/main/games/no-source/neal-fun--be5898efdb64/README.md) in the same root ranking and screenshot gallery. Check the latter's explicit no-verified-source label. Note that both OpenCode processes exited 0 with empty stderr after roughly 128 and 149 seconds. Confirm the observed worker, OpenCode server, and AgentsWeb SSH tunnel remained alive when `sleep 1800` began at 01:22 UTC on 2026-09-27; do not wait for the hold to finish. Treat OpenCode analysis time, not publication, as the observed throughput bottleneck. Do not treat this single production run as proof that future external pages remain accessible.
