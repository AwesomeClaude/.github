# scumm-game

[Play the game](https://binrick.github.io/scumm-game/) · [View source](https://github.com/binRick/scumm-game)

| Overall rating | Screenshot score |
| :---: | :---: |
| **38/100** | **62/100** |

<details>
<summary>Read the scoring rationale</summary>

### Overall rating

Far from AAA (two demo rooms, a handful of hotspots, no documented win state, NPC follow-only AI, no voice/cinematics/multiplayer; judged from repo docs, raw data files, and stills only, with no live playthrough, so balance, pacing, and performance are unverified). Most relevant comparators: THORNMERE (46 overall, full retro RPG campaign with 57 monsters/84 spells/town plus 3 dungeons) and The Nine Lives of Ash (47, deep deckbuilder rules core) both exceed it clearly on gameplay depth, scope, and content volume; neverquest (45, deep systems breadth in text UI) also exceeds it on systems. Closest peers are Taipo (35, complete single-loop typing-TD on one tilemap), T-Rex Runner (35, single endless mechanic), and TypeScript-Blackjack (28, rules-faithful single-table game): scumm-game matches or beats them on technical execution (single-file C engine, Dijkstra visibility-graph pathing, ear-clipped walk-behinds, y-scaled sprites, WASM web build, live polygon/sprite editors) and on visual polish of its best frame, but trails Taipo/Blackjack on finished-loop completeness since it is an engine demo with tip-the-butler micro-interactions rather than a full game arc. Above Beachy Beachy Ball (25, single ball-roller) and curiositY (18, static riddle pages) on engine depth and interactivity. Evidence gaps: gh CLI unavailable without auth so GitHub REST/raw endpoints used instead; screenshots and docs do not prove playability, performance, or balance.

### Screenshot score

Best frame shows a coherent, polished pixel-art night dock: huge dithered moon, star field, lit stone arch, ship rigging, moonlit water reflection, wooden dock planks, barrels/rope/shells, Guybrush sprite, and a Look at/Use verb bar. Composition and lighting exceed Taipo (55, sparser flat TD board), TypeScript-Blackjack (35) and Beachy Beachy Ball (35) flat presentations, and sit near THORNMERE (60, textured dungeon/street frames with portraits) and below OSRS Tower Defense (65, dense HUD-heavy action board) and the catalog 70s (Kart Royale, Turbo Kart Rally, Neural Sight) with 3D/photographic depth. Second and third images are bare background assets with no actor or UI and are discounted. Judged from stills only; no motion or gameplay feel inferred.

</details>

## At a glance

| Detail | Value |
| --- | --- |
| Repository created | 20 Apr 2026 · 20:30 UTC |
| Added to catalog | 27 Sep 2026 · 04:41 UTC |
| Last updated | 27 Sep 2026 · 04:41 UTC |
| Documented creation models | Not established |

## Screenshots

![Inspected 1920px gameplay frame: moonlit pixel-art dock with stone arch, lamps, ship, moonlit water, wooden planks, Guybrush-style actor center, gold debug marker right, bottom verb bar with highlighted 'Look at', 'Use', and hint text 'Click a verb, click an object, click floor to walk. \[D\] overlay \[E\] edit walkbox \[B\] sprite browser'. Clearly the game's own runtime output; sharpest and most detailed frame.](https://raw.githubusercontent.com/binRick/scumm-game/main/docs/screenshot.png)

Inspected 1920px gameplay frame: moonlit pixel-art dock with stone arch, lamps, ship, moonlit water, wooden planks, Guybrush-style actor center, gold debug marker right, bottom verb bar with highlighted 'Look at', 'Use', and hint text 'Click a verb, click an object, click floor to walk. \[D\] overlay \[E\] edit walkbox \[B\] sprite browser'. Clearly the game's own runtime output; sharpest and most detailed frame.

![Inspected background asset games/monkey1/bg.png: same moonlit dock pixel art without actor, verb bar, or markers. Backdrop image only, not a full gameplay capture; confirms the art source for the gameplay frame.](https://raw.githubusercontent.com/binRick/scumm-game/main/games/monkey1/bg.png)

Inspected background asset games/monkey1/bg.png: same moonlit dock pixel art without actor, verb bar, or markers. Backdrop image only, not a full gameplay capture; confirms the art source for the gameplay frame.

![Inspected background asset games/dumb-and-dumber/bg.png: flat daytime pixel-art mansion with red limo, red-carpet steps, uniformed figures, garlands, and snow. No actor, verb bar, or HUD visible; backdrop asset for the second world, not active gameplay.](https://raw.githubusercontent.com/binRick/scumm-game/main/games/dumb-and-dumber/bg.png)

Inspected background asset games/dumb-and-dumber/bg.png: flat daytime pixel-art mansion with red limo, red-carpet steps, uniformed figures, garlands, and snow. No actor, verb bar, or HUD visible; backdrop asset for the second world, not active gameplay.

## Play

- Open the playable web build at https://binrick.github.io/scumm-game/ (canvas + index.js/wasm build in docs/) with mouse and keyboard.
- Pick a world from the SELECT GAME overlay (games/monkey1 dock or games/dumb-and-dumber); Esc or G dismisses or reopens the menu.
- Click a verb (Look at / Use / Pick up / Give), then click a hotspot, inventory item, or floor point to walk there and resolve.
- Click floor to click-to-walk; the actor paths via Dijkstra over the walkbox visibility graph and idles on frame 0 when stopped.
- Press D for the walkbox/foreground debug overlay, E for the walkbox/foreground editor (W/F/H/K/N/Bksp/O/R/S), B for the sprite browser, G for the games menu.

## Mechanics

- Click-to-walk actor with Dijkstra pathing over walkbox/hole visibility-graph polygons
- Classic SCUMM-style verb bar: Look at / Use / Pick up / Give against hotspots and inventory
- Walk-behind foreground polygons rendered over the actor via ear-clipping triangulation
- Perspective sprite scaling by y with 8fps four-direction walk cycles and idle facing
- Rect hotspots with per-verb text, Give-to-tip flow, and $100-bill inventory consumption
- NPC follower actors that chase the player via the same pathfinder
- Two self-contained worlds (monkey1 dock, dumb-and-dumber) with walkbox/hole/scale/layout data
- Live in-game editors: walkbox/foreground/hole polygon editing, scale-line editor, sprite browser

## Tags

- point-and-click
- adventure
- scumm-like
- pixel-art
- retro
- engine
- single-player
- browser-game
- desktop-game

## Controls

- Mobile controls: Not established
- Motion controls: Not established
- Gamepad: Not established
- Keyboard/mouse: Supported

## Player modes

- Human players: 1
- Modes: single-player

## Technologies

- **C** — language ([evidence](https://api.github.com/repos/binRick/scumm-game/languages))
- **raylib 5.5** — framework ([evidence](https://raw.githubusercontent.com/binRick/scumm-game/main/CLAUDE.md))
- **Emscripten** — build ([evidence](https://raw.githubusercontent.com/binRick/scumm-game/main/build_web.sh))

## Reconstructed prompt

Build a tiny SCUMM-style point-and-click adventure engine in C with raylib: click-to-walk actor with Dijkstra pathing over walkbox/hole polygons, 8fps four-direction sprites with perspective y-scaling, Look at/Use/Pick up/Give verb bar, rect hotspots with per-verb text, inventory with tipping, NPC followers, walk-behind foregrounds via ear-clipping, live in-game walkbox/foreground/scale editors plus a sprite browser, two demo worlds (a moonlit Monkey Island dock and a snowy Dumb-and-Dumber entrance), all data in plain text, compiled to a desktop binary and an Emscripten web build served from docs/.

## Source evidence

- Repo binRick/scumm-game is public, created 2026-04-20, pushed 2026-04-24, primary language C, 0 stars/0 forks, default branch main, has\_pages true. ([source](https://api.github.com/repos/binRick/scumm-game))
- Repo root lists README.md, CLAUDE.md, Makefile, build\_web.sh, docs/, games/, guybrush\_sprites\_v3/; docs/ holds index.html/index.js/index.wasm/index.data plus screenshot.png. ([source](https://api.github.com/repos/binRick/scumm-game/contents/))
- README defines a tiny SCUMM-style point-and-click adventure engine in C with raylib: one dock room, click-to-walk Guybrush via Dijkstra over walkbox visibility graph, 8fps four-direction sprites, Look at/Use/Pick up verb bar, walk-behind foregrounds via ear-clipping, live walkbox/foreground editors, sprite browser. Explicitly not a SCUMM bytecode VM. ([source](https://raw.githubusercontent.com/binRick/scumm-game/main/README.md))
- CLAUDE.md documents multi-game structure under games/\<name\>/ (startup games/monkey1), NPC followers chasing the player, inventory/hotspot formats, scale/layout auto-scaling, and full key cheat sheet (click verbs/floor; D/E/B/G editors). ([source](https://raw.githubusercontent.com/binRick/scumm-game/main/CLAUDE.md))
- games/ contains exactly two worlds: monkey1 (dock with Guybrush, bg.png ~904KB, walkbox/fg/holes/scale/layout) and dumb-and-dumber (bg.png, hotspots, inventory, npcs). ([source](https://api.github.com/repos/binRick/scumm-game/contents/games?ref=main))
- dumb-and-dumber hotspots define Butler (left/right) and Doorman interactions; inventory holds five $100 bill lines; npcs.txt places follower 'harry 500 420 down'. ([source](https://raw.githubusercontent.com/binRick/scumm-game/main/games/dumb-and-dumber/hotspots.txt))
- Web build shell is an Emscripten canvas page (960x660 canvas, Module, index.js) and build\_web.sh compiles src/main.c with emcc plus USE\_GLFW=3/ASYNCIFY, preloading games and sprites into docs/. ([source](https://raw.githubusercontent.com/binRick/scumm-game/main/docs/index.html))
- Pages-style playable build at binrick.github.io/scumm-game/ responds with the scumm-game canvas app title. ([source](https://binrick.github.io/scumm-game/))
- Language breakdown is C (~82KB) plus Shell, HTML, Makefile; Makefile builds src/main.c with clang against raylib. ([source](https://api.github.com/repos/binRick/scumm-game/languages))
- No GitHub Pages API site record (404) but docs/ web bundle plus has\_pages true corroborate the hosted playable build; no AI creation-model attribution found in inspected docs. ([source](https://api.github.com/repos/binRick/scumm-game/pages))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 72/100: Fictional illustrative review one: clicked Look at, watched Guybrush route around the dock posts under a huge pixel moon, and tipped a butler in the snow room. Tiny, but it really feels like 1990.
- 55/100: Fictional illustrative review two: lovely moonlit dock and clever walkbox pathing, yet only two rooms and a handful of hotspots, so the verbs run out fast.
- 100/100: Fictional illustrative review three: a single-file C engine with Dijkstra walkboxes, ear-clipped walk-behinds, and a live in-game polygon editor? As retro tech craft this is a joy.

## Links

- [Source repository](https://github.com/binRick/scumm-game)
- [Playable web build](https://binrick.github.io/scumm-game/)
