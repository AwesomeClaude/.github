# ClaudeJump

[Play the game](https://claudejump.netlify.app) · [View source](https://github.com/PrabhjotSodhi/ClaudeJump)

| Overall rating | Screenshot score |
| :---: | :---: |
| **42/100** | **Not scored** |

<details>
<summary>Read the scoring rationale</summary>

### Overall rating

Far from AAA: one small arena, two modes, no audio, no online play, no campaign or live-ops scale. Calibrated against the full catalog: most relevant comparators are hypeJumper (36, Celeste-grade platformer tech but no browser play and sketch-only visuals), Ballz (40, complete single-loop arcade game), Turbo Kart Rally (40, complete 3D kart loop with AI field and inspected screenshots), SpaceHo2 (42, complete browser strategy loop), and Neon Arena (48, far broader roguelite systems with co-op but zero inspectable pixels). ClaudeJump sits around 42: it beats hypeJumper on shipped browser play, a verified live URL, real local 2-player Versus with gamepads, five working cards, sudden death, title/select/pause/results screens, and a tested deterministic engine, but it trails Neon Arena badly on systems breadth and trails Kart Royale (50) and OSRS Tower Defense (52) on scope, content volume, and verified visual polish. Evidence gaps: no inspectable gameplay screenshots (repo ships zero image files), Survival sub-systems and audio are still open tickets, and source files do not prove playability, performance, or balance.

### Screenshot score

No inspectable gameplay screenshot.

</details>

## At a glance

| Detail | Value |
| --- | --- |
| Repository created | 26 Sep 2026 · 10:58 UTC |
| Added to catalog | 27 Sep 2026 · 06:11 UTC |
| Last updated | 27 Sep 2026 · 06:11 UTC |
| Documented creation models | [Opus 5.5](https://github.com/PrabhjotSodhi/ClaudeJump/blob/main/README.md), [Sonnet 5](https://github.com/PrabhjotSodhi/ClaudeJump/blob/main/README.md) |

## Play

- Open https://claudejump.netlify.app in a modern desktop browser
- Pick Versus to knock your friend into the sea, or Survival to climb as high as you can
- Red moves with A/D and jumps with W; Blue moves with Left/Right arrows and jumps with Up
- Grab falling crates to collect card power-ups (dash, rocket, bounce pad, fire floor, ice floor) and play them to knock the opponent into the sea
- Win rounds first to 5; after 30 seconds sudden death raises the sea — last one out of the water wins the round

## Mechanics

- Versus knockback arena: bump, stomp, and card knockback push the rival into the sea
- Double jump plus floaty in-air and grippy grounded movement tuning
- Screen wrap on left and right edges with a puff marker where the player reappears
- Falling supply crates that grant one held card per player (dash, rocket, bounce pad, fire floor, ice floor)
- Card powers: dash burst, rocket projectile with blast knockback, bounce pad, burning and freezing platforms
- Sudden death: the sea rises after 30 seconds until it reaches the middle platform
- First-to-5 match structure with ready/go countdowns, match results screen, and most-stomps badge
- Survival climbing mode against rockets and crabs (partially built; climbing camera, difficulty ramp, and score tickets still open)
- Title, player-select join cards, pause menu, player color tags, and held-card icons
- Deterministic fixed 60-tick-per-second simulation with seeded randomness for replay and future online play

## Tags

- platformer
- arena-battler
- versus
- local-multiplayer
- pixel-art
- browser-game
- single-player
- power-ups
- 2d
- vanilla-js

## Controls

- Mobile controls: Not established
- Motion controls: Not established
- Gamepad: Supported
- Keyboard/mouse: Supported

## Player modes

- Human players: 1–2
- Modes: single-player, local multiplayer

## Technologies

- **JavaScript** — language ([evidence](https://github.com/PrabhjotSodhi/ClaudeJump/blob/main/AGENTS.md))
- **HTML5 Canvas** — rendering ([evidence](https://github.com/PrabhjotSodhi/ClaudeJump/blob/main/AGENTS.md))
- **WebGL** — rendering ([evidence](https://github.com/PrabhjotSodhi/ClaudeJump/blob/main/AGENTS.md))

## Reconstructed prompt

Create ClaudeJump, a pixel-art browser platform battler in plain JavaScript with Canvas 2D plus one WebGL composite pass, no build step: local 2-player Versus (stomp, bump, knockback, double jump, screen wrap, falling card crates with dash/rocket/bounce-pad/fire/ice, sudden-death rising sea, first to 5 wins) plus a Survival climbing mode, title/player-select/pause/results screens, keyboard and gamepad input, deterministic 60-tick simulation with seeded randomness, pixel HUD and effects, and a Netlify static deploy.

## Source evidence

- GitHub API identifies the repo as PrabhjotSodhi/ClaudeJump, public, JavaScript primary language with GLSL and HTML, MIT license, created 2026-09-26, 0 stars, 0 forks, no homepage set. ([source](https://github.com/PrabhjotSodhi/ClaudeJump))
- README defines the game as a pixel-art browser platformer: knock your friend into the sea in Versus, or climb as high as you can in Survival, with a Play now link to the Netlify build. ([source](https://github.com/PrabhjotSodhi/ClaudeJump/blob/main/README.md))
- README attributes construction to Claude: Opus 5.5 plans and reviews every ticket, Sonnet 5 writes the code, with full history in issues and pull requests. ([source](https://github.com/PrabhjotSodhi/ClaudeJump/blob/main/README.md))
- README controls table establishes keyboard play: Red moves with A/D and jumps with W; Blue moves with arrow keys and jumps with Up. ([source](https://github.com/PrabhjotSodhi/ClaudeJump/blob/main/README.md))
- AGENTS.md states two players share one keyboard in Versus and knock each other into the sea with cards, while one player climbs in Survival against rockets and crabs — establishing local multiplayer plus single-player. ([source](https://github.com/PrabhjotSodhi/ClaudeJump/blob/main/AGENTS.md))
- AGENTS.md describes the tech: plain JavaScript with 2D canvas drawing plus one WebGL shader pass, no build step, 320x180 layers scaled by whole numbers, fixed 60-tick deterministic simulation with seeded randomness. ([source](https://github.com/PrabhjotSodhi/ClaudeJump/blob/main/AGENTS.md))
- key-mappings.json confirms two keyboard player mappings (red: KeyA/KeyD/KeyW/KeyS/KeyC/Escape; blue: arrows/KeyS-equivalent/Comma/Escape), supporting keyboard controls for two humans. ([source](https://github.com/PrabhjotSodhi/ClaudeJump/blob/main/data/config/key-mappings.json))
- gamepad-input.js implements full gamepad mapping (stick move, A jump, B card, Start pause, D-pad) assigned per browser slot to each player id — establishing gamepad support. ([source](https://github.com/PrabhjotSodhi/ClaudeJump/blob/main/src/engine/gamepad-input.js))
- main.js wires keyboard plus gamepad inputs together, starts on a title scene, and renders layered canvases through a shader window — establishing keyboard and gamepad as live inputs. ([source](https://github.com/PrabhjotSodhi/ClaudeJump/blob/main/src/main.js))
- index.html is a static page with a single canvas and a module script loading src/main.js, with a mobile viewport tag but no touch controls — touch support is unestablished. ([source](https://github.com/PrabhjotSodhi/ClaudeJump/blob/main/index.html))
- netlify.toml builds a static dist from index.html, src, and data and the deployed site returns HTTP 200 with the game shell, verifying the play URL opens the game rather than a repo or promo page. ([source](https://claudejump.netlify.app))
- Issue tracker shows closed gameplay tickets (double jump, stomp, bump, knockback, screen wrap, sudden death, dash/rocket/bounce/fire/ice cards, crates, title, player select, pause, results, gamepads) and open gaps (sound effects and music, online Versus, Survival climbing camera/score/crabs/rockets, sprites and platform art), bounding verified scope. ([source](https://github.com/PrabhjotSodhi/ClaudeJump/issues))
- Recursive repo tree lists 83 files with no PNG/JPG/GIF assets — all art is procedural — so no gameplay screenshot could be inspected and none is claimed. ([source](https://github.com/PrabhjotSodhi/ClaudeJump/tree/main/src))
- Catalog search for claudejump/PrabhjotSodhi across games/ found no prior entry, and no catalog game references this repository or play URL, so no existing slug is reused. ([source](https://github.com/PrabhjotSodhi/ClaudeJump))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 78/100: Fictional illustrative review: sudden-death Versus with a friend is pure chaos — stomping them into the rising sea after stealing a rocket crate never gets old.
- 55/100: Fictional illustrative review: the knockback duels are fun for a few rounds, but the plain pixel arenas and missing sound make it feel like a solid jam prototype rather than a finished game.
- 100/100: Fictional illustrative review: a perfect tiny arena game — deterministic netcode-ready engine, great cards, gamepad support, and instant browser play make this the ideal couch-duel snack.

## Links

- [Source repository](https://github.com/PrabhjotSodhi/ClaudeJump)
- [Play the game](https://claudejump.netlify.app)
