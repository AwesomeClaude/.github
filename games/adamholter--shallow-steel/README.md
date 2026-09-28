# Shallow Steel

[View source](https://github.com/adamholter/shallow-steel)

| Overall rating | Screenshot score |
| :---: | :---: |
| **45/100** | **Not scored** |

<details>
<summary>Read the scoring rationale</summary>

### Overall rating

Real-time 3D melee gym with a genuinely deep documented combat model (phase timings, directional strikes, timed parry/riposte, guard/stamina, evade i-frames, weapon switch, shield pickup, destructibles, HUD, touch layout) and scripted QA/playthrough evidence. Most relevant comparators, excluding the target: Kart Royale (50, complete polished 3D loop, verified screenshots) ranks above because its visuals and loop are inspectable; HEX DANMAKU (48) and Dead Signal (47) rank just above on verified presentation; THORNMERE (46) and neverquest (45) are peers on systems depth vs polish. Shallow Steel sits at 45: below Ashlands (55, far broader RPG scope) and moorestech (64, catalog top) on scope, and capped by evidence gaps — no inspectable gameplay screenshot, no public playable URL (localhost only, Pages disabled), ~74KB of game source from a single-day-old 1-commit repo, and source/docs alone cannot prove playability, performance, balance or fun.

### Screenshot score

No inspectable gameplay screenshot.

</details>

## At a glance

| Detail | Value |
| --- | --- |
| Repository created | 26 Sep 2026 · 21:17 UTC |
| Added to catalog | 27 Sep 2026 · 06:18 UTC |
| Last updated | 27 Sep 2026 · 06:18 UTC |
| Documented creation models | [GPT-6 Astra](https://github.com/adamholter/shallow-steel/blob/main/README.md) |

## Play

- Launch locally with npm run dev and open http://localhost:9411, then Enter the gym from the menu.
- Move with WASD or arrow keys relative to the camera; drag or click to strike directionally, or use J, I, U for horizontal, descending and thrust attacks.
- Parry with right mouse button or K just before impact, hold to guard, evade with Space or L, switch greatsword and one-handed sword with Q, collect a dropped shield with F.
- Read the skeleton weapon raise and gold cue, riposte after a timed parry, manage stamina, and clear three trials of 3, 4 and 5 skeletons with partial healing between trials.

## Mechanics

- Directional melee strikes with separate windup, active and recovery phases and greatsword cleave vs faster one-handed attacks
- 190 ms timed parry opening a riposte window plus sustained stamina-cost guard
- Stamina-consuming guard and invulnerable directional evade
- Enemy attack scheduling where fast skeleton counters can punish slow greatsword recovery
- Destructible barrels, crates, jars and tables breaking into bouncing debris with knockback transfer
- Collectible dropped shields, three-trial progression with partial between-trial healing, loss/retry/victory/pause flow
- Procedural joint animation, coat/plume motion, hit stops, camera shake, sparks, damage numbers, splash crowns, rings and per-fragment water impacts

## Tags

- melee-combat
- action
- 3d
- threejs
- browser-game
- procedural-generation
- fantasy
- single-player

## Controls

- Mobile controls: Supported
- Motion controls: Not established
- Gamepad: Not established
- Keyboard/mouse: Supported

## Player modes

- Human players: 1
- Modes: single-player

## Technologies

- **Three.js 0.180.0** — engine ([evidence](https://github.com/adamholter/shallow-steel/blob/main/package.json))
- **JavaScript** — language ([evidence](https://api.github.com/repos/adamholter/shallow-steel/languages))
- **WebGL** — rendering ([evidence](https://github.com/adamholter/shallow-steel/blob/main/src/main.js))
- **Canvas 2D** — rendering ([evidence](https://github.com/adamholter/shallow-steel/blob/main/src/hud.js))
- **Web Audio API** — audio ([evidence](https://github.com/adamholter/shallow-steel/blob/main/src/audio.js))
- **Vite 7.3.6** — build ([evidence](https://github.com/adamholter/shallow-steel/blob/main/package.json))

## Reconstructed prompt

Create a playable browser 3D melee combat gym inspired by the Troubled Passage combat clip: a silver knight with navy cloth and plume fighting skeleton shield fighters, a captain and an axe fighter in shallow turquoise water with barrels, crates, jars, tables and chairs. Implement an oblique following camera, WASD movement, mouse-drag directional greatsword/one-handed strikes, timed parry with riposte, hold guard, stamina, i-frame evade, weapon switching, shield pickup, three trials of 3/4/5 skeletons, destructible props with splash/particle impacts, Canvas HUD with portrait/health/stamina/minimap, touch stick and buttons, synthesized Web Audio effects, and local Vite dev launch.

## Source evidence

- Repository is a public game repo named shallow-steel, described as 'Open-source Three.js combat recreation inspired by Troubled Passage', with browser-game/game/threejs topics, JavaScript language, MIT license, 1 commit, 0 stars/forks. ([source](https://api.github.com/repos/adamholter/shallow-steel))
- README defines the game as a playable AI recreation of the Troubled Passage combat gym: oblique following camera, silver knight vs skeleton shield fighters, hat-wearing captain and axe fighter in a shallow-water gym, with three trials of 3, 4 and 5 skeletons and partial healing between trials. ([source](https://github.com/adamholter/shallow-steel/blob/main/README.md))
- README Play section documents keyboard/mouse controls: WASD/arrows move, click/drag directional strikes, J/I/U strikes, RMB/K parry and hold-to-guard, Space/L evade, Q weapon switch, F shield pickup, Escape pause, R restart. ([source](https://github.com/adamholter/shallow-steel/blob/main/README.md))
- README and index.html document touch controls: movement stick plus strike, parry, evade and weapon buttons; QA reports CDP touch-event joystick movement and touch strike/weapon/evade checks passing. ([source](https://github.com/adamholter/shallow-steel/blob/main/README.md))
- Combat model documented with windup/active/recovery timings per weapon, 190 ms timed parry, sustained guard, stamina, ripostes, shield stagger, invulnerable evades, enemy scheduling, collision/knockback, and destructible barrels/crates/jars/tables. ([source](https://github.com/adamholter/shallow-steel/blob/main/README.md))
- Run path is local-only: \`npm run dev\` then open http://localhost:9411; repo has\_pages is false with no deployments, so no publicly reachable playable URL is established. ([source](https://github.com/adamholter/shallow-steel/blob/main/README.md))
- package.json pins Three.js 0.180.0 runtime dependency with Vite 7.3.6 and Playwright dev dependencies; src/main.js creates a THREE.WebGLRenderer with shadows/ACES tone mapping, hud.js draws HUD on Canvas 2D, audio.js synthesizes effects via AudioContext oscillators with no samples. ([source](https://github.com/adamholter/shallow-steel/blob/main/package.json))
- No gameplay screenshots or video files are committed: recursive file tree lists only docs, index.html, package files, scripts/\*.mjs and src/\*.js with no images; QA-referenced evidence/\*.png and demo MP4 are not present in the tree, so no gameplay frame could be inspected. ([source](https://api.github.com/repos/adamholter/shallow-steel/git/trees/main?recursive=1))
- README explicitly attributes creation to GPT-6 Astra for game code, models, animations, materials, textures, effects and sound, and states reference footage is never loaded by the game; no playable browser/macOS build of the original gym was available to the author. ([source](https://github.com/adamholter/shallow-steel/blob/main/README.md))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 82/100: The parry-riposte read finally clicked in trial two and the whole gym felt electric — weighty cleaves, splashes everywhere, debris bouncing off the water.
- 58/100: Clever combat skeleton with real timing skill, but one arena and three trials run thin fast, and I never got to see it running myself.
- 45/100: Promising study with sharp timing numbers on paper; without a live build or screenshots to judge, it feels like a sparring drill waiting for a game around it.

## Links

- [Source repository](https://github.com/adamholter/shallow-steel)
- [Reference: Troubled Passage on Steam](https://store.steampowered.com/app/1796660/Troubled_Passage/)
