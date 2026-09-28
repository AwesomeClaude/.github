# Tea Rush — Kitchen Core

[Play the game](https://kpkrr.github.io/tea-game/) · [View source](https://github.com/kpkrr/tea-game)

| Overall rating | Screenshot score |
| :---: | :---: |
| **38/100** | **Not scored** |

<details>
<summary>Read the scoring rationale</summary>

### Overall rating

Far from AAA (grey-box programmer art, no audio, animation, multiplayer, or live-ops evidence). Most relevant comparators: Pizza Chef (44, broader cooking systems with customers/power-ups/bosses/economy but unverified visuals), neverquest (45, deepest catalog systems scope but monochrome text UI), Turbo Kart Rally (40, complete indie 3D loop with HUD/AI), 2048 (38, complete minimal loop), and Taipo (35, complete niche loop with real pixel art). Tea Rush sits at 38: a genuinely complete, tuned, playable time-management loop with pathfinding, brew timers, slot multitasking, difficulty ramp, register meta, boosts, and bilingual guide exceeds Blackjack (28) and T-Rex Runner (35) on systems depth, but trails Pizza Chef and Turbo Kart Rally because its visuals are explicitly grey boxes plus debug HUD with no art pass, and trails neverquest badly on scope. Evidence gaps: gh api was unusable (no auth plus rate limits), so evidence came from repository pages and raw files; the web build shell was verified but the game was not played, so playability, performance, balance, and mobile feel are judged from code and docs only.

### Screenshot score

No inspectable gameplay screenshot.

</details>

## At a glance

| Detail | Value |
| --- | --- |
| Repository created | 26 Sep 2026 · 14:33 UTC |
| Added to catalog | 27 Sep 2026 · 06:26 UTC |
| Last updated | 27 Sep 2026 · 06:26 UTC |
| Documented creation models | Not established |

## Screenshots

![Tea Rush — Kitchen Core gameplay](screenshots/3cb4495c0b98dfbe4b663cbf2b6836473572339beb66d902367893162a70be0e.png)

Inspected 800x600 PNG at the play-build root: black page with the blue Godot robot head and GODOT / Game engine text. Default engine splash/loading placeholder, not gameplay; shows no kitchen, guests, HUD, or tea-shop scene.

[Original screenshot](https://kpkrr.github.io/tea-game/index.png)

## Play

- Open the playable web build at https://kpkrr.github.io/tea-game/ (Godot web export; desktop mouse click acts as a tap).
- Read the How to play guide on launch (goal, controls, stations, kettles, slots, cash box, points, boosts); reopen it with the ? button, switch language with EN/RU.
- Tap a station to walk the barista there and use it: Cups for an empty cup, Green/Black for leaf, Iced for instant iced tea, 100-degree kettle for black tea, 80-degree kettle for green tea, Lemon for brewed tea, Trash to discard.
- For brewed teas, bring a cup with leaf to the correct kettle; brewing runs a background timer while hands are free, then tap again to collect (or swap in a new leaf cup in one tap).
- Use the flat counter pads (7 slots) to put down, pick up, or swap cups and work several orders at once; the barista carries one cup at a time.
- Tap a guest to serve the exact held recipe before their green-to-red patience bar empties; faster serves earn more points.
- Survive the escalating guest flow; the round ends after 3 guests leave unserved. Coins feed the visible daily cash box; when full, finish the round for points and the shop closes until tomorrow (New day test resets it).

## Mechanics

- Tap-to-station movement with AStarGrid2D pathfinding, aisle-centre weighting, line-of-sight smoothing, and tap-to-cancel retargeting
- Step-ordered drink assembly across 5 recipes in 3 price tiers (iced 2 coins, black/green 5, lemon variants 9)
- Background kettle brewing timers with one-tap take-and-replace swap and wait-at-kettle behavior
- Single-cup hands plus 7 counter slots for put down, pick up, and swap multitasking
- Linear difficulty ramp to 3:00 (guest flow 8 to 18 per minute, patience 50s to 25s, complex share 0 to 40 percent)
- Three-strikes round end (3 guests lost) with elapsed time, served count, coins, and points summary
- Skill-scored points (price x 10 x remaining-patience share) with persistent best score
- Daily cash-box register with capacity levels 250/350/500/700 persisting across rounds until reset
- Mid-round boost panel simulating paid upgrades (register capacity and barista speed x1.0 to x1.5)
- Bilingual EN/RU UI with persisted language choice and full in-game How to play guide

## Tags

- time-management
- cooking
- tea-shop
- arcade
- 3d
- godot
- web
- telegram
- single-player
- prototype

## Controls

- Mobile controls: Supported
- Motion controls: Not established
- Gamepad: Not established
- Keyboard/mouse: Supported

## Player modes

- Human players: 1
- Modes: single-player

## Technologies

- **Godot 4.7** — engine ([evidence](https://github.com/kpkrr/tea-game/blob/main/project.godot))
- **GDScript** — language ([evidence](https://raw.githubusercontent.com/kpkrr/tea-game/main/prototypes/kitchen-core/kitchen_core.gd))
- **GL Compatibility** — rendering ([evidence](https://github.com/kpkrr/tea-game/blob/main/project.godot))

## Reconstructed prompt

Build a Godot 4 portrait time-management prototype called Tea Rush kitchen-core: a tap-controlled 3D tea kitchen with a fixed orthographic camera, AStarGrid2D barista pathfinding, stations for cups/iced/green/black/kettles 100 and 80/lemon/trash plus 7 counter slots, 5 step-ordered recipes in 3 price tiers, background kettle brew timers with swap, guests with patience bars and a 3-strikes round end, linear difficulty ramp to 3:00, coins into a persistent daily cash box with capacity and speed boost levels, skill points with best score, bilingual EN/RU texts, a full How to play guide overlay, and a Web export (no thread support) published to GitHub Pages.

## Source evidence

- Repository root is a Claude Code Game Studios template (49 agents, 74 skills), but it contains a real game prototype: the kitchen-core directory with README, kitchen\_core.gd, kitchen\_core.tscn, and kitchen\_text.gd; the game concept is Tea Rush, a barista tea-shop rush game for Telegram. ([source](https://github.com/kpkrr/tea-game))
- Tea Rush concept (RU+EN): play a barista in a small tea house at rush hour; assemble drinks step by step (leaf, water temperature, extra, cup, serve); complex drinks pay more; round ends after 3 guests leave; ~2-minute rounds; visible cash register daily limit (~5 rounds / ~10 min); coins vs skill points; free-to-play with purchase unlocking coins/leaderboard/upgrades. ([source](https://github.com/kpkrr/tea-game/blob/main/tea-rush-concept.txt))
- kitchen-core prototype README asks whether the tap-to-station 3D-kitchen core is fun (2.5D fixed camera, tap station/guest, 3/4/5-step orders, rising difficulty, round ends after 3 lost guests); documents full tuning: tap redirects barista, one cup at a time, trash resets cup, background brew timers, kettle swap/wait rules, serve-any-matching-guest, 8x11m kitchen with 2x4 island, 7 slots, linear difficulty to 3:00 (8-\>18 guests/min, patience 50-\>25s, complex 0-\>40%), color-coded steps, register base 250 (~3 rounds per playtest), boosts lv0-3, points = price x 10 x patience share, EN/RU guide, and 5 drinks priced 2/5/9. ([source](https://github.com/kpkrr/tea-game/blob/main/prototypes/kitchen-core/README.md))
- Prototype README publishes the web build in the gh-pages branch at https://kpkrr.github.io/tea-game/ with Godot Web export preset instructions (thread support off); fetching that URL returns a Godot web-export shell (canvas + engine loader), confirming a playable build exists at that address. ([source](https://github.com/kpkrr/tea-game/blob/main/prototypes/kitchen-core/README.md))
- kitchen\_core.gd source confirms the implemented loop: TUNING block (walk speed, brew time, prices, ramp, register/speed levels), RECIPES for iced/black/green/lemon variants, tap picking with fat-finger radius, AStarGrid2D grid with clearance weights and line smoothing, kettle states empty/brewing/done, slots put/pick/swap, serve scoring, strikes, register persistence via static vars, HUD/guide/boost UI, EN/RU text, and dev screenshot flag. ([source](https://raw.githubusercontent.com/kpkrr/tea-game/main/prototypes/kitchen-core/kitchen_core.gd))
- kitchen\_text.gd holds all player-facing EN/RU strings: drinks, steps, station signs, brewing/ready labels, HUD/register/boost labels, tap-failure hints, round-over/closed texts, and the full guide body describing goal, controls, orders, stations, menu, kettles, slots, serving, difficulty, coins/register, points, and test boosts. ([source](https://raw.githubusercontent.com/kpkrr/tea-game/main/prototypes/kitchen-core/kitchen_text.gd))
- project.godot sets config/name tea-game, main scene res://prototypes/kitchen-core/kitchen\_core.tscn, features 4.7 plus GL Compatibility, and gl\_compatibility rendering method. ([source](https://github.com/kpkrr/tea-game/blob/main/project.godot))
- Controls evidence: prototype README states tap station/guest to act, tap floor to walk, no queue (new tap redirects), and that desktop mouse works as tap; it targets opening in Telegram on a phone with fast load and ~60 FPS, portrait 540x960 framing; guide text documents tap station/guest/floor controls and one-cup carrying. ([source](https://github.com/kpkrr/tea-game/blob/main/prototypes/kitchen-core/README.md))
- Single-player evidence: one barista, one cup at a time, solo serve loop; no multiplayer, network, or multi-human support appears in the concept, prototype README, or source; src/ holds only .gitkeep/CLAUDE.md (game code lives in prototypes/), and production/ holds only stage.txt. ([source](https://github.com/kpkrr/tea-game/tree/main/prototypes/kitchen-core))
- Inspected the only reachable image at the play-build root (index.png, 800x600): Godot engine splash placeholder, not gameplay; no gameplay screenshots, QA evidence images, or art assets are committed (no image files found in the inspected trees); the source itself states the scene is built from code as grey boxes with an orthographic camera and debug HUD. ([source](https://kpkrr.github.io/tea-game/index.png))
- gh api could not be used: no GH\_TOKEN/GITHUB\_TOKEN auth in the environment and unauthenticated api.github.com requests were rate-limited; evidence was therefore gathered from repository pages and raw file endpoints instead, and no repository dates, stars, or catalog timestamps are asserted. ([source](https://github.com/kpkrr/tea-game))
- Catalog check: local catalog README lists 36 games; no existing entry matches kpkrr/tea-game by repository, playable URL, or project reference (nearest genre comparator is Pizza Chef, a different repo and game), so catalog\_slug is null. ([source](https://github.com/kpkrr/tea-game))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 75/100: Fictional illustrative review one: the lunch-rush squeeze is real — juggling two kettles while a patience bar bleeds out, then swapping a fresh leaf cup for ready tea in one tap, feels like a tiny Overcooked win.
- 55/100: Fictional illustrative review two: the loop works and the difficulty ramp is honest, but grey boxes on grey counters with coloured squares for recipes make every round look like a debug build rather than a tea house.
- 90/100: Fictional illustrative review three: the cash-box daily ritual is the smartest hook here — finishing a round for points after the register fills, then chasing two cheap iced teas versus one nine-coin lemon brew, kept me hitting Play again.

## Links

- [Source repository](https://github.com/kpkrr/tea-game)
- [Playable web build](https://kpkrr.github.io/tea-game/)
- [Prototype README (kitchen-core)](https://github.com/kpkrr/tea-game/blob/main/prototypes/kitchen-core/README.md)
- [Game concept](https://github.com/kpkrr/tea-game/blob/main/tea-rush-concept.txt)
