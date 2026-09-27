# The Nine Lives of Ash

[Open the game source](https://github.com/phirogue/SparkyGames)
**Repository created:** 2026-07-29T18:49:28Z
**Added to catalog:** 2026-09-27T04:05:54.560546+00:00
**Updated in catalog:** 2026-09-27T04:05:54.560546+00:00
**Built with:** [ChatGPT](https://raw.githubusercontent.com/phirogue/SparkyGames/main/docs/design/ai-transparency.md), [Kling](https://raw.githubusercontent.com/phirogue/SparkyGames/main/docs/design/ai-transparency.md)

**Overall rating:** 47/100. Deep roguelite deckbuilder scope with a deterministic rules core, JSON content engine, unit tests, balance sims, screenshot tour, and extensive design canon supports near-top catalog depth, but evidence is local-only with no public playable URL, no releases, no Pages, and only two inspected reference frames (one modal-obscured). Below Ashlands 55 for open-world breadth, below OSRS Tower Defense 52 and Kart Royale 50 for public play plus richer runtime visuals, and closest to Frosty Tactics 48, Neon Arena 48, Dead Signal 47, and THORNMERE 46: strong systems and coherent stylized art with limited public playability evidence. Screenshots and docs do not prove performance, balance, or full-run playability.

**Screenshot score:** 50/100. Battle frame shows coherent storybook UI with a detailed painted enemy portrait, legible intent/energy/skill systems, and portrait-phone composition, placing it above minimal DOM games like 2048 (45), chess rot (40), and Beachy Beachy Ball (35), but below densely detailed runtime frames like Taipo (55), THORNMERE (60), and OSRS Tower Defense (65); the central victory modal hides the chronicle and hand, and the second image is a title card that is discounted. Still images do not prove motion, feel, performance, or balance.

## Screenshots

![Inspected 506x899 PNG battle reference: portrait storybook page with dashed stitching; top environment card 'The Rooftops, Dusk' plus rules card; framed painterly vole portrait beside enemy plate 'The Vole' with thread-of-life and intent 'Next: Hold Very Still - 0 damage'; dimmed board behind a centered 'The Vole: dealt with. Continue' modal; fanned Ferocity energy card, skill tray with Scratch/Pounce and paw pips, and End Turn / Concentrate x2 / Slip Away buttons. Game's own runtime output, partly obscured by the victory modal.](https://raw.githubusercontent.com/phirogue/SparkyGames/main/screenshots/reference/battle.png)

Inspected 506x899 PNG battle reference: portrait storybook page with dashed stitching; top environment card 'The Rooftops, Dusk' plus rules card; framed painterly vole portrait beside enemy plate 'The Vole' with thread-of-life and intent 'Next: Hold Very Still - 0 damage'; dimmed board behind a centered 'The Vole: dealt with. Continue' modal; fanned Ferocity energy card, skill tray with Scratch/Pounce and paw pips, and End Turn / Concentrate x2 / Slip Away buttons. Game's own runtime output, partly obscured by the victory modal.

![Inspected 506x899 PNG title reference: black full-bleed page with large ornate storybook lettering 'The Nine Lives of Ashcat', black cat silhouette with rust-red scarf curled around a yarn-ball pendant, small top-left menu icon, and 'tap to begin' caption. Title/menu card, not active gameplay; game's own art output.](https://raw.githubusercontent.com/phirogue/SparkyGames/main/screenshots/reference/02_title.png)

Inspected 506x899 PNG title reference: black full-bleed page with large ornate storybook lettering 'The Nine Lives of Ashcat', black cat silhouette with rust-red scarf curled around a yarn-ball pendant, small top-left menu icon, and 'tap to begin' caption. Title/menu card, not active gameplay; game's own art output.

## Play

- On Windows, double-click run\_game.bat in the repo root to open the game in a phone-shaped desktop window (repo expects a local Godot binary).
- Alternatively open the game/ folder in the Godot 4 editor and press F5.
- Optionally double-click a launcher in play/apps or run play/play.ps1 to jump directly into a title, battle, prowl, or player-state part without touching the real save.
- Play the current prologue build as one continuous prowl across four encounters.
- Tap a skill card to open it and spend energy/paws to attack or use cat actions; tap hand energy cards to inspect them.
- Use End Turn to pass, Concentrate to recover energy, and Slip Away to retreat where allowed.

## Mechanics

- Turn-based card combat with paw action points
- Charge-to-power skills with persistent power across turns
- Four energy humours with wild Moonlight and true-Moonlight costs
- Pre-fight Approach entry choice: Stalk, Ambush, Case It, Ward, or walk in free
- Five-skill long-rest loadouts including Scratch
- Slip Away retreat with telegraphed-move punishment and satchel forfeit
- Concentrate turn-sacrifice energy recovery
- Scripted fights with HP floors, doom turns, withdrawal, and no-retreat locks
- Masked enemy intents unlocked through familiarity
- Nine-lives roguelite prowl structure with Hollow Court death handling
- Story choices that set flags and alter mechanics and later scenes
- Quests, casework, investigations, minigames, districts, and collectible lessons

## Tags

- roguelite
- deckbuilder
- card-game
- turn-based
- story-driven
- fantasy
- mystery
- single-player
- mobile
- portrait
- offline
- cats
- godot

## Controls

- Mobile controls: Supported
- Motion controls: Not established
- Gamepad: Not established
- Keyboard/mouse: Supported

## Player modes

- Human players: 1
- Modes: single-player

## Technologies

- **Godot 4.4** — engine ([evidence](https://raw.githubusercontent.com/phirogue/SparkyGames/main/game/project.godot))
- **GDScript** — language ([evidence](https://raw.githubusercontent.com/phirogue/SparkyGames/main/docs/design/tech-stack.md))
- **Godot mobile renderer** — rendering ([evidence](https://raw.githubusercontent.com/phirogue/SparkyGames/main/game/project.godot))
- **JSON** — framework ([evidence](https://raw.githubusercontent.com/phirogue/SparkyGames/main/docs/design/tech-stack.md))
- **Gradle** — build ([evidence](https://raw.githubusercontent.com/phirogue/SparkyGames/main/game/export_presets.cfg))

## Reconstructed prompt

Create a portrait mobile roguelite deckbuilder in Godot 4 GDScript called The Nine Lives of Ash: you are Ash, a murdered witch's cat solving her murder across 3-5 minute story-driven prowls; energy-deck plus 5-skill loadout turn-based card combat with paws, charge-to-power skills, four humours with wild Moonlight, approach choices, retreat costs, and scripted story fights; JSON content, deterministic rules core, offline single-player, storybook stitched-page UI with painted portraits, title screen, battle screen, and local Godot/Windows phone-window launch.

## Source evidence

- Repository phirogue/SparkyGames is public, default branch main, primary language GDScript; created 2026-07-29, pushed 2026-09-01; description empty, homepage empty, has\_pages false. ([source](https://api.github.com/repos/phirogue/SparkyGames))
- Language breakdown is dominated by GDScript with TeX and Python also present; repo size ~790MB. ([source](https://api.github.com/repos/phirogue/SparkyGames/languages))
- README defines SparkyGames as The Nine Lives of Ash: a brand-new mobile roguelite deckbuilder card game for iOS and Android where you are Ash, a murdered witch's cat familiar solving her murder in Hollowmere; 3-5 minute runs, quest/story-driven, offline-first. ([source](https://raw.githubusercontent.com/phirogue/SparkyGames/main/README.md))
- Current build is a playable prologue: four prologue encounters as one continuous prowl; tap skills to fight, tap hand cards, End Turn / Slip Away buttons; launched via run\_game.bat in a phone-shaped window or Godot editor game/ folder with F5. ([source](https://raw.githubusercontent.com/phirogue/SparkyGames/main/README.md))
- Windows launcher opens the game with the Godot binary at a local path; no public web, store, or hosted playable build is documented. ([source](https://raw.githubusercontent.com/phirogue/SparkyGames/main/run_game.bat))
- Tech stack doc decides Godot 4.x with GDScript (not C#), portrait one-handed orientation, pure rules engine in game/core with seeded RNG and command log, all cards/skills/enemies/quests as JSON with stable string IDs, versioned JSON saves; explicitly no multiplayer ever, single-player with no servers or accounts. ([source](https://raw.githubusercontent.com/phirogue/SparkyGames/main/docs/design/tech-stack.md))
- project.godot names the app The Nine Lives of Ash v0.1.0, main scene res://scenes/game.tscn, features 4.4 and Mobile, portrait 720x1280 viewport with 506x900 window override, stretch canvas\_items/keep, mobile rendering method. ([source](https://raw.githubusercontent.com/phirogue/SparkyGames/main/game/project.godot))
- Export presets scaffold Android AAB (com.sparkygames.ninelivesofash, Gradle build) and iOS IPA builds; store signing, icons, and team IDs are empty slots, and owner-actions doc confirms store accounts and launch gates are still pending. ([source](https://raw.githubusercontent.com/phirogue/SparkyGames/main/game/export_presets.cfg))
- Battle screen code states this is a mobile game where only clicks are registered, with a tap-target action row, tap layers, and tap-to-open card close-ups; spool chip answers taps/clicks. ([source](https://raw.githubusercontent.com/phirogue/SparkyGames/main/game/scenes/battle.gd))
- Core gameplay doc documents paw action points, charge-to-power skills, four energy humours including wild Moonlight, Approach entry choices, Slip Away retreat costs, Concentrate, scripted fights, masked intents, and long-rest loadouts. ([source](https://raw.githubusercontent.com/phirogue/SparkyGames/main/docs/design/core-gameplay.md))
- AI-transparency doc attributes stills to ChatGPT, motion to Kling, music to AI-generated commercial-tier tools, and code to AI-assisted development, with human story, design, curation, and approval. ([source](https://raw.githubusercontent.com/phirogue/SparkyGames/main/docs/design/ai-transparency.md))
- No GitHub releases exist, GitHub Pages is 404, homepage is null, and publishing docs are drafts pending accounts, icon, privacy URL, and owner approval; no publicly reachable playable URL was established. ([source](https://api.github.com/repos/phirogue/SparkyGames/releases))
- Screenshots directory is documented as generated tour output plus a small tracked reference set; only two tracked reference images were listed. ([source](https://raw.githubusercontent.com/phirogue/SparkyGames/main/screenshots/README.md))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 85/100: A murder-solving cat with real card grammar: approaches, paws, and wild Moonlight make every three-minute prowl feel like deduction by claw.
- 62/100: Clever systems and a charming storybook table, but I want the public build: the best fight I saw was hiding behind its own victory popup.
- 100/100: Purred, loafed, slipped away, solved it anyway. Ash is the familiar I would spend all nine lives on.

## Links

- [Source repository](https://github.com/phirogue/SparkyGames)
