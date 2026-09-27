# Publish issue game links

Post the banner and “I’m on it. Analyzing the links may take 10–30 minutes.” as the first job step. Link to the current attempt’s analysis job; use the run URL if job lookup fails. Pin the banner URL to the workflow commit. Keep the issue body unchanged.

Put every qualifying game in the root catalog and screenshot gallery. Treat `repository_url` as optional; normalize an omitted, null, or empty value to null. Require an original `source_url`; reuse the repository URL for existing repository-only reports. Verify every supplied source repository. Preserve existing game directories and original-link-derived directories. Always reanalyze submitted games. Use one validation and publication path for additions and refreshes.

Fetch the latest default branch before applying report artifacts. Create a catalog PR and request a squash auto-merge with an exact head-commit match. Enable repository auto-merge. Set repository variable `ISSUE_CATALOG_AUTO_MERGE=false` to leave new catalog PRs open. Respect required checks and reviews. Leave partial or failed analyses open. Report merge failures on the issue and fail the publication step. Keep published branches available for the game README links.

Publish the final report before uploading diagnostics and starting the owner-only 30-minute hold. Keep the worker and SSH tunnel alive through that hold, including on failure. Preserve the configured Chat-ID in generated and squash commit messages as the automation’s implementation provenance.

## Verify the live flow

Verify SSH on a live AgentsWeb runner before editing workflow YAML. Deploy the workflow to the default branch. Open an owner-authored test issue with a real source-backed game and a real game without verified source. Inspect the startup comment, banner response, and job link. SSH into the issue worker during analysis; inspect OpenCode records, logs, and processes. Inspect the final reports and combined catalog. Confirm the catalog PR merges automatically and its issue links resolve. Report the PR and comment URLs immediately. Return while the same worker remains in its 30-minute hold.

Keep credentials out of the analysis step. Use the workflow token only for the acknowledgment and publication steps. Account for GitHub runner queue time before the first comment; treat the 10–30-minute estimate as guidance, not a deadline.

## Reuse the live regression evidence

Use [issue #12](https://github.com/agents-dev/Astra-Top-Games/issues/12) and [Actions job 108524405448](https://github.com/agents-dev/Astra-Top-Games/actions/runs/36285154991/job/108524405448) as the first production E2E record. Inspect its [startup comment](https://github.com/agents-dev/Astra-Top-Games/issues/12#issuecomment-5851568458) for the rendered banner, 10–30-minute estimate, and direct job link. Inspect the [final comment](https://github.com/agents-dev/Astra-Top-Games/issues/12#issuecomment-5851587711) and merged [catalog PR #13](https://github.com/agents-dev/Astra-Top-Games/pull/13) for publication and automatic merge.

Compare [2048](https://github.com/agents-dev/Astra-Top-Games/blob/main/games/gabrielecirulli--2048/README.md) and [Infinite Craft](https://github.com/agents-dev/Astra-Top-Games/blob/main/games/no-source/neal-fun--be5898efdb64/README.md) in the same root ranking and screenshot gallery. Check the latter's explicit no-verified-source label. Note that both OpenCode processes exited 0 with empty stderr after roughly 128 and 149 seconds. Confirm the observed worker, OpenCode server, and AgentsWeb SSH tunnel remained alive when `sleep 1800` began at 01:22 UTC on 2026-09-27; do not wait for the hold to finish. Treat OpenCode analysis time, not publication, as the observed throughput bottleneck. Do not treat this single production run as proof that future external pages remain accessible.

## Refresh reports and retain evidence

Use `prompt.md` for every analysis instruction. Use `games.py` for shared session execution, report validation, identity resolution, history, and generation. Use `issue_catalog.py` only for issue input, debug lifecycle, and GitHub publication; invoke its separate phases from Actions.

Ask OpenCode to inspect the catalog and reuse an existing `catalog_slug` for the same game. Match concrete repository paths and play URLs again against the latest catalog during publication. Preserve labeled historical links; add source, play, and submission links; deduplicate by URL. Record documented creation models with evidence separately from the analysis model. Avoid title-only and fork-ancestry-only matches.

Record Added, Updated, Unchanged, or Failed for every attempt in `games/log.jsonl`. Reanalyze Unchanged games. Preserve prior reports on failure. Store UTC repository creation, first catalog inclusion, and material update timestamps. Preserve original inclusion dates; recover legacy dates from Git. Link Updated reports to the prior committed README. Compare content independently of refresh provenance.

Commit redacted session messages, tool events, prompts, diagnostics, and result metadata under each game's `analysis/<run>-<attempt>/<record>/` directory. Put unmatched failures under `games/analysis/`. Publish logs-only PRs when reports are unchanged or fail. Keep failed batches open for inspection. Retain previous report versions in Git.

Serialize publication through atomic creation of `codex/catalog-publication-lock`. Release the lock after publication, before the debug hold. Inspect the owning run before deleting a stale lock after cancellation. Reapply later runs to the latest default branch. Respect repository merge requirements; queued PRs may still require reconciliation if the base changes before their eventual merge.

Start unauthenticated TryCloudflare sessions only for owner debug runs. Add temporary session URLs to the initial banner comment before analysis. Continue analysis when tunnel startup fails. Keep the same worker and tunnels alive through the 30-minute hold, stop the public tunnel afterward, and edit the comment to mark sessions expired. Treat forced cancellation as an exceptional lifecycle interruption; inspect Actions if an expiry update could not run.

Show outcome, report, overall and graphics scores, verified play/source links, documented creation models, and repository creation date with elapsed hours/days in each game comment. Show score transitions and the previous report link for updates. Keep analysis provenance in the committed log rather than confusing it with creation models.
