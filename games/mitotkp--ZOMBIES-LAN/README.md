# ZOMBIES LAN

[View source](https://github.com/mitotkp/ZOMBIES-LAN)

| Overall rating | Screenshot score |
| :---: | :---: |
| **50/100** | **Not scored** |

<details>
<summary>Read the scoring rationale</summary>

### Overall rating

Far from AAA: no verified public build, no screenshots, and playability, performance, and balance are unverifiable from docs alone, with 0 stars and LAN self-hosting friction. On documented scope it outranks Dead Signal: Exclusion Zone (47, single-player zombies FPS with no multiplayer and a thinner loop) thanks to 1-4 player authoritative LAN co-op, a five-zone map, mystery box, Pack-a-Punch, six perks, buildable shield, infection/meds system, and five bosses, and it roughly matches Kart Royale (50, complete verified 3D loop) on systems depth while sitting below Ashlands (55, catalog top) because its 3D presentation cannot be verified from any image evidence. Judged from repository sources and docs only; code and docs do not prove playability, performance, or balance.

### Screenshot score

No inspectable gameplay screenshot.

</details>

## At a glance

| Detail | Value |
| --- | --- |
| Repository created | 25 Sep 2026 · 17:51 UTC |
| Added to catalog | 27 Sep 2026 · 06:16 UTC |
| Last updated | 27 Sep 2026 · 06:16 UTC |
| Documented creation models | [Claude Opus 5.5](https://github.com/mitotkp/ZOMBIES-LAN) |

## Play

- Host PC needs Node.js 20+ and all players on the same LAN; run npm install once then npm start (or double-click start-server.bat on Windows) and share the printed http://HOST-IP:3000 address.
- Each player opens the address in a modern desktop browser with WebGL, enters a name, picks a color, presses Unirse a la partida, marks Listo, and the host presses Iniciar partida.
- Start in the Terminal with an M1911 and 500 points; shoot zombies and rebuild barricade boards (hold F) to earn points, then open doors, buy wall weapons, perks, and turn on the power.
- Cure with H (bandage, antidote, or medkit bought from red-cross cabinets), use V/G/Q for melee/grenade/shield, L for flashlight, and revive downed teammates before everyone falls.

## Mechanics

- First-person wave survival for 1-4 LAN players with authoritative Node.js server (20 Hz tick/snapshots) and Three.js browser client
- Points economy from kills and barricade rebuilding spent on doors, wall-buy weapons, mystery box, Pack-a-Punch upgrades, and 6 Perk-a-Colas
- Pueblo Olvidado map with Terminal, Calle, Bar, Almacen, and Planta Electrica zones plus power switch and buildable shield
- Three special zombies (Corredor, Explosivo, Tanque) and five bosses (Carnicero, Madre Plaga, Nigromante, Acorazado, Espectro) scaling per round
- Health/infection system with bandages, antidotes, and medkits bought at red-cross cabinets or dropped by zombies
- Revivecoop: downed players can be revived by teammates; full team wipe ends the run; solo quick-revive supported
- Procedural code-generated art and WebAudio sound with no asset downloads; Spanish/English i18n and brightness setting
- Dev tooling: chat slash commands, ?debug=1 mode, /test/ weapon/model inspection room, map validator, and bot load tests

## Tags

- fps
- zombie
- survival
- co-op
- wave-defense
- lan-multiplayer
- 3d
- procedural

## Controls

- Mobile controls: Not supported
- Motion controls: Not established
- Gamepad: Not established
- Keyboard/mouse: Supported

## Player modes

- Human players: 1-4
- Modes: single-player, online multiplayer

## Technologies

- **Three.js 0.186.1** — engine ([evidence](https://github.com/mitotkp/ZOMBIES-LAN/blob/main/package.json))
- **JavaScript** — language ([evidence](https://api.github.com/repos/mitotkp/ZOMBIES-LAN))
- **ws 8.21.3** — framework ([evidence](https://github.com/mitotkp/ZOMBIES-LAN/blob/main/package.json))
- **WebGL** — rendering ([evidence](https://github.com/mitotkp/ZOMBIES-LAN/blob/main/README.md))
- **Web Audio API** — audio ([evidence](https://github.com/mitotkp/ZOMBIES-LAN/blob/main/public/js/audio.js))

## Reconstructed prompt

Build a 1-4 player LAN co-op browser FPS Zombies survival game inspired by Call of Duty Black Ops 2, in Spanish and English: authoritative Node.js + WebSocket server with a Three.js client and no bundler, a five-zone Pueblo Olvidado map with barricaded windows, points economy, doors, mystery box, Pack-a-Punch, 6 perks, wall weapons, buildable shield, powerups, health/infection with bandages/antidotes/medkits, 3 special zombies and 5 scaling bosses, revives, WASD+mouse pointer-lock controls, fully procedural textures and WebAudio, plus dev commands, a test room, a map validator, and bot tests.

## Source evidence

- Real game project: repo mitotkp/ZOMBIES-LAN, description 'Proyecto de juego Zombie de prueba de Claude Opus 5.5', language JavaScript, 0 stars/0 forks, default branch claude/affectionate-edison-hb53ej plus main; homepage null, has\_pages false, so no public playable deployment. ([source](https://api.github.com/repos/mitotkp/ZOMBIES-LAN))
- README defines a 1-4 player LAN co-op FPS inspired by Call of Duty Black Ops 2 Zombies: one player hosts with Node.js, others join from their PCs on the same network; solo play confirmed by solo boss-damage/HP scaling rules. ([source](https://github.com/mitotkp/ZOMBIES-LAN/blob/main/README.md))
- Controls table documents WASD/mouse movement and look, LMB fire, RMB aim, Shift/C/Ctrl/Space, R reload, F use, V/G/Q melee/grenade/shield, L flashlight, H heal, 1-2-3/wheel weapons, Tab/T/Enter/Esc; client input.js is keyboard/mouse with pointer lock, establishing keyboard/mouse support. ([source](https://github.com/mitotkp/ZOMBIES-LAN/blob/main/README.md))
- README frames all clients as PCs ('los demas se conectan desde su PC'), requires pointer-lock mouse look, and a full client-code search finds no touch, joystick, or gamepad handlers (no touchstart/ontouch/gamepad APIs), ruling out mobile touch controls as a supported path; gamepad and motion support are undocumented. ([source](https://github.com/mitotkp/ZOMBIES-LAN/blob/main/public/js/input.js))
- Recursive main-branch file tree lists all game code (server/, shared/, public/js, tools) and zero image files, so no gameplay screenshot can be inspected from the repository. ([source](https://api.github.com/repos/mitotkp/ZOMBIES-LAN/git/trees/main?recursive=1))
- package.json declares ESM Node server with three 0.186.1 and ws 8.21.3 dependencies; index.html uses an import map for three with a WebGL browser requirement; audio.js synthesizes all sound with WebAudio. ([source](https://github.com/mitotkp/ZOMBIES-LAN/blob/main/package.json))
- No catalog match: the closest entry, Dead Signal: Exclusion Zone (bridge-mind single-player extraction zombies FPS), is a different repository, architecture, and mode set with no explicit cross-reference to this project, so this is a new entry with catalog\_slug null. ([source](https://github.com/mitotkp/ZOMBIES-LAN))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 82/100: The full Black Ops 2 Zombies loop is here: barricades, points, doors, mystery box, Pack-a-Punch, six perks and a buildable shield, with runners, exploders, tanks and five distinct bosses keeping later rounds tense.
- 58/100: Enormous documented scope for a browser LAN shooter, but with no public playable build and zero screenshots I cannot verify the look, the gunfeel, or that four-player sessions hold together.
- 100/100: Infection plus bandages, antidotes and medkits, chalk-outline melee weapons, Spanish and English, procedural everything and a bot test harness: the most complete co-op Zombies package in the catalog.

## Links

- [Source repository](https://github.com/mitotkp/ZOMBIES-LAN)
- [Repository README](https://github.com/mitotkp/ZOMBIES-LAN/blob/main/README.md)
