# Turbo Kart Rally

[View source](https://github.com/bridge-mind/turbo-kart-rally/tree/main)

| Overall rating | Screenshot score |
| :---: | :---: |
| **40/100** | **70/100** |

<details>
<summary>Read the scoring rationale</summary>

### Overall rating

Impressive complete indie kart racer with full loop, 8 karts, items, AI, HUD and music, but far from AAA: single track, no multiplayer/online, limited modes, simple low-poly procedural art/audio, and no evidence of extensive balancing, QA, accessibility or live-ops scale. Evidence gaps: no playtest metrics, performance data, or depth beyond one circuit.

### Screenshot score

Visible gameplay shows coherent colorful low-poly stylization, readable karts/track, varied scenery with mountains/trees/grandstands, and polished HUD/minimap/leaderboard. Detail, lighting and textures are simple indie-level, not high-end, but composition and polish are strong for procedural assets.

</details>

## At a glance

| Detail | Value |
| --- | --- |
| Documented creation models | Not established |

## Screenshots

![Third-person gameplay on asphalt circuit: red player kart chasing two rivals, boost pad chevrons ahead, red-white curbs, TURBO/KART/RALLY billboards, low-poly trees and mountains, HUD with LAP 1/3, timer, 8-place leaderboard, item slot, minimap, 137 km/h speedometer and 7th place.](https://raw.githubusercontent.com/bridge-mind/turbo-kart-rally/main/docs/screenshots/race.jpg)

Third-person gameplay on asphalt circuit: red player kart chasing two rivals, boost pad chevrons ahead, red-white curbs, TURBO/KART/RALLY billboards, low-poly trees and mountains, HUD with LAP 1/3, timer, 8-place leaderboard, item slot, minimap, 137 km/h speedometer and 7th place.

![Gameplay beside grandstand: red kart on grass next to crowded colorful low-poly spectators, checkered start line visible, HUD shows triple-mushroom item x3, LAP 1/3, 8th place at 36 km/h, minimap and leaderboard.](https://raw.githubusercontent.com/bridge-mind/turbo-kart-rally/main/docs/screenshots/items.jpg)

Gameplay beside grandstand: red kart on grass next to crowded colorful low-poly spectators, checkered start line visible, HUD shows triple-mushroom item x3, LAP 1/3, 8th place at 36 km/h, minimap and leaderboard.

![Title card overlaying live demo race: large TURBO KART RALLY logo, PRESS ENTER / CLICK TO START prompt, three karts on start straight under gantry, mountains and trees behind; menu/title, not active racing.](https://raw.githubusercontent.com/bridge-mind/turbo-kart-rally/main/docs/screenshots/title.jpg)

Title card overlaying live demo race: large TURBO KART RALLY logo, PRESS ENTER / CLICK TO START prompt, three karts on start straight under gantry, mountains and trees behind; menu/title, not active racing.

![Character-select menu: 8 racer cards with portraits and SPD/ACC/HDL/WGT bars, Blaze detail panel with class 100cc NORMAL and 3 LAPS selectors, RACE! button and controls footer over blurred track background.](https://raw.githubusercontent.com/bridge-mind/turbo-kart-rally/main/docs/screenshots/character-select.jpg)

Character-select menu: 8 racer cards with portraits and SPD/ACC/HDL/WGT bars, Blaze detail panel with class 100cc NORMAL and 3 LAPS selectors, RACE! button and controls footer over blurred track background.

![Results menu: VICTORY! 2 LAP RACE FINAL STANDINGS table 1st-8th with best/total times, Rex YOU first at 1:34.74, RACE AGAIN and MAIN MENU buttons over dimmed track; menu, not gameplay.](https://raw.githubusercontent.com/bridge-mind/turbo-kart-rally/main/docs/screenshots/results.jpg)

Results menu: VICTORY! 2 LAP RACE FINAL STANDINGS table 1st-8th with best/total times, Rex YOU first at 1:34.74, RACE AGAIN and MAIN MENU buttons over dimmed track; menu, not gameplay.

## Play

- Open the play link in a desktop WebGL2 browser and click or press Enter on the title screen.
- Choose one of 8 racers, pick 50cc/100cc/150cc class and lap count, then press RACE!.
- Hold accelerate during the final countdown moment for a rocket start when GO shows.
- Race 3 laps around Palm Cove Circuit against 7 AI, holding position 1st-8th on the HUD.
- Steer with A/D or arrows or left stick, accelerate with W/Up, brake/reverse with S/Down.
- Tap Space to hop, hold Space while steering to drift; release when sparks turn blue/orange/purple for mini-turbo boost.
- Drive over item boxes for roulette, then fire with E/X/Shift to use mushrooms, shells, bananas, star, lightning or blue shell.
- Hit boost pads, trick off jump ramps, avoid off-road grass, bananas and shells; watch minimap, speedometer, final-lap and wrong-way banners to finish first.

## Mechanics

- 8-racer arcade kart physics with drift, hop and 3-level mini-turbo boost
- Rocket start timing, boost pads, jump-ramps with trick boost, off-road slowdown and wall bounce
- Weight-based kart-to-kart collisions, spin/tumble/shrink hit states with star invulnerability
- 8 position-weighted items: mushroom, triple mushroom, banana, green shell, homing red shell, star, lightning, blue shell
- Item boxes with respawn, roulette delay, drag-and-throw bananas/shells, projectile bouncing and homing
- 7 AI drivers following racing line, drifting, avoiding hazards, using items tactically with rubber-banding
- Lap/checkpoint validation, live places, countdown, final-lap speedup, wrong-way detection and results with splits
- Chase camera with speed FOV, shake and intro flyover, minimap, speedometer and procedural audio/music

## Tags

- kart-racer
- arcade
- racing
- threejs
- webgl
- procedural-generation
- single-player
- ai-generated
- browser

## Reconstructed prompt

Build Turbo Kart Rally, a Mario Kart-style arcade kart racer in Three.js with no build step and 100% procedural assets. Include 8 original racers with stats, one 2km scenic circuit with boost pads, jumps and item boxes, drift with 3-stage mini-turbo, 8 position-balanced items, 7 rubber-banding AI, chase camera, minimap HUD, menus/results, and synthesized sound plus chiptune music. Playable in desktop WebGL2 browser with keyboard and gamepad.

## Source evidence

- Arcade kart racer built entirely with Three.js r170 as ES modules with no build step; all meshes, CanvasTexture textures, sounds and music are generated procedurally in code with no asset files. ([source](https://github.com/bridge-mind/turbo-kart-rally/blob/main/README.md))
- Built by five Claude Opus 5.5 sub-agents working in parallel from a single Mario Kart clone prompt, coordinated via an architecture contract and shared config plus event bus, with no follow-up questions. ([source](https://github.com/bridge-mind/turbo-kart-rally/blob/main/README.md))
- Roster of 8 original racers (Blaze, Zippy, Bella, Toadly, Rex, Grumbo, Koopz, Dotty) with speed/accel/handling/weight stats, 50cc/100cc/150cc classes, and single Palm Cove Circuit (~2.1km, 8 boost pads, 2 jump ramps, 30 item boxes). ([source](https://github.com/bridge-mind/turbo-kart-rally/blob/main/src/config.js))
- Arcade driving model: hop/drift with 3-stage mini-turbo (blue-orange-purple), rocket start, trick boosts, off-road slowdown, wall bumps, weight-based kart collisions, and AI that follows racing line, drifts, dodges hazards and rubber-bands. ([source](https://github.com/bridge-mind/turbo-kart-rally/blob/main/ARCHITECTURE.md))
- Eight position-weighted items (mushroom, triple mushroom, banana, green shell, homing red shell, star, lightning, blue shell) with roulette, item boxes, projectiles and hazards, plus pooled particles, bloom, chase camera and minimap HUD. ([source](https://github.com/bridge-mind/turbo-kart-rally/blob/main/ARCHITECTURE.md))
- Fully procedural Web Audio: engine/drift/item sounds plus sequenced chiptune menu/race music that speeds up on final lap; game flow is Title \> Character Select \> Intro flyover \> 3-2-1-GO \> 3-lap race vs 7 AI \> Results. ([source](https://github.com/bridge-mind/turbo-kart-rally/blob/main/README.md))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 100/100: Fictional review: I picked Rex for the memes and stayed for the drift sparks. That purple mini-turbo out of the S-bend felt illegal in a browser tab.
- 60/100: Fictional review: Fun for three races, but my couch crew wanted split-screen and a second cup. The blue shell has personal beef with me specifically.
- 80/100: Fictional review: As a fictional kart dad, I approve: readable track, bouncy chiptune, grandstands full of gummy bears. Docked one star because Toadly beat me on the bridge.

## Links

- [Related link](https://bridge-mind.github.io/turbo-kart-rally/)
- [Related link](https://github.com/bridge-mind/turbo-kart-rally/blob/main/README.md)
- [Related link](https://github.com/bridge-mind/turbo-kart-rally/blob/main/ARCHITECTURE.md)
- [Source repository](https://github.com/bridge-mind/turbo-kart-rally/tree/main)
