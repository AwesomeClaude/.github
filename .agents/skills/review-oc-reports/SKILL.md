---
name: review-oc-reports
description: Review OpenCode game-analysis reports to recommend evidence-based improvements to the project's prompt.md.
---

# Improve the OpenCode analysis prompt

Read each requested `readme.json` directly. Compare it with the project's `prompt.md` and its example. Do not run automated report checks.

Check source claims against their links. Open linked screenshots when available; compare the observations with what is visible and judge whether the score reflects gameplay screenshots. Confirm that all reviews are identified as fictional. Separate supported findings from inferences and unverifiable claims.

Make improvements to `prompt.md` the main conclusion. Group recurring or consequential report defects. Distinguish gaps in the prompt from failures to follow existing instructions and limits of available evidence. For each genuine prompt gap, recommend a precise, imperative edit, cite the report evidence, and explain its expected benefit and any output-schema trade-off. Do not add duplicate instructions for failures the prompt already addresses.

Briefly report each run's strengths, omissions, and factual risks after the prompt recommendations. State when an output is missing or unreadable. Do not change `prompt.md` or reports unless asked.
