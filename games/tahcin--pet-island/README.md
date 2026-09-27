# Pet Island

[Play the game](https://pet-island.vercel.app) · [View source](https://github.com/tahcin/pet-island)

| Overall rating | Screenshot score |
| :---: | :---: |
| **56/100** | **Not scored** |

<details>
<summary>Read the scoring rationale</summary>

### Overall rating

Far from AAA (single small island, no multiplayer, no voice acting or cinematics, 0 stars/forks, one-day build; screenshots, playability, performance and balance unverified from stills). Compared against all catalog games: broader systems scope than Kart Royale (50, complete single-track 3D kart loop) and OSRS Tower Defense (52, dense 2D TD) via photo-driven pets, 6 quest/volume types, AI dialogue with memory, progression/passport and day-night cycle, and a verified live deployment; closest to Ashlands (55, catalog breadth leader with no inspectable screenshots) but below moorestech (64/76 screenshots, deepest verified 3D sim) because no gameplay screenshot could be inspected and visual polish is unproven. Evidence gaps: gh api unavailable (no auth, REST rate-limited), so evidence is page plus raw-file fetches; source not cloned per instructions.

### Screenshot score

No inspectable gameplay screenshot.

</details>

## At a glance

| Detail | Value |
| --- | --- |
| Repository created | 26 Sep 2026 · 07:18 UTC |
| Added to catalog | 27 Sep 2026 · 06:20 UTC |
| Last updated | 27 Sep 2026 · 06:20 UTC |
| Documented creation models | [Claude Opus 5.5](https://github.com/tahcin/pet-island) |

## Play

- Open https://pet-island.vercel.app in a browser.
- Upload a photo of your pet (dogs, cats, rabbits and hamsters work best) or play with the Claude mascot if you have no photo.
- Wait for the reveal (about 5 seconds) showing your pet's name, personality traits and island name, then press Let's go.
- Move with WASD or arrow keys (Shift to run), drag the mouse to look, scroll to zoom; on phones use the on-screen joystick and action buttons.
- Press Space to talk, collect and turn in quests, T to talk to your pet, Tab to swap between you and the pet, C for pet-eye camera, J for journal, K for Island Passport, M for map, P for photo mode, Esc to pause.

## Mechanics

- Photo-to-pet pipeline: a vision call returns a typed pet spec (species, build, colors, markings, ears, tail) plus name, personality, island name and villagers
- Procedural parametric pet builder and animator (idle, walk, run, sit, dig, sniff, tricks) with no generative 3D
- Seeded procedurally generated island with beaches, terraced cliffs, river, shore foam, curved horizon and day-night cycle
- Companion mode and playable pet mode with pet-eye camera
- Species-matched collectibles (bones, yarn balls, carrots) plus beach shells
- Villager quests (fetch, letter delivery, show-pet, lookout visit) with journal, guide markers, minimap and accessory rewards
- Talk-to-pet dialogue grounded in world perception with moods, actions and memory, plus overheard villager gossip
- Persistent save with return news, streak bonuses, daily gifts and tasks, bond levels, Island Passport collection/stamps/bell shop and photo mode

## Tags

- 3d
- cozy
- pet-sim
- procedural
- ai-npc
- exploration
- single-player
- browser

## Controls

- Mobile controls: Supported
- Motion controls: Not established
- Gamepad: Not established
- Keyboard/mouse: Supported

## Player modes

- Human players: 1
- Modes: single-player

## Technologies

- **three ^0.186.1** — rendering ([evidence](https://github.com/tahcin/pet-island/blob/main/package.json))
- **@react-three/fiber ^9.8.1** — framework ([evidence](https://github.com/tahcin/pet-island/blob/main/package.json))
- **React ^19.3.0** — framework ([evidence](https://github.com/tahcin/pet-island/blob/main/package.json))
- **Vite ^8.3.1** — build ([evidence](https://github.com/tahcin/pet-island/blob/main/package.json))
- **TypeScript ^7.0.2** — language ([evidence](https://github.com/tahcin/pet-island/blob/main/package.json))
- **Hono ^4.13.9** — framework ([evidence](https://github.com/tahcin/pet-island/blob/main/package.json))
- **zustand ^5.0.15** — framework ([evidence](https://github.com/tahcin/pet-island/blob/main/package.json))

## Reconstructed prompt

Build a cozy Animal Crossing style 3D browser game called Pet Island: upload a pet photo, use a vision model to return a typed pet spec plus name, personality, island name and villagers, build a chibi toon pet procedurally in three.js, generate a seeded island with beach, terraces, river and town, add companion/pet play modes, collectibles, villager fetch quests, talk-to-pet dialogue with memory, saves with streaks and daily tasks, photo mode, minimap, and mobile joystick controls.

## Source evidence

- Repository page titles the project Pet Island and describes showing a pet photo then walking around a cozy Animal Crossing style island with a chibi 3D version that talks back, with a Claude mascot fallback. ([source](https://github.com/tahcin/pet-island))
- Repository advertises a playable deployment at https://pet-island.vercel.app; the URL serves the Pet Island single-page app shell and its JS bundle contains real game systems (pet follow/sniff/dig/play/trick state machine, collectibles, quests, villagers), confirming a playable game rather than a promo page. ([source](https://pet-island.vercel.app))
- Controls table documents WASD/arrows to move, Shift to run, mouse drag/scroll for camera, Space to talk/collect/turn in, T to talk to pet, Tab to swap character, C for pet-eye camera, J journal, K passport, M map, P photo mode, Esc pause. ([source](https://github.com/tahcin/pet-island))
- README states that on phones there is a joystick and action buttons, establishing mobile touch controls. ([source](https://github.com/tahcin/pet-island))
- No gamepad, accelerometer or gyroscope support is documented anywhere in the inspected README, PRD or controls table, so those remain unknown; no responsive-layout-only inference is made. ([source](https://github.com/tahcin/pet-island/blob/main/PRD.md))
- PRD scope is a single-page app with one player exploring with their pet and explicitly lists multiplayer (along with accounts and cloud saves) as what is not being built, establishing single-player with one human player. ([source](https://github.com/tahcin/pet-island/blob/main/PRD.md))
- Built-with section names three.js with React Three Fiber, Vite, Hono and zustand, all procedural, with the full spec in PRD.md. ([source](https://github.com/tahcin/pet-island))
- package.json pins three ^0.186.1, @react-three/fiber ^9.8.1, @react-three/drei ^10.7.9, React ^19.3.0, Vite ^8.3.1, TypeScript ^7.0.2, Hono ^4.13.9 and zustand ^5.0.15. ([source](https://github.com/tahcin/pet-island/blob/main/package.json))
- README attributes the build to Claude Opus 5.5 in Claude Code and runtime dialogue to small structured-output calls to claude-opus-5 with offline fallbacks. ([source](https://github.com/tahcin/pet-island))
- Docs folder contains only inspiration.md and the repo root has no committed screenshots folder (raw fetch 404), so no gameplay screenshot could be opened and inspected. ([source](https://github.com/tahcin/pet-island/tree/main/docs))
- gh CLI had no auth in this environment and api.github.com returned rate-limit exceeded, so GitHub evidence was gathered via page and raw.githubusercontent.com fetches instead of gh api. ([source](https://github.com/tahcin/pet-island))
- No catalog match: searched games/ directories and contents for pet-island/tahcin with zero hits, and scanned the catalog index plus every linked game README for calibration, so catalog\_slug is null. ([source](https://github.com/tahcin/pet-island))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 85/100: Uploaded my beagle and nearly dropped my phone when the little chibi version trotted over and sat down next to me. The trick chat actually works.
- 60/100: Sweet island loop with fetch quests and a chatty pet, but I wanted to see more of the town before the chores repeated.
- 100/100: Showed my cat to the island cat and it remembered us the next day. Pure cozy magic, passport stamps and all.

## Links

- [Source repository](https://github.com/tahcin/pet-island)
- [Play the game](https://pet-island.vercel.app)
