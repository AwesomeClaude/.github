# Publish directly and preserve screenshots

Use direct fast-forward publication by default. Create a PR only with `ISSUE_CATALOG_AUTO_MERGE=false`. Keep the publication lock and one generated commit per branch. Reject stale-base pushes; retain recovery branches. Keep incomplete pipelines off the default branch. Leave organization PR permissions unchanged.

Archive screenshots beside each game report. Preserve source URLs and record content hashes. Render local files in all three README contexts. Reuse matching verified snapshots and retry missing files when reanalyzing a game. Keep failed sources visible in metadata rather than rendering broken images.

Reuse the 2026-09-28 backfill evidence: 135 of 140 screenshot records archived across 67 games. Recover Meridian Wake's four deleted PNGs from the verified parent of the upstream deletion commit; retain the pinned recovery URLs. Keep the five unavailable OxCity sources recorded as HTTP 404. Budget approximately 46 MiB for this initial archive; cap individual transfers at 8 MiB.

Inspect the live issue workflow after deployment. Confirm direct publication, matching report/profile output, archived screenshot bytes, issue links, and the same SSH worker during the owner hold. Treat manual-mode PR permission and race-rejection paths as separate from the default-mode E2E evidence.

Reuse the successful [issue #3 report](https://github.com/AwesomeClaude/.github/issues/3#issuecomment-5863690944): three refreshed games published directly without a PR, seven screenshot hashes matched, and both generated galleries resolved all 35 image references. Keep manual-mode permissions unchanged.
