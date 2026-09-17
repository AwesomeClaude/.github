# SparkyGames — source, screenshot, and game analysis

**Repository:** [phirogue/SparkyGames](https://github.com/phirogue/SparkyGames)  
**Reviewed:** 2026-09-17  
**Method:** Read the public GitHub API, raw files, and tracked reference screenshots. No repository checkout was performed.

## Publication and modification dates

- **Public game/repository publication:** No standalone store release date or GitHub release was found. The public GitHub repository was created on **2026-07-29**.
- **Latest recorded modification:** The repository metadata reports the latest push on **2026-09-01** (latest GitHub metadata update: **2026-09-01**).
- **Evidence:** [GitHub repository metadata API](https://api.github.com/repos/phirogue/SparkyGames). These are repository dates, not proof of a public App Store or Google Play launch.

## Executive summary

*SparkyGames* is a Godot 4 mobile portrait game currently titled **The Nine Lives of Ash**. It is a playable prologue / vertical-slice for a story-driven roguelite deckbuilder: Ash, a murdered witch's cat familiar, investigates her death in the fog-bound city of Hollowmere.

The strongest design idea is the **inversion of a normal deckbuilder**: the player equips a fixed skill bar, while the deck contains only energy/fuel. This produces a compact, readable mobile interface and makes resource exhaustion the run clock. The game also integrates cat behavior into the rules rather than using it only as theme.

The codebase is unusually design-documented and test-oriented for a prototype. It separates pure rules from Godot UI, stores tuning and story in JSON, and includes unit tests, simulation, fuzzing, and screenshot-tour tooling. The main risk is scope: the repo describes a compelling complete game, but the shipped implementation is primarily the prologue and the later chapter/minigame content is partly design specification rather than demonstrated production content.

## What the source contains

- **Engine:** Godot 4.4 / GDScript, mobile renderer, 720×1280 viewport with a phone-shaped desktop override.
- **Core rules:** `RefCounted` state classes for combat, case board, prowl, crossings, lattice, stitch, testimony, and wards.
- **Services:** data loading, story loading, save files, audio, and strings.
- **Scenes:** title, hub, battle, journal, loadout, case board, shelf, story, settings, minigames, and ending.
- **Data-driven content:** skills, enemies, quests, encounters, energy cards, rules, environments, evidence, and story are JSON.
- **Verification:** unit tests, bot simulations, chaos/fuzz tests, layout guards, typography tests, and automated screenshot tours.

Useful source links: [README](https://github.com/phirogue/SparkyGames/blob/main/README.md), [architecture guide](https://github.com/phirogue/SparkyGames/blob/main/docs/architecture/README.md), [project configuration](https://github.com/phirogue/SparkyGames/blob/main/game/project.godot), [combat state](https://github.com/phirogue/SparkyGames/blob/main/game/core/combat_state.gd), [rules data](https://github.com/phirogue/SparkyGames/blob/main/game/data/rules.json), [skills data](https://github.com/phirogue/SparkyGames/blob/main/game/data/skills.json), [encounters](https://github.com/phirogue/SparkyGames/blob/main/game/data/encounters.json), [prologue story index](https://github.com/phirogue/SparkyGames/blob/main/game/story/prologue/index.json).

## Screenshot analysis

Tracked references are available in the [screenshots/reference folder](https://github.com/phirogue/SparkyGames/tree/main/screenshots/reference): [title screen](https://raw.githubusercontent.com/phirogue/SparkyGames/main/screenshots/reference/02_title.png) and [battle screen](https://raw.githubusercontent.com/phirogue/SparkyGames/main/screenshots/reference/battle.png).

### Title screen

- Portrait-first presentation with a dark brown/black field and a large centered logo.
- The logo communicates the hook immediately: ornate typography, a black cat silhouette, orange neckerchief, and a hanging orange thread/wool motif.
- “Tap to begin” is understated and atmospheric rather than a loud mobile CTA.
- Strength: distinctive identity and strong storybook / gothic-fairytale tone.
- Risk: the elaborate display type is beautiful but small text and contrast should be checked on real phones and accessibility settings.

### Battle screen

- Parchment/card-board frame reinforces the investigation and sewing motif.
- The upper area combines location, an atmospheric scene image, enemy portrait/HP, and a telegraphed next intent.
- A modal result (“The Vole: dealt with.”) confirms encounter resolution without losing the underlying scene.
- The lower area shows the energy card, skill tray, and large action controls: **End Turn**, **Concentrate**, and **Slip Away**.
- Visual hierarchy is legible: enemy danger above, resource and abilities below, action buttons at the bottom.
- Risk: the screen is information-dense, and the darkened modal plus decorative frame can reduce readability. The overlapping skill-card treatment must be validated across device widths.

## Reverse-engineered creation prompt

This is an **inferred recreation prompt**, not a claim about the author's original prompt:

> Create a polished mobile-portrait, offline-first, story-driven roguelite card game called *The Nine Lives of Ash*. The player is Ash, a murdered witch's cat familiar investigating her witch Elspeth's murder in a fog-bound fantasy city. Use a dark parchment, stitched-cloth, candlelit visual language with ornate storybook typography, expressive animal characters, and restrained wry humor.
>
> Make the game a 3–5 minute prowl loop. Let the player equip five skills before leaving home; make the deck contain simple energy cards rather than action cards. Use four energy humours: Ferocity, Guile, Shadow, and Moonlight. Draw a small hand, spend energy to charge skills, limit energy placements with three paw action points, and permanently exhaust spent energy during the prowl. Telegraph enemy intents that attack health, skills, or the hand. Give the player counterplay through damage, block, stealth, healing, hand protection, skill unjamming, and piercing attacks.
>
> Add a push-your-luck choice after encounters: slip away and bank part of the spoils, or press on for richer rewards while risking exhaustion and loss. Make death authored and meaningful: ordinary defeat spends no life, while marked mortal story beats spend one of Ash's nine lives and are remembered by the world. Include a short prologue teaching the systems through a vole, wisp, dog, rag-wraith, and an unwinnable parlor confrontation with The Unpicked.
>
> Structure the implementation as a data-driven Godot project: pure deterministic/refplayable rule state in GDScript, UI scenes separated from rules, JSON for content and balance, stable IDs, save/load support, unit tests, balance simulations, fuzz tests, and screenshot-tour verification. Add later investigation minigames that reuse the same deck and pressure systems: Seam & Stitch, Testimony, Patch the Ward, The Unpicking, and The Long Way Home.

## How to play

1. Start a prowl from the quest board.
2. Choose an approach when offered: **Stalk** (Shadow; hide and sharpen the first hit), **Ambush** (Ferocity; opening damage but a stronger retaliation), **Case It** (Guile; draw extra), or **Ward** (Moonlight; temporary block). Walk in for free when conserving fuel.
3. On each turn, draw toward the hand limit, then spend energy cards to power equipped skills. Each energy placement costs a paw; free instinct actions do not.
4. Read the enemy's next intent. Defend health, protect the hand from theft with **Loaf**, protect skills from jams/burns, or time attacks around enemy guard/healing.
5. Use **Concentrate** to spend the whole turn recovering one useful spent energy card; use **Purr** only if Ash can remain still while the channel completes.
6. **Scratch** is the always-available 1-damage instinct. Skills have limited charges per adventure.
7. After an encounter, choose **Press On** for a richer but riskier run or **Slip Away** to extract with only the configured retained share.
8. Treat the deck as Ash's stamina. When it is gone, the run is running on fumes. At home, change the loadout/deck and spend currencies in the Magpie Exchange.

## Mechanics used

### Combat and resource mechanics

- Energy-only deckbuilder; skills are equipped separately.
- Four resource types; Moonlight is wild for ordinary costs but special Moonlight costs require true Moonlight.
- Opening hand of 3, hand limit 5, default 3 paw placements per turn.
- Charge-to-power skills; stored charge can persist across turns.
- Limited skill charges, permanent spent pile, slow one-card recovery, and two Concentrate uses.
- Enemy intents are visible, target-specific, and sometimes masked until familiarity is earned.
- Enemy targets: health damage, hand theft/discard, skill jam/burn, self-block, and self-heal.
- Status effects include block, hidden, sharpened damage, purring/channel healing, loafing, jamming, and alarm/stealth hooks.
- Scripted encounter controls include HP floors, forced-exit turns, mortal beats, and no-retreat rooms.

### Meta, narrative, and investigation mechanics

- Push-your-luck prowl/extraction loop.
- Nine-life authored death system; ordinary loss is a bureaucratic refusal rather than automatic life loss.
- Persistent Gleam and Favors, deck tuning, equipment, loadouts, quest progression, journal/case evidence, standing, grudge effects, and story flags.
- Planned/partly implemented reusable minigames: line-drawing stitch puzzle, witness pressing/evidence presentation, polyomino ward patching, safe-order thread removal, and priced route decisions.
- Cat behaviors become real choices: purring, loafing, scratching, basking, hiding, stealing, and knocking things down.

### Architecture mechanics

- Command-driven pure state (`do_command`) makes combat and minigames deterministic, testable, and simulatable.
- Core code avoids scene-tree and disk concerns; services own persistence/content I/O.
- Stable string IDs and validation reduce content/script coupling.
- Automated tests cover combat, story, minigames, saves, layout, typography, art, and balance behavior.

## Tags

**Primary:** Card game, roguelike, roguelite, deckbuilder, story-rich, single-player, offline, mobile, portrait, fantasy, mystery, cats.  
**Mechanics:** Resource management, push-your-luck, turn-based combat, telegraphed attacks, hand management, limited-use abilities, stealth, investigation, branching choices, puzzle minigames.  
**Audience/tone:** Cozy-dark, gothic fairytale, witty, narrative adventure, low-gore fantasy.

## Rating: AA

**Scale used:** A = early prototype; AA = strong playable indie vertical slice; AAA = commercially complete, polished, released-scale production.

**Why AA:** The repository shows a real playable prologue, coherent visual identity, substantial content design, and unusually strong engineering/verification practices. It is not AAA evidence yet: Chapter 1 is described as still in design, publishing assets and store readiness remain open, screenshots are curated references rather than proof of broad device QA, and there is no public release/reception data. The concept and underlying systems are above an ordinary prototype, but completion and production breadth are not yet demonstrated.

**Subscores:** Concept **AAA-** · Core design **AA+** · Engineering discipline **AA+** · Visual direction **AA** · Content completeness **A/AA** · Release readiness **A**.

## Three generated user reviews and ratings

> These are fictional sample reviews generated from the repository evidence. They are not collected user reviews.

### 1 — 4.5/5

“Finally, a deckbuilder where the cards are fuel instead of a pile of actions. I love planning a five-skill cat build and then watching the energy spool run thin. The enemies telegraph exactly the kind of trouble they are about to cause, so Loafing against a thief feels smarter than simply blocking damage. The prologue ends just as the mystery gets sharp, but the tone is superb.”

### 2 — 4.0/5

“The art and writing have a wonderfully strange storybook mood. The vole tutorial is funny, and the bureaucracy around losing a life is a memorable twist. The battle screen is attractive but busy on a phone, and I sometimes had to parse the intent, card, and skill states at once. If the later casework minigames land as designed, this could become a very distinctive mystery game.”

### 3 — 3.5/5

“Great ideas, especially the push-your-luck extraction and the fact that Ash's deck is his stamina. I enjoyed the playable slice, but it currently feels more like a polished prototype than a finished game: some promised systems and chapters are still plans, and the loadout/deck economy needs more content to show its full range. I would follow development for the cat detective, the visual style, and the dry humor.”

**Generated-review average:** 4.0/5 (illustrative only; not a market score).

## Collected links

- [GitHub repository](https://github.com/phirogue/SparkyGames)
- [README / project overview](https://github.com/phirogue/SparkyGames/blob/main/README.md)
- [Architecture](https://github.com/phirogue/SparkyGames/blob/main/docs/architecture/README.md)
- [Core gameplay design](https://github.com/phirogue/SparkyGames/blob/main/docs/design/core-gameplay.md)
- [Minigame designs](https://github.com/phirogue/SparkyGames/blob/main/docs/design/minigames.md)
- [Death and nine lives](https://github.com/phirogue/SparkyGames/blob/main/docs/design/death-and-lives.md)
- [Store listing draft](https://github.com/phirogue/SparkyGames/blob/main/docs/publishing/store-listing.md)
- [Combat rules implementation](https://github.com/phirogue/SparkyGames/blob/main/game/core/combat_state.gd)
- [Skills](https://github.com/phirogue/SparkyGames/blob/main/game/data/skills.json)
- [Enemies](https://github.com/phirogue/SparkyGames/blob/main/game/data/enemies.json)
- [Encounters](https://github.com/phirogue/SparkyGames/blob/main/game/data/encounters.json)
- [Rules/tuning](https://github.com/phirogue/SparkyGames/blob/main/game/data/rules.json)
- [Prologue story](https://github.com/phirogue/SparkyGames/tree/main/game/story/prologue)
- [Tracked reference screenshots](https://github.com/phirogue/SparkyGames/tree/main/screenshots/reference)
- [Title screenshot](https://raw.githubusercontent.com/phirogue/SparkyGames/main/screenshots/reference/02_title.png)
- [Battle screenshot](https://raw.githubusercontent.com/phirogue/SparkyGames/main/screenshots/reference/battle.png)

## Bottom line

This is a promising, highly intentional **cat-mystery roguelite deckbuilder** with a strong mechanical thesis and an above-average prototype foundation. The next proof point is not more design documentation; it is shipping a complete first case with the promised investigation modules, device-tested UI, and a playable build outside the developer environment.

## Machine-readable files

- [JSON analysis report](/Users/igor/Documents/Codex/2026-09-17/https-github-com-phirogue-sparkygames-https/the-nine-lives-of-ash/game-analysis.json)
- [Reusable JSON Schema template](/Users/igor/Documents/Codex/2026-09-17/https-github-com-phirogue-sparkygames-https/outputs/game-analysis.schema.json)

## External services, APIs, and server requirements

The reviewed game appears to run as a **static/local-first client**:

- **Required to play:** no external API, server, authentication, network connection, analytics backend, ads, or IAP service is evidenced.
- **Local requirements:** the packaged Godot runtime/assets and local save storage.
- **Development tooling:** `requirements.txt` lists Pillow and NumPy for local tooling. These are not player runtime requirements.
- **Assessment scope:** public source snapshot reviewed on 2026-09-17.

The structured version is in the `external_services_and_runtime` object of the [JSON report](/Users/igor/Documents/Codex/2026-09-17/https-github-com-phirogue-sparkygames-https/the-nine-lives-of-ash/game-analysis.json#L1), and the same field is required by the [JSON Schema template](/Users/igor/Documents/Codex/2026-09-17/https-github-com-phirogue-sparkygames-https/outputs/game-analysis.schema.json#L1).
