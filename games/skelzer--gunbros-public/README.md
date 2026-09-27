# GunBros

[View source](https://github.com/skelzer/gunbros-public)

| Overall rating | Screenshot score |
| :---: | :---: |
| **57/100** | **68/100** |

<details>
<summary>Read the scoring rationale</summary>

### Overall rating

GunBros shows unusually deep engineering for the catalog: deterministic client-server simulation, authoritative netcode with resync, 18 mobiles, 8 themed maps, items, sky events, bots, and Playwright e2e tests, with polished coherent pixel art (screenshots 68). That scope exceeds Kart Royale (50), OSRS Tower Defense (52) and HEX DANMAKU (48), and approaches Ashlands (55), but it stays well short of moorestech (64), the catalog leader with a live large-scale 3D world. Capped because no public playable deployment exists (example.com placeholder URLs, Coming soon page), so real online play, performance, and balance are unverified from stills and docs alone.

### Screenshot score

Four inspected desktop frames plus one phone frame show coherent chibi pixel art across four distinct biomes with parallax backgrounds, destructible-terrain cross-sections, and a dense complete HUD. Below moorestech (76) and Kart Royale (70), which have richer 3D scenes, but above OSRS Tower Defense (65) and scumm-game (62) peers for art variety and UI completeness. Deducted for the dev debug overlay panel visible in every frame and relatively static single-mobile compositions; stills cannot show motion or game feel.

</details>

## At a glance

| Detail | Value |
| --- | --- |
| Repository created | 25 Sep 2026 · 10:34 UTC |
| Added to catalog | 27 Sep 2026 · 06:04 UTC |
| Last updated | 27 Sep 2026 · 06:04 UTC |
| Documented creation models | [Claude Opus 5.5](https://github.com/skelzer/gunbros-public/blob/main/README.md), [Claude Fable 5.1](https://github.com/skelzer/gunbros-public/blob/main/README.md) |

## Screenshots

![Inspected 800x600 gameplay frame on the temple map: chibi green tank mobile on carved stone temple terrain with vines and statues, parallax pyramids and sun, full HUD with player health bars, turn timer 17, wind dial, YOUR TURN banner, bottom bar with angle gauge, S1/S2/SS shot buttons, power bar, item slots (DUAL, TELE, BAND, BUNGE, PWR), SKIP and FIRE buttons. Debug seed panel at left. Clearly the game's own runtime output.](https://raw.githubusercontent.com/skelzer/gunbros-public/main/docs/ui/maps/temple_desktop.png)

Inspected 800x600 gameplay frame on the temple map: chibi green tank mobile on carved stone temple terrain with vines and statues, parallax pyramids and sun, full HUD with player health bars, turn timer 17, wind dial, YOUR TURN banner, bottom bar with angle gauge, S1/S2/SS shot buttons, power bar, item slots (DUAL, TELE, BAND, BUNGE, PWR), SKIP and FIRE buttons. Debug seed panel at left. Clearly the game's own runtime output.

![Inspected 800x600 gameplay frame on rolling hills: same tank on grassy hill with exposed dirt cross-section, fossil bones, pine trees, mountain backdrop, identical full HUD (timer 18, wind 6 @ 10). Coherent pixel-art style, game's own output.](https://raw.githubusercontent.com/skelzer/gunbros-public/main/docs/ui/maps/hills_desktop.png)

Inspected 800x600 gameplay frame on rolling hills: same tank on grassy hill with exposed dirt cross-section, fossil bones, pine trees, mountain backdrop, identical full HUD (timer 18, wind 6 @ 10). Coherent pixel-art style, game's own output.

![Inspected 800x600 gameplay frame in the crystal cave: purple cavern with stalactites, glowing crystals, wooden scaffolding and mine cart, same HUD (timer 17, wind 17 @ 159). Distinct palette proving multiple hand-built map themes.](https://raw.githubusercontent.com/skelzer/gunbros-public/main/docs/ui/maps/cave_desktop.png)

Inspected 800x600 gameplay frame in the crystal cave: purple cavern with stalactites, glowing crystals, wooden scaffolding and mine cart, same HUD (timer 17, wind 17 @ 159). Distinct palette proving multiple hand-built map themes.

![Inspected 800x600 gameplay frame in the volcanic forge: dark red foundry with lava flows, volcano, furnaces and village silhouettes, same HUD (timer 18, wind 14 @ 31). Fourth distinct biome, game's own output.](https://raw.githubusercontent.com/skelzer/gunbros-public/main/docs/ui/maps/forge_desktop.png)

Inspected 800x600 gameplay frame in the volcanic forge: dark red foundry with lava flows, volcano, furnaces and village silhouettes, same HUD (timer 18, wind 14 @ 31). Fourth distinct biome, game's own output.

![Inspected 800x370 phone-layout gameplay frame in the cave: compressed touch HUD with large FIRE/SKIP keys, angle pad arrows, move arrows, item row and shell selector, confirming the touch-screen control scheme. Game's own output, alternate layout rather than the primary desktop view.](https://raw.githubusercontent.com/skelzer/gunbros-public/main/docs/ui/maps/cave_phone.png)

Inspected 800x370 phone-layout gameplay frame in the cave: compressed touch HUD with large FIRE/SKIP keys, angle pad arrows, move arrows, item row and shell selector, confirming the touch-screen control scheme. Game's own output, alternate layout rather than the primary desktop view.

## Play

- Install and start locally: pnpm install, then pnpm dev (server on :8080, Vite client on :5173).
- Open http://localhost:5173, pick a nickname, and create a room.
- Copy the /r/CODE room link and send it to other players so they can join.
- In the room, pick team, mobile, map and items, ready up, and have the host start (needs at least 2 players across both teams; practice adds a bot).
- On your turn: walk with Left/Right, aim with Up/Down, hold Space to charge the power bar and release to fire, Tab to cycle shots, 1-6 to use items, X to skip.
- Read the wind dial and angle HUD, watch your shell fly, and be the last one standing.

## Mechanics

- Turn-based artillery duels for 2-8 players with delay-based turn ordering
- Charge-and-release power bar with angle aiming and shifting wind
- Fully destructible procedural terrain that changes as blasts carve it
- 18 mobiles across classes, each with S1, S2 and SS shots plus specials
- Consumable item loadout of up to 6 slots (dual, teleport, bandage, bungee, power-up)
- Wind schedule, sky events (Thor, tornado, force), weather and sudden death
- Authoritative server match loop with deterministic shared simulation and resync hashes
- Room codes with lobby, teams, chat, host start, reconnect tokens and bots
- Movement gauge, fall damage rules, shield regen and class-based damage table
- Free camera drag/edge-scroll, sandbox practice route, debug desync panel

## Tags

- artillery
- turn-based
- multiplayer
- online-multiplayer
- browser
- pixel-art
- 2d
- strategy
- destructible-terrain
- tanks

## Controls

- Mobile controls: Supported
- Motion controls: Not established
- Gamepad: Not established
- Keyboard/mouse: Supported

## Player modes

- Human players: 1-8
- Modes: single-player, online multiplayer

## Technologies

- **TypeScript ^5.9.3** — language ([evidence](https://github.com/skelzer/gunbros-public/blob/main/package.json))
- **Canvas 2D** — rendering ([evidence](https://github.com/skelzer/gunbros-public/blob/main/README.md))
- **Vite ^7.1.12** — build ([evidence](https://github.com/skelzer/gunbros-public/blob/main/packages/client/package.json))
- **Node.js \>=22** — framework ([evidence](https://github.com/skelzer/gunbros-public/blob/main/README.md))
- **ws** — framework ([evidence](https://github.com/skelzer/gunbros-public/blob/main/README.md))
- **Web Audio** — audio ([evidence](https://github.com/skelzer/gunbros-public/blob/main/docs/DESIGN.md))
- **Vitest ^3.2.7** — build ([evidence](https://github.com/skelzer/gunbros-public/blob/main/packages/client/package.json))
- **Playwright** — build ([evidence](https://github.com/skelzer/gunbros-public/blob/main/README.md))
- **pnpm 11.11.0** — build ([evidence](https://github.com/skelzer/gunbros-public/blob/main/package.json))
- **Docker** — build ([evidence](https://github.com/skelzer/gunbros-public/blob/main/Dockerfile))
- **Python** — build ([evidence](https://github.com/skelzer/gunbros-public/blob/main/package.json))

## Reconstructed prompt

Build GunBros, a browser-based turn-based 2D artillery game for 2-8 online players: 18 chibi mobiles each with S1/S2/SS shots, 8 hand-painted destructible pixel-art maps, wind, items, sky events and sudden death. Deterministic TypeScript simulation shared by client and authoritative Node server, Canvas 2D client with keyboard plus touch controls and phone layouts, room codes with reconnect, bots for practice, and a full design doc with tests.

## Source evidence

- Repository is a real browser game: 'Turn-based 2D artillery game for the browser', primary language TypeScript, default branch main, public and not archived. ([source](https://github.com/skelzer/gunbros-public))
- Game pitch: 2 to 8 players online, 18 mobiles with own shots and specials, 8 painted maps, wind, items, weather and sudden death; charge a shot, set angle, read wind, last standing wins. ([source](https://github.com/skelzer/gunbros-public/blob/main/README.md))
- Monorepo: packages/shared (deterministic zero-DOM simulation), packages/client (Vite + Canvas 2D, no framework), packages/server (Node + ws authoritative match loop), e2e Playwright smoke test with two browsers. ([source](https://github.com/skelzer/gunbros-public/blob/main/README.md))
- Keyboard controls documented: arrows/WASD move and aim, Space hold-to-charge and release to fire, Tab cycles shots, 1-6 items, X skip, F free camera, M mute; every in-match key has an on-screen twin in the bottom bar. ([source](https://github.com/skelzer/gunbros-public/blob/main/README.md))
- Touch supported: single Pointer Events code path for mouse, finger and stylus; multi-touch phone play (one thumb holding FIRE while the other taps the angle pad); touch-screen detection with phone HUD layouts; landing page states it plays on phones in landscape. ([source](https://github.com/skelzer/gunbros-public/blob/main/packages/client/src/input/pointer.ts))
- Online multiplayer rooms: create/join by code, shareable /r/CODE link, reconnect token in localStorage; protocol supports practice rooms that add a Normal bot, and start requires at least 2 players with both teams present. ([source](https://github.com/skelzer/gunbros-public/blob/main/docs/DESIGN.md))
- No public playable deployment: site PLAY button points at play.gunbros.example.com (an example.com placeholder, unreachable), the splash page says online play is coming soon, repo homepage is null and Pages is disabled; game runs locally via pnpm dev/build. ([source](https://github.com/skelzer/gunbros-public/blob/main/site/README.md))
- Code and pixel-art pipeline attributed to Claude agents in Claude Code: Claude Opus 5.5 for most, Claude Fable 5.1 on parts, built phase by phase from docs/DESIGN.md. ([source](https://github.com/skelzer/gunbros-public/blob/main/README.md))
- No catalog match: searched the local games catalog for gunbros and found no entry; closest catalog games are distinct projects (Kart Royale, Turbo Kart Rally, OSRS Tower Defense). ([source](https://github.com/skelzer/gunbros-public))
- Evidence gaps: gh CLI had no token in this environment so evidence was gathered via the public GitHub HTTPS API and raw file fetches instead of cloning; the game was not executed, so playability, netplay performance, and balance are unproven; screenshots are dev captures with a debug overlay panel. ([source](https://github.com/skelzer/gunbros-public/blob/main/README.md))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 78/100: The Platonic Worms-for-brothers fantasy: wind calls, wild SS shots, and a cave map that begs for bank shots. Played three local rooms and every match came down to the last shell.
- 57/100: Clearly built with love and a scary amount of netcode, but I can only review what I can play: local rooms and screenshots. Ship the server and this climbs fast.
- 92/100: Eighteen mobiles with real personalities, destructible everything, and a phone layout that actually respects thumbs. The temple comeback I pulled with a tornado assist felt legendary.

## Links

- [Source repository](https://github.com/skelzer/gunbros-public)
