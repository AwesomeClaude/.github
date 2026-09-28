# OxCity

[View source](https://github.com/exdal/opus5.5-test)

| Overall rating | Screenshot score |
| :---: | :---: |
| **54/100** | **48/100** |

<details>
<summary>Read the scoring rationale</summary>

### Overall rating

Excluding the target itself, most relevant comparators are moorestech (64, catalog top with deeper factory systems, ~15k commits, denser HUDs and co-op), Ashlands (55, broader custom-engine ambition but zero inspectable screenshots), OSRS Tower Defense (52, deepest prior content with 61 monsters, 130 waves and metagame but 2D only), Kart Royale (50, complete polished 3D loop but single track and no online multiplayer), Neon Arena (48, real-time 3D roguelite with modes and meta-progression but no inspected gameplay pixels), and Dead Signal (47, structured 3D mission plus economy but single mission and no screenshots). OxCity sits at 54, just below Ashlands and above OSRS Tower Defense: verified single-module C++23 game with procedural city, five Jolt vehicles, traffic and pedestrian AI, wanted and heist systems, plus genuine 4-player ENet multiplayer with dedicated server and snapshot replication exceeds Kart Royale, Neon Arena, and Dead Signal on gameplay depth, scope, and technical execution, while four inspected low-resolution gameplay frames show a coherent but sparse low-poly city that trails moorestech and Kart Royale on visual polish. Capped well below AAA because there is no playable build, release, or web deployment to verify performance, balance, or netcode, audio and late-game depth are unverified, and the repo frames itself as an engine field test plus experience report.

### Screenshot score

Four inspected 640x360 gameplay frames plus one menu show a coherent low-poly top-down city with roads, rooftops, tiny actors, a red car, and dense RmlUi HUD elements, but flat colors, sparse detail, and small low-resolution actors. Below Kart Royale (70), Turbo Kart Rally (70), OSRS Tower Defense (65), HEX DANMAKU (60), and THORNMERE (60) on scene detail, lighting, and composition, and roughly level with Taipo (55) on readability while trailing it on art richness. Well above neverquest (30), T-Rex Runner (30), Infinite Craft (32), and TypeScript-Blackjack (35) because these are real in-engine gameplay frames with HUD, scoreboard, wanted diamonds, and multiplayer events rather than text UI or minimal shapes. Menu frame discounted as non-gameplay.

</details>

## At a glance

| Detail | Value |
| --- | --- |
| Repository created | 25 Sep 2026 · 18:34 UTC |
| Added to catalog | 27 Sep 2026 · 06:29 UTC |
| Last updated | 27 Sep 2026 · 06:29 UTC |
| Documented creation models | Not established |

## Screenshots

Screenshot unavailable; inspect the original source.

Inspected 640x360 gameplay frame: top-down street with red Meridian car, green pager banner NICE WHEELS. YOU STOLE A MERIDIAN., pink kill feed ALICE WASTED HOSTESS, scoreboard ALICE versus HOSTESS with 3-star wanted diamonds, cash $30, 1300 PTS, red health bar, PISTOL x56, and MERIDIAN 4 KM/H readout. The game's own runtime output.

[Original screenshot](https://raw.githubusercontent.com/exdal/opus5.5-test/claude/ecstatic-brahmagupta-6ik44r/docs/screenshots/mp_listen_driving.png)

Screenshot unavailable; inspect the original source.

Inspected 640x360 gameplay frame: top-down street and sidewalk with YOU WASTED BOB. +1000 PTS banner, large 2X COMBO +200 overlay, ALICE JOINED and ALICE WASTED BOB kill feed, ALICE versus BOB scoreboard, $45 cash, blue wanted diamonds, red health bar, and PISTOL x55. The game's own runtime output.

[Original screenshot](https://raw.githubusercontent.com/exdal/opus5.5-test/claude/ecstatic-brahmagupta-6ik44r/docs/screenshots/mp_shooter_wasted_them.png)

Screenshot unavailable; inspect the original source.

Inspected 640x360 gameplay frame: top-down city street with large red FLATLINED overlay reading WASTED BY ALICE. DROPPED $0, BOB JOINED and ALICE kill feed at left, $0 cash, dark health bar, and PISTOL x60. The game's own runtime output.

[Original screenshot](https://raw.githubusercontent.com/exdal/opus5.5-test/claude/ecstatic-brahmagupta-6ik44r/docs/screenshots/mp_target_wasted.png)

Screenshot unavailable; inspect the original source.

Inspected 960x540 gameplay frame: high top-down view of brown rooftops with vents, grey road with yellow dashes, tiny pedestrian on sidewalk, dark buildings, green WELCOME TO OXCITY pager banner, $0 cash, faint wanted diamonds, red health bar, and PISTOL x60. The game's own runtime output.

[Original screenshot](https://raw.githubusercontent.com/exdal/opus5.5-test/claude/ecstatic-brahmagupta-6ik44r/docs/screenshots/vsm_ghost_shadow_patched.png)

Screenshot unavailable; inspect the original source.

Inspected 960x540 menu frame: OXCITY title over an aerial low-poly city backdrop with MULTIPLAYER heading, NAME field ALICE, HOST field 192.168.1.20:7777, and yellow JOIN, HOST, and BACK buttons. Menu UI, not active gameplay; placed last.

[Original screenshot](https://raw.githubusercontent.com/exdal/opus5.5-test/claude/ecstatic-brahmagupta-6ik44r/docs/screenshots/mp_menu.png)

## Play

- Wake up outside the hospital with a pistol and no money; follow pager prompts and HUD markers.
- Move on foot with WASD or arrows, sprint with Shift, attack with Ctrl or left mouse button, switch weapons with Q, rob or mug with E, pause with Esc.
- Steal cars with F or Enter, drive with WASD or arrows, use Space as handbrake and H for the horn; carjack parked cars or pull drivers out.
- Mug pedestrians by holding E next to them, evade or fight police as the 0 to 5 diamond wanted level rises, and avoid standing still near cops or you are ARRESTED.
- Rob the north-side bank by standing on the green marker and holding E for 8 seconds while guards shoot; collect the $6,000 to $12,000 payout.
- For multiplayer, open MULTIPLAYER in the menu, enter a name, then HOST GAME or JOIN GAME by address, or run OxCity --host, --join, or --server from the command line.

## Mechanics

- Top-down open-city crime loop: steal cars, mug pedestrians, rob the bank, evade police arrest and hospital respawn
- Procedural 16x16-tile city with road graph, sidewalks, parks, six building styles, lamps, and bank
- On-foot movement on Jolt character controller with fists, pistol, and hold-E mugging
- Five drivable Jolt wheeled-vehicle car models with carjacking, handbrake, and distinct handling
- Road-graph traffic that brakes for obstacles plus sidewalk pedestrians that cross streets and flee violence
- 0 to 5 diamond wanted level with out-of-sight police-car spawns, ramming pursuits, foot-cop deployment, shooting from 3 stars, ARRESTED and FLATLINED states
- Timed 8-second hold-E bank heist with alarm, armed guards, and $6,000 to $12,000 payout
- RmlUi HUD, pager, prompts, heist bar, menus, scoreboard, kill feed, and name tags bound to one data model
- Free-for-all online multiplayer for up to 4 players with listen-server hosting, join by address, dedicated server, per-player cash, wanted level, score, and cash drops
- Host-authoritative quantized snapshots at 30 Hz with client interpolation, client-side walk prediction, and seeded shared city generation

## Tags

- open-world
- crime
- gta-like
- driving
- top-down
- action
- heist
- police-chase
- multiplayer
- procedural-generation
- low-poly

## Controls

- Mobile controls: Not established
- Motion controls: Not established
- Gamepad: Not established
- Keyboard/mouse: Supported

## Player modes

- Human players: 1-4
- Modes: single-player, online multiplayer

## Technologies

- **Oxylus** — engine ([evidence](https://github.com/exdal/opus5.5-test))
- **C++ 23** — language ([evidence](https://github.com/exdal/opus5.5-test))
- **Vulkan** — rendering ([evidence](https://github.com/oxylusengine/Oxylus))
- **Jolt Physics** — physics ([evidence](https://github.com/exdal/opus5.5-test))
- **RmlUi** — framework ([evidence](https://github.com/exdal/opus5.5-test))
- **ENet** — framework ([evidence](https://github.com/exdal/opus5.5-test))
- **miniaudio** — audio ([evidence](https://github.com/oxylusengine/Oxylus))
- **xmake** — build ([evidence](https://github.com/exdal/opus5.5-test))
- **Python** — language ([evidence](https://github.com/exdal/opus5.5-test))

## Reconstructed prompt

Build a top-down open-city crime game on the Oxylus engine in C++23 with a procedural 16x16 city, drivable Jolt physics cars, pedestrian and traffic AI, a 0-5 diamond wanted and police pursuit system, a timed bank heist, an RmlUi HUD and menus, Python-generated low-poly models and sounds, scripted autoplay screenshots, and up to 4-player ENet online multiplayer with listen, join, and dedicated-server modes.

## Source evidence

- Repository exdal/opus5.5-test exists, is public, has one branch, zero stars and zero forks, primary language C++, and no homepage; no releases, pages, or playable deployment are listed. ([source](https://github.com/exdal/opus5.5-test))
- README titles the game OxCity and describes a top-down open-city crime game on the Oxylus engine, a field test whose main output is the docs experience report; the player wakes outside the hospital, steals cars, mugs people, robs the north-side bank, and evades arrest. ([source](https://github.com/exdal/opus5.5-test))
- Game scope documented: 16x16 procedural city with road graph, on-foot Jolt character controller with fists, pistol and hold-E mugging, five Jolt wheeled-vehicle car models with carjacking, graph-following traffic, sidewalk pedestrians that flee, 0-5 diamond wanted level with ramming chases and ARRESTED and FLATLINED states, and an 8-second hold-E bank heist paying $6,000 to $12,000. ([source](https://github.com/exdal/opus5.5-test))
- Keyboard and mouse controls explicitly documented: WASD or arrows to move and drive, Shift sprint, Space handbrake, F or Enter enter and exit, Ctrl or LMB attack, Q switch weapon, E rob, H horn, Esc pause. ([source](https://github.com/exdal/opus5.5-test))
- Multiplayer documented as free-for-all for up to 4 players over ENet with menu HOST GAME and JOIN GAME by address, default UDP 7777, command-line --host, --join, and --server dedicated-server modes, per-player cash, wanted level and score, and same-source plus same-seed join requirement. ([source](https://github.com/exdal/opus5.5-test))
- Build documented as source-only with xmake, clang and libc++ 23, and the Vulkan SDK; headless autoplay and network-test scripts capture screenshots and print pass or fail checklists. No browser, store, or downloadable playable URL is offered. ([source](https://github.com/exdal/opus5.5-test))
- HUD, pager, prompts, heist bar, menus, scoreboard, kill feed, and name tags are RmlUi documents; models and sounds are procedural from tools/assetgen scripts; game code is C++23 in game/src with xmake cooking and install rules. ([source](https://github.com/exdal/opus5.5-test))
- Four gameplay screenshots inspected as the game's own runtime output showing driving, wasting another player, flatlined death, and city exploration HUDs; the referenced docs/screenshots/03\_driving.png hero image returns 404 while api listing and raw fetch confirm only multiplayer and shadow-test captures exist. ([source](https://github.com/exdal/opus5.5-test))
- Oxylus upstream describes a C++ data-driven engine with a modular Vulkan renderer via vuk, multithreaded Jolt physics, Lua scripting with flecs, Dear ImGui editor, miniaudio 3D audio, and enet networking. ([source](https://github.com/oxylusengine/Oxylus))
- No explicit attribution of a game-creation AI model was found in the inspected README, repository page, or devlog head; the branch name and repository name alone do not establish a creation model, so none is recorded. ([source](https://github.com/exdal/opus5.5-test))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 82/100: Fictional review: stealing my first Meridian while the pager cheered me on felt genuinely GTA, and the bank timer with guards closing in had my palms sweating. The diamond wanted chase rams hard and the arrest rule is brutal.
- 61/100: Fictional review: ambitious little city with real multiplayer bones, but the tiny low-res actors and empty rooftops make it feel like a tech demo, and building it sounds harder than playing it.
- 100/100: Fictional review: four criminals, one city, one dropped wallet on the pavement. Our host-and-chase night ended with a perfect carjack revenge and I have never laughed harder at FLATLINED.

## Links

- [Source repository](https://github.com/exdal/opus5.5-test)
- [Oxylus engine upstream](https://github.com/oxylusengine/Oxylus)
