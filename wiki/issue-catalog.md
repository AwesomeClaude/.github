# Publish issue game links

Post the banner and “I’m on it. Analyzing the links may take 10–30 minutes.” as the first job step. Link to the current attempt’s analysis job; use the run URL if job lookup fails. Pin the banner URL to the workflow commit. Keep the issue body unchanged.

Put every qualifying game in the root catalog and screenshot gallery. Treat `repository_url` as optional; normalize an omitted, null, or empty value to null. Require an original `source_url`; reuse the repository URL for existing repository-only reports. Verify every supplied source repository. Preserve existing game directories and original-link-derived directories. Always reanalyze submitted games. Use one validation and publication path for additions and refreshes.

Fetch the latest default branch before applying report artifacts. Create a catalog PR and request a squash auto-merge with an exact head-commit match. Enable repository auto-merge. Set repository variable `ISSUE_CATALOG_AUTO_MERGE=false` to leave new catalog PRs open. Respect required checks and reviews. Auto-merge completed batches independently of individual submission failures. Keep pipeline errors visible and leave their recovery PRs open. Report merge failures on the issue and fail the publication step. Keep published branches available for the game README links.

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

Record Added, Updated, Unchanged, or Failed for every attempt in `games/history/<run>-<attempt>.jsonl`. Preserve migrated entries in `games/history/legacy.jsonl`. Write each run independently to avoid shared append conflicts. Reanalyze Unchanged games. Preserve prior reports on failure. Store UTC repository creation, first catalog inclusion, and material update timestamps. Preserve original inclusion dates; recover legacy dates from Git. Link Updated reports to the prior committed README. Compare content independently of refresh provenance.

Commit redacted session messages, tool events, prompts, diagnostics, and result metadata under each game's `analysis/<run>-<attempt>/<record>/` directory. Put unmatched failures under `games/analysis/`. Publish logs-only PRs when reports are unchanged or fail. Auto-merge diagnostic-only PRs when every submission fails but the pipeline completes. Retain previous report versions in Git.

Serialize publication through atomic creation of `codex/catalog-publication-lock`. Release the lock after publication, before the debug hold. Inspect the owning run before deleting a stale lock after cancellation. Reapply later runs to the latest default branch. Respect repository merge requirements; queued PRs may still require reconciliation if the base changes before their eventual merge.

Start unauthenticated TryCloudflare sessions only for owner debug runs. Add temporary session URLs to the initial banner comment before analysis. Continue analysis when tunnel startup fails. Keep the same worker and tunnels alive through the 30-minute hold, stop the public tunnel afterward, and edit the comment to mark sessions expired. Treat forced cancellation as an exceptional lifecycle interruption; inspect Actions if an expiry update could not run.

Show outcome, report, overall and graphics scores, verified play/source links, documented creation models, and repository creation date with elapsed hours/days in each game comment. Show score transitions and the previous report link for updates. Keep analysis provenance in the committed log rather than confusing it with creation models.

## Recover metadata and model-field failures

Fetch authenticated GitHub repository metadata during publication, not in the unauthenticated analysis process. Keep the workflow token out of OpenCode's environment. Normalize creation-model `url` evidence to `evidence_url`; specify the exact object shape in the prompt. Commit raw candidate reports alongside diagnostic logs even when validation fails.

Inspect [issue #16](https://github.com/agents-dev/Astra-Top-Games/issues/16), [merged PR #17](https://github.com/agents-dev/Astra-Top-Games/pull/17), and [its result](https://github.com/agents-dev/Astra-Top-Games/issues/16#issuecomment-5852336200) for a real alternative-URL refresh of 2048 and addition of T-Rex Runner. Verify original inclusion time, previous report link, labeled link union, and conversation exports. Observe 85- and 143-second analyses with public unauthenticated sessions and retained SSH hold.

Inspect [five-game issue #18](https://github.com/agents-dev/Astra-Top-Games/issues/18) and [partial PR #19](https://github.com/agents-dev/Astra-Top-Games/pull/19) for the regression evidence: UnityPuzzle emitted a valid evidence URL under `url`, while OSRS Tower Defense and Find Panda hit unauthenticated GitHub metadata rate limits. Retain these failed-attempt logs; reanalyze the five randomly selected games after deploying the recovery changes. Do not infer failure of game analysis from failure of metadata enrichment.

## Record game technology

Collect `technologies` with `name`, nullable `version`, `category`, and `evidence_url` in every analysis. Inspect project manifests, configuration, documentation, or source evidence. Distinguish engines, languages, frameworks, rendering, physics, audio, and build tools. Record only technologies used by the game. Preserve documented version strings or ranges; use null for unknown versions and an empty array for unknown stacks. Render the entries with evidence in each game README. Accept existing reports without the field until their next refresh.

## Verify recovery with five real games

Inspect [issue #21](https://github.com/agents-dev/Astra-Top-Games/issues/21), [merged PR #22](https://github.com/agents-dev/Astra-Top-Games/pull/22), and [the result comment](https://github.com/agents-dev/Astra-Top-Games/issues/21#issuecomment-5852419388). Verify successful reports for Pizza Chef, Dead Signal, UnityPuzzle, OSRS Tower Defense, and Find Panda. Inspect retained raw candidates and conversations for all five; check authenticated repository creation metadata and independently documented creation-model evidence for Dead Signal and UnityPuzzle. Keep the earlier [partial PR #19](https://github.com/agents-dev/Astra-Top-Games/pull/19) available for failure diagnosis. Do not treat an unused SSH port as proof of analysis continuing after public-tunnel failure.

## Reuse the technology and failure E2E evidence

Inspect [technology issue #26](https://github.com/agents-dev/Astra-Top-Games/issues/26), [merged PR #27](https://github.com/agents-dev/Astra-Top-Games/pull/27), and [its result](https://github.com/agents-dev/Astra-Top-Games/issues/26#issuecomment-5852498871). Check the rendered Technologies sections and structured evidence for Godot 4.4/GDScript in The Nine Lives of Ash and Unity 2022.3.62f2/C# in UnityPuzzle. Verify that the existing UnityPuzzle slug, original inclusion time, source label, and immutable previous-report link survive the refresh. Inspect committed candidates and conversation logs.

Inspect [mixed-result issue #23](https://github.com/agents-dev/Astra-Top-Games/issues/23) and [partial PR #24](https://github.com/agents-dev/Astra-Top-Games/pull/24) for an updated UnityPuzzle report alongside a real Example Domain rejection. Inspect retained candidate rejection and session records. Treat closed PRs #19 and #24 as superseded diagnostic evidence, not unresolved delivery work; retain their branches.

Reproduce public-tunnel failure on a separate runner without changing production holds: start OpenCode normally, run preparation with an unreachable HTTPS proxy and localhost excluded from proxying, then clear proxies before analysis. Inspect the observed preflight-runner artifacts at `/tmp/catalog-preflight-work/artifact` while that runner remains alive. Confirm actual cloudflared download failure, `debug_available: false`, successful real 2048 analysis, and a real Example Domain rejection. Do not publish this isolated negative test to the catalog.

Inspect [issue #16's startup comment](https://github.com/agents-dev/Astra-Top-Games/issues/16#issuecomment-5852311996) for the real expiry confirmation. Check the successful hold/expiry steps at 04:05:50/51 UTC on 2026-09-27; observe the former public session returning HTTP 530 and the former SSH endpoint closing after the worker exits. Preserve later workers' full holds without waiting idle. Distinguish these observed checks from unexercised exact-content Unchanged and simultaneous-publication branches.

## Keep reports readable

Separate navigation, scores, metadata, and screenshots. Show scores in a compact table. Collapse scoring explanations behind a labeled disclosure. Format display dates to UTC minutes; preserve precise timestamps in structured reports. Rebuild existing game pages with `./scripts/games.sh` after changing the renderer.

## Verify submission isolation

Submit a real game and a real non-game link in the same owner issue. Inspect both outcomes and retained evidence over SSH. Confirm that publication succeeds and auto-merges the valid report alongside failure diagnostics. Verify independent per-run history files, readable report tables, expandable scoring details, and the unchanged owner hold. Keep publication failures distinct from submission failures.

## Reuse partial-success and layout evidence

Inspect [mixed-result issue #32](https://github.com/agents-dev/Astra-Top-Games/issues/32), [its result](https://github.com/agents-dev/Astra-Top-Games/issues/32#issuecomment-5853034640), and [merged PR #34](https://github.com/agents-dev/Astra-Top-Games/pull/34). Confirm one updated moorestech report and one rejected non-game repository, successful analysis and publication steps, and automatic merge. Inspect the retained candidates, conversations, and `games/history/36297444704-1.jsonl`. Preserve the original inclusion timestamp and immutable previous-report link.

Inspect [diagnostic-only issue #33](https://github.com/agents-dev/Astra-Top-Games/issues/33), [its result](https://github.com/agents-dev/Astra-Top-Games/issues/33#issuecomment-5853037091), and [merged PR #35](https://github.com/agents-dev/Astra-Top-Games/pull/35). Confirm Example Domain rejection, successful publication, and changes limited to diagnostic evidence and `games/history/36297527438-1.jsonl`. Compare the two independent history files. Verify all 39 migrated entries byte-for-byte against the former aggregate. Treat per-run history as removal of one conflict hotspot, not proof that same-game reports or the generated index cannot conflict.

Open the published moorestech report on GitHub. Check the separate navigation row, score table, collapsed rationale, working disclosure, readable UTC metadata, and screenshots. Keep all 36 regenerated pages consistent with the renderer. Preserve precise JSON timestamps and full scoring evidence.

Use the recorded analysis durations of 108.46 seconds for moorestech, 71.31 seconds for the rejected repository, and 35.45 seconds for Example Domain as this run's throughput evidence. Treat source inspection and catalog comparison as the main analysis cost. Inspect the successful publication steps before the owner holds. Reuse the SSH observation at 05:35 UTC on 2026-09-27: both workers retained their original OpenCode servers, public tunnels, AgentsWeb tunnels, and `sleep 1800` processes. Leave both holds uninterrupted. Distinguish these observations from unexercised simultaneous lock contention, interrupted pipelines, and forced merge failures.
