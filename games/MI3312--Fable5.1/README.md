# LUCID SKY

[View source](https://github.com/MI3312/Fable5.1)

| Overall rating | Screenshot score |
| :---: | :---: |
| **58/100** | **Not scored** |

<details>
<summary>Read the scoring rationale</summary>

### Overall rating

Excluding the target itself, the most relevant comparators are moorestech (64, catalog top: Unity factory sim with ~15,520 commits since 2021, Steam page, official site, and 76/100 inspected screenshots), Ashlands (55, prior scope leader: ~94k-line Three.js RPG with 18 quests and harness, but zero inspectable screenshots), and Wilderness (44, closest voxel comparator: single 192x192 survival world, no screenshots, dead demo, 2 commits). LUCID SKY exceeds Ashlands and Wilderness on documented scope and systems breadth (seeded galaxy plus infinite voxel planets, spaceflight, walkable stations, derelict freighters, survival, crafting, alchemy, fishing/cooking, bases, rovers, rideable creatures, quests, photo mode, and host-authoritative Steam multiplayer across a ~1MB JavaScript tree with 41 commits), so it ranks above Ashlands at 58. It stays below moorestech (64) because visual polish is unverifiable (no committed screenshots, no playable URL, no release, 0 stars, 2-day history), and source/docs alone cannot prove playability, performance, balance, or netcode. Evidence gaps: no frame-rate, audio-quality, gamepad/touch, or human-player-count verification.

### Screenshot score

No inspectable gameplay screenshot.

</details>

## At a glance

| Detail | Value |
| --- | --- |
| Repository created | 25 Sep 2026 · 21:23 UTC |
| Added to catalog | 27 Sep 2026 · 06:18 UTC |
| Last updated | 27 Sep 2026 · 06:18 UTC |
| Documented creation models | Not established |

## Play

- Serve the folder over HTTP (e.g. \`npm start\` serves at http://localhost:8080, or \`python3 -m http.server 8080\`) and open it in a WebGL2 browser; do not open index.html via file:// because ES modules and module workers are blocked.
- Move with WASD, look/steer with the mouse, jump with Space (hold for jetpack), sprint/boost with Shift.
- Use the multi-tool with LMB (mine, collect block, fire, cast/hook/reel), place blocks with RMB, cycle tool mode with Q, select hotbar blocks with 1-9 or wheel.
- Press F for scanner pulse, V for analysis visor (hold LMB on creatures or plants), E to interact, board/exit ship, land, dock, or ride a tamed creature.
- Open inventory, fabrication, alchemy, technology, discoveries and journey with Tab/I, the galaxy map with M, photo mode with P, and pause with Esc.
- For online multiplayer, run the desktop shell (desktop/: npm install, npm start, with Steam running) and host or join via Esc/Multiplayer; in a plain browser, two tabs of the same browser can share a dream via BroadcastChannel local test mode.

## Mechanics

- Procedural galaxy of seeded star systems with 2-5 planets, space stations, asteroid fields, and hyperdrive warp travel on a galaxy map
- Infinite voxel planets in nine biomes streamed in 16x16x128 chunks by Web Workers, with caves, floating islands, rivers, ruins, and dream zones
- First-person survival (health, shield, hazard protection, life support, jetpack) with storms, shelter, sentinels with wanted levels, and hostile fauna
- Multi-tool with Mining Beam, Builder, Boltcaster, Dream Line fishing mode, plus scanner pulse and analysis visor cataloguing
- Block-by-block voxel building with block bag, base computers, teleporters, planters, storage, and dream alchemy fusion with 53 hidden recipes
- Starship flight across atmosphere, orbit, pulse drive, asteroid mining, space combat with nightmare ambushes, planetary landing and docking
- Rideable/tameable procedural creatures with distinct locomotion (striders, hoppers, runners, flying mantas) plus companions
- Roamer rover vehicle with suspension, boost, hops, headlights, and terrain-blasting roof cannon
- Fishing minigame with hook/reel tension and cooking system producing buff dishes, plus angler log and mission contracts
- Missions boards with bounties, surveys, expeditions, cache and supply runs raising Dreamwalker rank; Lucid Path questline to the galactic centre
- Online multiplayer via Steam lobbies with relay P2P (host-authoritative universe, block-edit sync, ~12 snapshots/s, chat/ping/wave) plus same-browser BroadcastChannel test mode
- Photo mode with free camera, time-of-day control, depth of field, film filters, and PNG export; procedural WebAudio music and SFX; GPU post pipeline (SSAO, bloom, god rays, volumetrics)

## Tags

- voxel
- space-exploration
- survival
- sandbox
- crafting
- building
- procedural-generation
- open-world
- 3d
- threejs
- webgl
- browser-game
- single-player
- online-multiplayer
- local-multiplayer
- horror
- fishing
- vehicle

## Controls

- Mobile controls: Not established
- Motion controls: Not established
- Gamepad: Not established
- Keyboard/mouse: Supported

## Player modes

- Human players: Not established
- Modes: single-player, online multiplayer, local multiplayer

## Technologies

- **three.js 0.186.1** — engine ([evidence](https://raw.githubusercontent.com/MI3312/Fable5.1/claude/exciting-goodall-0olbhs/package.json))
- **WebGL2** — rendering ([evidence](https://github.com/MI3312/Fable5.1/blob/claude/exciting-goodall-0olbhs/README.md))
- **JavaScript** — language ([evidence](https://api.github.com/repos/MI3312/Fable5.1/languages))
- **WebAudio** — audio ([evidence](https://github.com/MI3312/Fable5.1/blob/claude/exciting-goodall-0olbhs/README.md))
- **Electron 31.0.0** — framework ([evidence](https://raw.githubusercontent.com/MI3312/Fable5.1/claude/exciting-goodall-0olbhs/desktop/package.json))
- **steamworks.js 0.4.0** — framework ([evidence](https://raw.githubusercontent.com/MI3312/Fable5.1/claude/exciting-goodall-0olbhs/desktop/package.json))
- **esbuild 0.25.0** — build ([evidence](https://raw.githubusercontent.com/MI3312/Fable5.1/claude/exciting-goodall-0olbhs/package.json))

## Reconstructed prompt

Build LUCID SKY, a browser voxel space-exploration dream mixing No Man's Sky with liminal voxel building: a seeded galaxy of star systems with nine-biome infinite voxel planets streamed in chunks by Web Workers; three.js + WebGL2 rendering with SSAO, bloom, god rays, volumetric clouds, sun shadows, and weather/sky events; first-person survival with multi-tool, scanner, sentinels, procedural creatures, hunters, spaceships, walkable stations, derelict freighters, rovers, fishing, cooking, bases, missions, and a galaxy-centre questline; dream-horror liminal zones, voxel building, and item-fusion alchemy; procedural WebAudio music and SFX; single-player plus Steam-relay online multiplayer (Electron shell) and same-browser local test mode; plain ES modules with no build step plus a single-file build tool.

## Source evidence

- Repository is an actual game: API metadata shows public repo MI3312/Fable5.1, language JavaScript, 0 stars/0 forks, created 2026-09-25, pushed 2026-09-27, default branch claude/exciting-goodall-0olbhs, no homepage, no license. gh CLI was unusable without auth (no GH\_TOKEN in runner), so unauthenticated public REST/raw endpoints were used for the same GitHub evidence. ([source](https://api.github.com/repos/MI3312/Fable5.1))
- Repository page identifies the game as LUCID SKY, 'An infinite dream of blocks and stars', a browser game built with three.js + WebGL2 mixing No Man's Sky (procedural galaxy, planets, starships, scanning, survival, crafting, journey to the galactic centre) with dreamlike voxel worlds and block-by-block building; file tree lists css/, desktop/, lib/, src/, tools/, index.html, package files, and 41 commits. ([source](https://github.com/MI3312/Fable5.1))
- Game must be served over HTTP (npm start serves at http://localhost:8080) because browsers block ES modules and module workers on file:// URLs; single-file build via npm run build writes dist/lucid-sky.html; requires a WebGL2 browser with GPU strongly recommended. ([source](https://github.com/MI3312/Fable5.1/blob/claude/exciting-goodall-0olbhs/README.md))
- Recursive file tree (about 70 paths) contains only code, styles, docs, and configs with zero .png/.jpg/.webp/.gif/.mp4 files, and the README embeds no screenshots; therefore no gameplay screenshot can be inspected and screenshot\_based\_score is null. ([source](https://api.github.com/repos/MI3312/Fable5.1/git/trees/claude/exciting-goodall-0olbhs?recursive=1))
- No publicly reachable playable URL exists: API homepage is null, has\_pages is false, deployments list is empty, releases list is empty, and the README only documents local serving (localhost:8080) plus a local single-file build, so play\_game\_url is null. ([source](https://api.github.com/repos/MI3312/Fable5.1))
- Controls table documents WASD move/ship throttle-roll, mouse look/steer, Space jump/jetpack/takeoff/pulse, Shift sprint/boost, LMB use/fire, RMB place block, Q cycle tool, 1-9/wheel hotbar, F scanner, V visor, E interact/board/land/ride, plus G/L/P/R/T/Tab/I/M/F2/Esc keys; input.js implements keyboard/mouse with pointer lock only. This is the evidence for keyboard\_mouse=supported. ([source](https://github.com/MI3312/Fable5.1/blob/claude/exciting-goodall-0olbhs/README.md))
- Input module handles keydown/keyup, mouse buttons/movement/wheel, and pointer lock with no touch, accelerometer/gyroscope, or gamepad handlers; index.html viewport meta alone is a responsive layout, not touch controls. No source explicitly rules these in or out, so mobile\_controls, motion\_controls, and gamepad remain unknown rather than not\_supported. ([source](https://raw.githubusercontent.com/MI3312/Fable5.1/claude/exciting-goodall-0olbhs/src/core/input.js))
- Multiplayer: one player hosts their universe and others join as guests sharing walking, building, flying, driving, and fishing, with host-canonical block edits, ~12 position snapshots/s with interpolation, host time-of-day, chat (Enter), ping (Z), wave (X), name tags, and remote ships/rovers/fishing lines. Online play runs in the desktop Electron shell via Steamworks (app ID 480 Spacewar test app) with friends-only/public lobbies, overlay invites, and Steam Datagram Relay P2P. This is the evidence for online multiplayer mode. ([source](https://github.com/MI3312/Fable5.1/blob/claude/exciting-goodall-0olbhs/README.md))
- Local test mode uses a BroadcastChannel so two tabs of the same browser can share a dream; this is the evidence for local multiplayer on one device. No fixed human-player count is documented anywhere, so human\_players is null. ([source](https://github.com/MI3312/Fable5.1/blob/claude/exciting-goodall-0olbhs/README.md))
- Desktop shell README confirms Electron + steamworks.js Steam lobbies/invites/relay P2P, host-canonical block changes, per-guest character save slots, snapshot/edit sync, and chat/ping/wave social features; native binaries for Windows x64, Linux x64, macOS. ([source](https://github.com/MI3312/Fable5.1/blob/claude/exciting-goodall-0olbhs/desktop/README.md))
- package.json identifies the project as lucid-sky 1.0.0, a procedural voxel space exploration game built with three.js + WebGL, ES modules, with three 0.186.1 and esbuild dev dependencies and http-server start script. ([source](https://raw.githubusercontent.com/MI3312/Fable5.1/claude/exciting-goodall-0olbhs/package.json))
- Language breakdown via API is JavaScript-dominant (~1,025,886 bytes) with CSS (~27,716) and HTML (~980); supports the JavaScript language finding. ([source](https://api.github.com/repos/MI3312/Fable5.1/languages))
- No AI creation models are attributed anywhere in the inspected README, package manifests, or desktop docs, so creation\_models is empty. ([source](https://github.com/MI3312/Fable5.1/blob/claude/exciting-goodall-0olbhs/README.md))
- No existing catalog entry matches this game: full-text search of games/ for 'lucid sky', 'lucid', 'Fable5', and 'MI3312' returns no match, verified against distinct repository identity (not title alone), so catalog\_slug is null. ([source](https://github.com/MI3312/Fable5.1))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 85/100: Fictional illustrative review one: crashed on a lush world, repaired the ship, warped two systems out, then got lost for an hour in a tile-void dream zone while my tamed wildebeest waited by the door. As a browser voxel space dream it swings for the fences.
- 60/100: Fictional illustrative review two: the breadth is staggering on paper - galaxies, freighters, fishing, alchemy, Steam co-op - but with no screenshots or live build to try, this reads as a hugely ambitious prototype awaiting proof of performance and balance.
- 100/100: Fictional illustrative review three: reeling in a Star Koi at dusk while a friend ship burned through the atmosphere overhead and volumetric clouds rolled past the horizon giants - no other catalog game even attempts this scale of dream.

## Links

- [Source repository](https://github.com/MI3312/Fable5.1)
- [Project README](https://github.com/MI3312/Fable5.1/blob/claude/exciting-goodall-0olbhs/README.md)
- [Desktop shell README (Steam multiplayer)](https://github.com/MI3312/Fable5.1/blob/claude/exciting-goodall-0olbhs/desktop/README.md)
