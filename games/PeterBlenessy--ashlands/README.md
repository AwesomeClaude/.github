# Ashlands

[View source](https://github.com/PeterBlenessy/ashlands)

| Overall rating | Screenshot score |
| :---: | :---: |
| **55/100** | **Not scored** |

<details>
<summary>Read the scoring rationale</summary>

### Overall rating

New catalog top on scope/depth/technical ambition, but far from AAA. Most relevant comparators: Kart Royale (50 overall, ~60k-line complete 3D kart loop with 2 verified polished screenshots), neverquest (45 overall, deepest prior systems scope but text-UI only across ~591 files), Turbo Kart Rally (40 overall, complete indie 3D racer with HUD/menus) and Neural Sight (30 overall, photographic prototype with almost no loop). Ashlands exceeds all on paper breadth: ~94k lines, 16 contract-first subsystems, deferred engine (CDLOD, CSM, GTAO, TAA, AgX), 27 skills-by-use, spellmaking/alchemy/enchanting, topic dialogue/factions/crime, 18 completable quests and a 32-check + e2e harness. It therefore ranks above Kart Royale and neverquest on gameplay depth, scope and technical execution. Capped at 55 because visual polish is unverifiable (0 images committed, shots/ gitignored, no inspectable gameplay frame), self-reports 1/32 gate failing, waterline aliasing, terrain mottling and 20-35 fps on M3 Air, admits the blind Morrowind comparison never happened and AAA/perfect not reached, and source alone does not prove playability, performance, balance or fun. Above Taipo (35), Blackjack (28), Beachy (25) and curiosity (18) which are far narrower in systems and 3D tech.

### Screenshot score

No inspectable gameplay screenshot.

</details>

## At a glance

| Detail | Value |
| --- | --- |
| Documented creation models | Not established |

## Play

- Install Node 20+ and run npm install, then npm run play to build and serve at http://127.0.0.1:5200 (use play build, not dev hot-reload, for real sessions).
- Move with W/A/S/D (default gait is run); hold Shift to walk, Ctrl to sneak, Space to jump / swim up / ascend while levitating.
- Attack with Mouse 1 and block with Mouse 2 when armed; interact/talk/pick up with E.
- Toggle first/third person with V, levitation with T, water-walking with G, free camera with F1.
- Open Inventory (I), Character (C), Magic (M), Journal (J), Map (N); rest to regenerate health and fatigue (no over-time regen).
- Quicksave with F5 and quickload with F9; pause with Esc menu.

## Mechanics

- First/third-person open exploration of procedural volcanic island with CDLOD terrain, hydraulic erosion and triplanar splat materials
- Morrowind-like attributes, 27 skills that improve by use, levelling, classes, races and birthsigns
- Melee/ranged combat with attack, block, damage resolution and fatigue degradation
- Magic system with spellmaking, enchanting, alchemy and particle/volumetric effects
- Topic-based NPC dialogue with persuasion, factions, crime/bounty and disposition
- Hand-authored 18-quest graph with journal tracking and quest-driver harness
- Inventory, encumbrance, books, items, rest-to-heal economy and quicksave/quickload
- Procedural atmosphere: Rayleigh/Mie sky, weather/clouds, ocean with extinction/caustics, deferred CSM shadows, GTAO, TAA, AgX tonemap
- Procedural flora/fauna/architecture: instanced vegetation, creature/NPC bodies with animation, Vaelmyr towers/settlements/interiors
- Procedural audio: synthesized music/SFX with reverb plus spectral verification harness
- Verification discipline: 32-check regression gate, framing-search captures, bench/leak/e2e tooling, serialised browser verification

## Tags

- action-rpg
- rpg
- open-world
- 3d
- first-person
- third-person
- threejs
- webgl
- procedural-generation
- single-player
- fantasy
- typescript
- browser-game

## Reconstructed prompt

Build Ashlands, a Morrowind-spirit action-RPG in Three.js + WebGL2 as a fully procedural browser game with zero binary assets: CDLOD eroded terrain, Rayleigh/Mie sky, deferred CSM/GTAO/TAA/AgX pipeline, ocean/underwater, flora, Vaelmyr architecture, creatures/NPCs, first/third-person controller with run/walk/sneak/jump/levitation, melee/block combat, 27 skills-by-use, attributes/classes/races/birthsigns, spellmaking/alchemy/enchanting, topic dialogue, factions/crime/persuasion, 18-quest graph with journal, procedural music/SFX, full UI panels and quicksave, plus a deterministic capture gate, e2e/quest/audio/bench harnesses and an art bible.

## Source evidence

- Repo resolves to addable-labs/ashlands: an action-RPG in the spirit of Morrowind, first/third-person exploration, skills-by-use, spellmaking, topic dialogue, hand-authored quest graph, running in browser on Three.js r185 + WebGL2 with everything procedural and zero binary assets. ([source](https://github.com/addable-labs/ashlands))
- Public API metadata: created 2026-08-02, pushed 2026-09-21, language TypeScript, 0 stars / 0 forks / 0 watchers, MIT license, ~2216 KB size, default branch main. Requested URL PeterBlenessy/ashlands redirects to addable-labs/ashlands. gh CLI (gh api) was unusable without auth, so evidence was gathered via unauthenticated public REST/raw endpoints instead. ([source](https://api.github.com/repos/PeterBlenessy/ashlands))
- Self-reported scale: ~94,000 lines TypeScript across 160 files, 16 contract-first subsystems, 114 tool files, largest file TerrainMaterial.ts 4317 lines, 18 quests, zero binary assets, 32 gate checks + 17 e2e checks plus bench/leak/audio/quest harnesses. ([source](https://github.com/addable-labs/ashlands/blob/main/EVALUATION.md))
- Current state self-report: gate 1 of 32 failing (coast palette check), typecheck clean, e2e 16/16, quests drivable to completion, 20-35 fps at capture resolution on M3 MacBook Air, plus open defects: waterline stair-stepping, terrain mottling, dawn godrays missing. ([source](https://github.com/addable-labs/ashlands/blob/main/README.md))
- RPG/quest scope evidenced by source tree: src/quest holds QuestData.ts (~74KB), Topics.ts, Quests.ts, Factions.ts, Crime.ts, Persuasion.ts, Npcs.ts, Books.ts; src/rpg holds RPG.ts, Character.ts, Attributes.ts, Skills-by-use, Magic.ts, Effects.ts, Alchemy.ts, Enchant.ts, Inventory.ts, Items.ts, Rest.ts. ([source](https://github.com/addable-labs/ashlands/tree/main/src/quest))
- RPG subsystem listing confirms attributes, classes, races, magic/spell effects, alchemy, enchanting, inventory, rest/fatigue systems backing the Morrowind-like loop. ([source](https://github.com/addable-labs/ashlands/tree/main/src/rpg))
- Recursive git tree (310 paths) contains zero .png/.jpg/.webp/.gif/.mp4 files; .gitignore explicitly excludes shots/ and dist-\*, so canonical verification captures are not committed and no gameplay screenshot is inspectable in-repo. ([source](https://github.com/addable-labs/ashlands/blob/main/.gitignore))
- Honest evaluation admits the blind side-by-side vs real Morrowind never happened (no reference screenshots obtained), perfect/AAA not reached, ~1.32M tokens for one shipped visual fix in closing phase, and multiple harness instruments that manufactured false signal. ([source](https://github.com/addable-labs/ashlands/blob/main/EVALUATION.md))
- Art direction target is defined in ART\_BIBLE.md: Morrowind-2002 baseline, ash/basalt/ember/sulphur palette with saturation discipline, 10-point technical bar (ground contact, CSM shadows, aerial perspective, no tiling, PBR differentiation) and 8-axis critic rubric requiring \>=8/10 with zero artifacts. ([source](https://github.com/addable-labs/ashlands/blob/main/ART_BIBLE.md))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 82/100: Fictional illustrative review one: rolled a skills-by-use build, rested to heal like it is 2002, talked my way through topic threads into a faction quest and actually finished it. For a browser toy with no assets it feels shockingly Morrowind-shaped.
- 58/100: Fictional illustrative review two: ambitious systems, earnest evaluation docs, but I never saw a screenshot I could trust, the fps warning scared my laptop, and levitation plus spellmaking still need a real playtest before I call it more than a brilliant rig.
- 100/100: Fictional illustrative review three: a contract-first 94k-line procedural RPG with its own gate harness, reverted negatives kept as evidence and an honest postmortem about lying instruments? As an agentic experiment this is the most interesting game in the catalog, warts and all.

## Links

- [Source repository](https://github.com/PeterBlenessy/ashlands)
- [Related link](https://github.com/addable-labs/ashlands)
- [Related link](https://github.com/addable-labs/ashlands/blob/main/README.md)
- [Related link](https://github.com/addable-labs/ashlands/blob/main/EVALUATION.md)
- [Related link](https://github.com/addable-labs/ashlands/blob/main/ART_BIBLE.md)
