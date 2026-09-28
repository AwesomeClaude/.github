# Audit issue #29 OpenCode behavior

Treat the issue, PR, comment, and Actions numbers below as private predecessor records. Inspect the committed analysis records for public evidence.

## Reuse the real run

- Inspect issue #29, Actions run 36294749657, and the result comment.
- Treat the ten finished, exit-zero OC sessions as nine accepted reports and one intentional `not_game` rejection, not ten successful game submissions.
- Observe analysis from 04:36:11 to 04:44:55 UTC on 2026-09-27: 8 minutes 44 seconds with three workers. Observe the result comment at 04:45:09, before the 04:45:14–05:15:14 owner hold. Inspect the successful expiry step and expired startup comment.
- Distinguish the old publication defect from OC failure: the publisher created PR #30, withheld automatic merge for any failed outcome, and returned exit 1. Observe PR #30's later merge at 05:24:48 UTC.
- Retain the current partial-success fix. Inspect the successful later runs 36297444704 and 36297527438, rather than claiming this old run used the fixed publisher.
- Use the committed `analysis/36294749657-1/` records instead of current reports when auditing this issue; account for moorestech's later refresh.
- Treat the September 27 audit SSH attempt to the workflow's requested AgentsWeb port 32657 as unavailable: the connection closed after the completed worker's hold. Do not claim a live process inspection or revive an unrelated worker.

## Prioritize prompt and capability improvements

### 1. Remove the authentication dead end

- Inspect [hypeJumper's credential probe](../games/parkjongbin0520-spec--hypeJumper/analysis/36294749657-1/run-002/messages.json#L373) and [PirateSeas's configuration probe](../games/AndreiBesliu--PirateSeas/analysis/36294749657-1/run-010/messages.json#L464).
- Reconcile the prompt's mandatory `gh api` instruction with the intentionally token-free OC environment. Observe all ten sessions failing their initial CLI requests and falling back to public HTTP requests.
- Account for environment enumeration, event-payload reads, `printenv GH_TOKEN`, GitHub-config directory inspection, and local token-reference searches. Treat these as unnecessary credential troubleshooting, not evidence of malicious intent. Limit the security conclusion to no token disclosure found in the inspected outputs; do not infer a comprehensive security guarantee.
- Propose this prompt edit: “Use public HTTPS evidence or the supplied read-only evidence cache. Treat unavailable authentication as expected. Keep credential discovery and workflow internals outside the analysis scope.”
- Supply authenticated metadata through the trusted publisher or a narrowly scoped evidence-fetching service. Keep the write-capable workflow token outside OC.
- Preserve the output schema; change evidence acquisition and execution boundaries instead.

### 2. Separate documentation from observed behavior

- Inspect [Devi's Lab's retained report](../games/shyamathreye--devis-lab/analysis/36294749657-1/run-003/report.json#L46). Observe “4 themes” in its rationale and “four ... plus pirate copy variant” in its mechanics.
- Compare [the theme definitions](https://github.com/shyamathreye/devis-lab/blob/main/src/data/themes.js) with the live world-selection screen: Unicorns, Animals, Ocean, Space, and Pirates. Count five selectable worlds. Note that the repository's latest main-branch commit predates the audit run; do not attribute this discrepancy to a post-run update without evidence.
- Distinguish the retained HTML-shell fetches for Devi's Lab and scumm-game from executed browser gameplay. Treat the reported play URLs as plausible and reachable, but not runtime-tested by OC.
- Reuse the audit's real browser interaction: enter Audit, select Animals, open Save the Balloons, choose Baby, complete PIG, and observe score 60. Treat scumm-game's rendered dock scene as rendering evidence only; do not claim a successful movement test from the audit's unchanged canvas observations.
- Propose this prompt edit: “Label material findings as documented, source-inspected, or runtime-observed. Resolve feature counts against current implementation or UI. Record the method and limitation of each playable-URL check.”
- Add browser execution/capture capability before requiring runtime verification from OC. Capture a gameplay frame when the live game is available but the repository has no screenshots. Keep a null graphics score when no frame was actually inspected.
- Reuse `source_analysis.finding` for evidence-level labels without a schema change. Consider structured verification metadata separately if machine-readable distinctions become necessary.

### 3. Fix compliance rather than repeat existing instructions

- Retain the existing requirements to read all linked game READMEs and avoid running catalog scripts. Do not add duplicate prose for these already-covered behaviors.
- Observe full linked-README reading in Lille only among the nine qualifying-game sessions. Inspect the other sessions' index-only, score-extraction, or selected-comparator reads. Treat claims of comparison with every catalog game as inadequately supported by those traces.
- Inspect [PirateSeas's script execution](../games/AndreiBesliu--PirateSeas/analysis/36294749657-1/run-010/messages.json#L2486): `games.py --help`, module import, `games.validate`, and `games.report_destination`. Distinguish this boundary violation from a catalog mutation; no mutation appears in that call.
- Supply a compact, immutable catalog evidence snapshot and track coverage outside the model. Keep score-only lists insufficient for substantive comparison. Preserve full-coverage requirements unless deliberately changing the comparison policy.
- Isolate OC report writes from catalog mutation and publisher execution. Enforce that separation with tool/filesystem boundaries rather than prompt wording alone.

### 4. Make scoring defensible

- Inspect [Lille's rationale](../games/leynos--lille/analysis/36294749657-1/run-001/report.json#L63): compare its “below every complete loop with verified play” claim with its score 28 and its cited complete games scored 18 and 25. Correct the contradiction in a future requested report refresh.
- Inspect [Ballz's rationale](../games/kurtmc--ball-game/analysis/36294749657-1/run-007/report.json#L183), HEX DANMAKU's comparison, and moorestech's original rationale. Distinguish implementation size, test counts, commits, 3D presentation, and documented ambition from observed execution quality.
- Propose this prompt edit: “Base each score on evidenced gameplay depth, scope, polish, and execution. State uncertainty separately. Treat source size, commit counts, and reported test counts as context rather than proof of production quality. Keep comparative inequalities consistent with the cited scores.”
- Keep genre-appropriate visual judgment and the existing stylized-art instruction. Treat automatic preference for 3D or photographic depth as a calibration problem, not a missing requirement to praise stylized art.
- Preserve the schema by improving `rating.reason`; avoid inventing a numerical confidence score without a defined method.

### 5. Define the prototype boundary

- Treat Lille's accepted status as a policy ambiguity, not a proven classification bug. Contrast its camera/static-entity prototype description with the prompt's undefined “actual game” threshold.
- Propose this clarification: “State whether the submission is a game, playable prototype, or engine/demo. Identify the implemented player interaction and gameplay loop; separate planned mechanics from implemented ones.”
- Use existing tags and evidence prose initially. Add a dedicated maturity field only with an explicit schema decision.

## Inspect each retained outcome

| Run | Outcome and seconds | Preserve strengths; inspect limitations |
| --- | --- | --- |
| 001 Lille | Added; 321.86 | Preserve complete catalog reading, source investigation, and null graphics. Inspect the prototype threshold and contradictory score rationale. Note the malformed JSON token and successful in-session repair. |
| 002 hypeJumper | Added; 170.48 | Preserve documented controls, releases, and explicit map-sketch classification. Treat Opus 4.8 as a repository attribution from CLAUDE.md, not independent proof of model use. Inspect credential probing and partial comparison coverage. |
| 003 Devi's Lab | Added; 180.79 | Preserve three-game identification and honest absence of inspected screenshots. Correct the world count; distinguish HTML-shell inspection from gameplay; use the live game for future visual evidence. |
| 004 scumm-game | Added; 118.44 | Preserve real image reads and separation of gameplay from background assets. Inspect the limited demo scope, selected-comparator coverage, and HTML-only play check. |
| 005 gen-ai-experiments | Rejected; 66.88 | Preserve rejection of the submitted collection root and its evidence. Keep specific nested game projects eligible for separate submissions; do not equate a successful rejection with pipeline failure. |
| 006 HEX DANMAKU | Added; 137.41 | Preserve inspected gameplay/menu separation and controls evidence. Inspect partial catalog coverage and graphics comparisons that overemphasize dimensionality. |
| 007 Ballz | Added; 103.38 | Preserve source-level mechanics, technology evidence, and null graphics. Inspect the claim of all-catalog calibration against only three full comparator README reads. |
| 008 moorestech | Added; 152.84 | Preserve inspected official gameplay images, engine manifest evidence, and refusal to label an unreleased store page playable. Inspect unsupported all-catalog superlatives and commit-count-based scoring. |
| 009 Zoo Keeper | Added; 120.94 | Preserve explicit MaxPlayers=1 evidence and unknown unsupported input categories. Distinguish source/declaration breadth from running functionality; inspect sparse comparator reading. |
| 010 PirateSeas | Added; 131.48 | Preserve source-backed gamepad findings and exclusion of a modeling preview from graphics scoring. Inspect credential probing, publisher-module execution, and index-only comparison. |

## Bound the conclusion

- Treat screenshot handling as a relative strength: inspect the recorded image-read calls and the independently opened scumm-game, HEX DANMAKU, and moorestech images. Preserve null graphics for non-gameplay assets instead of inventing scores.
- Keep fictional reviews under the existing fictional-reviews field and rendered heading. Do not classify their imagined first-person experiences as real user testimony; retain their labels when excerpts leave the report.
- Note the absence of target-repository clones, game-build execution, session timeouts, or observed unauthorized publication in the inspected OC command traces. Distinguish the workflow's own AgentsWeb helper clone from OC cloning a target game.
- Treat Lille's 5 minute 22 second duration as the longest session, not a hang. Observe roughly 35 seconds before its first target API request; avoid attributing the full duration to catalog reading. Investigate repeated API/authentication requests and duplicated catalog context before increasing concurrency.
- Preserve original prompts, reports, workflow files, and the pre-existing AGENTS.md change during this audit. Implement these recommendations only in a separately requested change and verify it through the real issue flow.
