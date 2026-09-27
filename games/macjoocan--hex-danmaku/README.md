# HEX DANMAKU

[Open the game source](https://github.com/macjoocan/hex-danmaku)
**Repository created:** 2026-08-19T16:05:10Z
**Added to catalog:** 2026-09-27T04:42:36.648365+00:00
**Updated in catalog:** 2026-09-27T04:42:36.648365+00:00

**Overall rating:** 48/100. Far from AAA: no voice, cinematics, multiplayer, proven audio, or device-verified performance, and pipeline notes leave numeric fun targets and late balance unverified. Most relevant comparators: OSRS Tower Defense (52, denser 2D TD with 12 towers/61 monsters/130 waves and 65 screenshot score), Ashlands (55, catalog top on paper breadth but zero inspectable screenshots), Kart Royale (50, complete 3D kart loop with 70 screenshots), THORNMERE (46, full retro RPG with 60 screenshots), and Taipo (35, single-map typing TD at 55 screenshots). Hex Danmaku exceeds Taipo, Blackjack (28), and Beachy (25) on depth and scope with 24 stages plus a 5-room hunt, daily/endless/editor modes, seeded RNG, and 124+ headless tests, and its inspected mobile boss frame is more polished than Taipo. It sits below OSRS TD and Ashlands on systems breadth, test scale, and content volume, and below the catalog 70s on 3D lighting and scene density, landing beside Frosty Tactics/Neon Arena (48) as a complete polished indie tactics loop. Source and stills do not prove playability, performance, or balance.

**Screenshot score:** 60/100. Both gameplay frames are the game's own output: coherent cute-chibi fantasy styling, readable hex composition, detailed hero/dragon sprites, clear teal/coral telegraph language, and complete HUD/skill UI across mobile and dark-HUD skins. Against catalog calibration this sits with THORNMERE (60, deliberate textured retro scene with portrait) and just above Taipo (55, sparser flat pixel TD board), below OSRS Tower Defense (65, denser varied 2D battlefield) and far below Kart Royale/Turbo Kart Rally/Neural Sight (70, dense 3D or photographic scenes with lighting and depth). Flat mint tiles, simple dot bullets, and shared boss art cap it. Menu frame discounted as non-gameplay. Stills prove nothing about motion, feel, performance, or balance.

## Screenshots

![Inspected downloaded copy of fantasy-game-slash-mobile.png: vertical mobile gameplay frame of STAGE 06 boss versus dragon. Mint hex board with teal reachable tiles and pink/hatched danger telegraphs, chibi sword hero with slash arc, detailed dragon boss, small red bullet dots, PHASE 1 banner, turn/score/combo HUD, next-spawn trays, and three skill cards (time rewind, rune slash, frost magic) with Q/E/A/D/Z/X/SPC/R hints. Clearly the game's own runtime output.](https://raw.githubusercontent.com/macjoocan/hex-danmaku/main/art-review/fantasy-game-slash-mobile.png)

Inspected downloaded copy of fantasy-game-slash-mobile.png: vertical mobile gameplay frame of STAGE 06 boss versus dragon. Mint hex board with teal reachable tiles and pink/hatched danger telegraphs, chibi sword hero with slash arc, detailed dragon boss, small red bullet dots, PHASE 1 banner, turn/score/combo HUD, next-spawn trays, and three skill cards (time rewind, rune slash, frost magic) with Q/E/A/D/Z/X/SPC/R hints. Clearly the game's own runtime output.

![Inspected downloaded copy of hud-stage.png: dark-fantasy STAGE 01 gameplay frame with Lv.1 hero portrait, 6/6 HP and EXP bars, next-bullet trays, forest-backed hex board with teal move range around the hero and one purple enemy, and three bottom skill buttons with coin costs. Clearly the game's own runtime output in an alternate HUD skin.](https://raw.githubusercontent.com/macjoocan/hex-danmaku/main/art-review/hud-stage.png)

Inspected downloaded copy of hud-stage.png: dark-fantasy STAGE 01 gameplay frame with Lv.1 hero portrait, 6/6 HP and EXP bars, next-bullet trays, forest-backed hex board with teal move range around the hero and one purple enemy, and three bottom skill buttons with coin costs. Clearly the game's own runtime output in an alternate HUD skin.

![Inspected downloaded copy of fantasy-menu-desktop.png: desktop title/menu screen with HEX DANMAKU logo, floating-island key art, chibi hero and dragon, and mode cards for stages, endless, daily challenge, and preparation. Menu/title art, not active gameplay; discounted for graphics scoring.](https://raw.githubusercontent.com/macjoocan/hex-danmaku/main/art-review/fantasy-menu-desktop.png)

Inspected downloaded copy of fantasy-menu-desktop.png: desktop title/menu screen with HEX DANMAKU logo, floating-island key art, chibi hero and dragon, and mode cards for stages, endless, daily challenge, and preparation. Menu/title art, not active gameplay; discounted for graphics scoring.

## Play

- Serve the folder over http (for example \`npx serve .\`) and open \`Hex Danmaku.html\`, or run \`npm run dev\` and open the printed preview URL.
- Pick a mode from the menu: classic 24-stage run, 5-room Sanctuary Expedition hunt, daily challenge, endless, or stage editor.
- Each turn move to an adjacent hex by tapping/clicking a highlighted cell or pressing Q/E/A/D/Z/X and arrows; tap the hero cell or press Space to wait.
- Read pink/hatched telegraphs and bullet previews, then dodge; in hunt rooms your hero auto-slashes adjacent monsters after every move or wait.
- Spend coins on skills: Time Rewind (undo), Rune Slash (bomb), Frost Magic (freeze); collect gems, XP, and pick 1-of-3 relics to survive all rooms or stages.

## Mechanics

- Turn-based movement on a 7x11 odd-r hex grid where every move or wait advances one turn
- Action-triggered enemy danmaku with one-turn direction locks and next-position previews
- Safe-move (teal) versus danger (coral/hatched) tile telegraphing and graze/dash play
- Three coin-cost skills: time rewind (undo), rune slash bomb clearing bullets, freeze stopping movement and cooldowns
- Classic 24-stage campaign across portal, collect, survive, and boss rule sets
- Sanctuary Expedition hunt: 5 rooms, 9 monsters, auto melee, XP levels, 1-of-3 relic drafts, per-turn single-hit protection
- Endless mode, daily seeded challenge, regions, achievements, coins, stars, and relic meta progression
- In-browser stage editor with pixel-art mode backed by a central art registry

## Tags

- turn-based
- bullet-hell
- danmaku
- hex-grid
- tactics
- fantasy
- tower-defense-adjacent
- single-player
- 2D
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

- **React 18.3.1** — framework ([evidence](https://raw.githubusercontent.com/macjoocan/hex-danmaku/main/Hex%20Danmaku.html))
- **JavaScript** — language ([evidence](https://api.github.com/repos/macjoocan/hex-danmaku/languages))
- **SVG** — rendering ([evidence](https://raw.githubusercontent.com/macjoocan/hex-danmaku/main/app.jsx))
- **CSS** — rendering ([evidence](https://api.github.com/repos/macjoocan/hex-danmaku/languages))
- **Babel 7.29.0** — build ([evidence](https://raw.githubusercontent.com/macjoocan/hex-danmaku/main/Hex%20Danmaku.html))

## Reconstructed prompt

Build a turn-based hex-grid bullet-hell web game called HEX DANMAKU with no build step using React 18 UMD plus in-browser Babel, a 7x11 hex board with telegraphed safe/danger tiles, 24 stages plus a 5-room monster-hunt RPG mode with XP and relic drafts, undo/bomb/freeze skills, daily seed, editor, and a bright chibi fantasy skin with mobile and desktop HUDs.

## Source evidence

- Public repository macjoocan/hex-danmaku exists, default branch main, language JavaScript, created 2026-08-19, pushed 2026-09-08, no license, no homepage, Pages disabled, no deployments or releases. ([source](https://api.github.com/repos/macjoocan/hex-danmaku))
- README describes HEX DANMAKU as a turn-based hex bullet-hell game in plain React 18 UMD plus Babel-in-browser with no build step, entry point Hex Danmaku.html, engine/stages/resources/sprites/screens/app file map, 24 stage definitions, and RPG hunt with health, auto attacks, enemy HP, XP, and three-choice relic upgrades. ([source](https://raw.githubusercontent.com/macjoocan/hex-danmaku/main/README.md))
- Entry HTML loads React 18.3.1 UMD, React-DOM 18.3.1, and Babel standalone 7.29.0 from CDN, then engine, stages, hunt-engine, art-data, resources, sprites, combat-fx, editor-core, screens, editor, and app scripts. ([source](https://raw.githubusercontent.com/macjoocan/hex-danmaku/main/Hex%20Danmaku.html))
- app.jsx implements hex cell click-to-move, clickable skill buttons, keyboard movement with Q/E/A/D/Z/X plus arrows, Space/S/W wait, and R retry, and footer text explicitly says grid tap moves. ([source](https://raw.githubusercontent.com/macjoocan/hex-danmaku/main/app.jsx))
- Language breakdown is JavaScript, CSS, and HTML; repository contents include engine.jsx, stages.jsx, hunt-engine.js, app.jsx, editor files, tests, assets, art-review, and tools. ([source](https://api.github.com/repos/macjoocan/hex-danmaku/languages))
- HUNT\_DESIGN documents the 5-room Sanctuary Expedition: move/wait turns, hero-first auto slash, archer/mage/dasher/dragon stats and patterns, one-turn attack telegraphs, freeze behavior, rune slash, per-turn one-hit protection, and full-clear victory. ([source](https://raw.githubusercontent.com/macjoocan/hex-danmaku/main/HUNT_DESIGN.md))
- VISUAL\_DESIGN records the fantasy direction: 7x11 hex grid, hero/goblin/dragon PNGs, mint rune tiles, teal safe versus coral danger language, mobile 390px and desktop 1280px HUD rules, and confirmation images hud-390/hud-1280/hud-stage. ([source](https://raw.githubusercontent.com/macjoocan/hex-danmaku/main/VISUAL_DESIGN.md))
- Art-review log confirms fantasy hero/goblin/dragon PNGs, combat FX timing table, desktop and mobile overflow checks, and that combat.html is a non-saving interactive effect preview only. ([source](https://raw.githubusercontent.com/macjoocan/hex-danmaku/main/art-review/README.md))
- Pages API returns 404 and deployments list is empty, so no verified hosted playable build was established; package.json only defines a local preview server and node --test suite. ([source](https://api.github.com/repos/macjoocan/hex-danmaku/pages))
- No existing catalog game matches this repository, playable URL, or explicit project reference; title-only similarity was not used, so catalog\_slug is null. ([source](https://github.com/macjoocan/hex-danmaku))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 85/100: Clever twist on bullet-hell: every step matters on the hex grid, and the telegraphed pink tiles make brutal patterns feel fair. Boss 6 had me hoarding runes for one perfect slash.
- 62/100: Charming chibi knights and dragons, readable tactics, generous undo — but runs blur together and the flat mint board never quite sells the sanctuary fantasy.
- 100/100: The daily hunt is my morning coffee ritual. Five rooms, three relics, one dragon — turn-based danmaku perfection in a browser tab.

## Links

- [Source repository](https://github.com/macjoocan/hex-danmaku)
