# Meridian Wake

[Play the game](https://meridian-wake-g6a.vercel.app) · [View source](https://github.com/michaelcrosato/meridian-wake-g6a) · [Previous report](https://github.com/AwesomeClaude/.github/blob/e866255fc5cb8e58c821c089ae8d9381df1f427d/games/michaelcrosato--meridian-wake-g6a/README.md)

| Overall rating | Screenshot score |
| :---: | :---: |
| **60/100** | **68/100** |

<details>
<summary>Read the scoring rationale</summary>

### Overall rating

Excluding the target itself, the closest comparators are moorestech (64 overall, catalog top with verified dense 3D factory systems, co-op, and years of iteration), LUMENRIFT (58, polished 3D action with 68-score screenshots), GunBros (57, complete twin-stick combat loop with 68-score screenshots), Kart Royale (50, complete polished single-loop 3D racer with 70-score screenshots), and SpaceHo2 (42, single-map 2D space 4X with AI rivals but unverified presentation). Meridian Wake sits above Kart Royale and SpaceHo2: it has a publicly reachable playable build, three inspected coherent gameplay frames with full HUDs, and documented end-to-end systems (694 systems, 351 hulls, large outfit catalog, Free Worlds campaign with endings, mining, boarding, escorts, autosave, CI/e2e, keyboard plus touch plus gamepad). It sits below moorestech because it is a single-day AI-generated adaptation with 0 stars, single-player only, no multiplayer/live-ops/modding evidence, and inventory counts alone cannot prove balance, performance at scale, or fun. Evidence gaps: no interactive playtest beyond loading the game shell and screenshots; combat balance, late-campaign depth, and sustained performance unverified.

### Screenshot score

Best gameplay frame (flight.png) is the game's own output: faceted low-poly planet, brick-built Sparrow and ring station, scattered asteroids, orbit lines, and a complete readable HUD with mission, credits, ship bars, action buttons, radar, and renderer telemetry. Coherent palette, clean composition, genuine scene detail. Against catalog calibration it sits just below Kart Royale/Turbo Kart Rally/Neural Sight (70, denser dynamic 3D or photographic scenes) and moorestech (76, densest HUD-heavy 3D), above OSRS Tower Defense (65, dense flat 2D) on 3D depth, and well above THORNMERE (60), Taipo (55), and flat DOM games (2048 45, Blackjack/Beachy 35, neverquest 30). Fleet and touch frames confirm real gameplay UI; title card discounted. Stills prove nothing about motion, performance, or balance.

</details>

## At a glance

| Detail | Value |
| --- | --- |
| Repository created | 27 Sep 2026 · 04:27 UTC |
| Added to catalog | 27 Sep 2026 · 06:18 UTC |
| Last updated | 28 Sep 2026 · 04:52 UTC |
| Documented creation models | [GPT-6 Astra](https://raw.githubusercontent.com/michaelcrosato/meridian-wake-g6a/main/README.md) |

## Screenshots

![Meridian Wake gameplay](screenshots/795097682ba47d658140230b7de03ab869161480a83f27c5fc028b2b368a24cb.png)

Inspected 1920x1080 gameplay frame: top-down 3D flight at Rutilicus near New Boston with large faceted teal/white planet, white/teal brick-built Sparrow with engine flames, ring station, scattered asteroids, orbit rings, second ship, mission banners, top Starmap/Spaceport/My ship/Journal/Options/Cloak bar, 24,000 cr plus 75,000 cr loan readout, shield/hull/fuel/power/heat bars, Land/Plot a course/Actions buttons, radar, and WebGL2 Auto-High 16.8 ms 29 bodies telemetry. Clearly the game's own runtime output.

[Original screenshot](https://raw.githubusercontent.com/michaelcrosato/meridian-wake-g6a/19e49a23f4ce9e41c3d937a73e6a9973cf3b49fd/docs/images/flight.png)

![Meridian Wake gameplay](screenshots/d21d6277c7e9108cf935904a01feaca38a5fae05741a79763052d85e8e7353f9.png)

Inspected 1440x900 gameplay frame: same planet and station surrounded by a large Quarg Hydra fleet of dark multi-arm ships, AUTOPILOT LANDING APPROACH text, captain's-heading mission panel, full top bar and credits readout, bottom Land/Plot/Actions buttons, left ship stat bars, right scanner showing 12 hostile contacts, WebGPU High 248.1 ms 41 bodies telemetry. Clearly the game's own runtime output showing fleet encounter scale.

[Original screenshot](https://raw.githubusercontent.com/michaelcrosato/meridian-wake-g6a/19e49a23f4ce9e41c3d937a73e6a9973cf3b49fd/docs/images/webgpu.png)

![Meridian Wake gameplay](screenshots/861c1e095a315f468951674a947d283771f8f14dfb5e71bc8f92e3f0a951ffd9.png)

Inspected 844x390 gameplay frame: touch layout with top icon bar, credits readout, planet and brick ship, mission panel, right-side Sparrow stat bars, bottom on-screen steering/thrust/brake/boost buttons left and fire/boost buttons right, WebGL2 Balanced 54.0 ms 17 bodies telemetry. Clearly the game's own runtime output proving touch controls.

[Original screenshot](https://raw.githubusercontent.com/michaelcrosato/meridian-wake-g6a/19e49a23f4ce9e41c3d937a73e6a9973cf3b49fd/docs/images/touch-landscape.png)

![Meridian Wake gameplay](screenshots/7b35d3c8831c7b515e4375654511119b6ceb80a9d3566d42efa217e03fc5d4c2.png)

Inspected 1920x1080 title screen: MERIDIAN WAKE masthead with Begin your voyage button, Flight handbook and Options links, large brick-built ship and faceted planet backdrop with asteroids and station. Menu/title card, not active gameplay; discounted for graphics scoring.

[Original screenshot](https://raw.githubusercontent.com/michaelcrosato/meridian-wake-g6a/19e49a23f4ce9e41c3d937a73e6a9973cf3b49fd/docs/images/title.png)

## Play

- Open the playable build at https://meridian-wake-g6a.vercel.app/ in a current hardware-accelerated browser with WebGPU or WebGL2.
- Begin your voyage and choose the Sparrow, Shuttle, or Star Barge; a new captain replaces the local autosave, so export a backup first if needed.
- Read the first transmission at New Boston's spaceport and accept it.
- Depart, open the starmap with M, select the route, and jump; interstellar travel costs fuel and advances the day.
- Press L for assisted landing, then complete the mission at the port; pursue story and freelance trading, passenger, cargo, and mining work in parallel.
- Desktop: W/Up thrust, A/D or arrows rotate, S/Down brake, Space fire primary, F fire secondary, Shift boost, C cloak, M starmap, L land/launch, E ship operations, B board, G harvest fuel, R survey/scan, J journal, I equipment/cargo, Esc pause. Touch screens use on-screen steering, thrust, brake, boost, fire, and cloak controls; standard gamepads are also supported with remapping in Options.

## Mechanics

- Top-down inertial 3D spaceflight with thrust, rotation, braking, boosting, assisted landing, and autopilot landing approach
- Open-world trading in commodities plus passenger and cargo contracts with deadlines, fuel costs, and day advancement
- Bank loan, crew costs, fuel/repair, banking, shipyards, outfitters, and fleet/escort services at ports
- Combat with primary and secondary weapons, finite ammunition, point defense, energy/heat management, cloaking, boarding and capturing disabled ships, and persistent hulks/wrecks
- Asteroid mining with finite extraction and cooldowns, mineral cargo sales, and salvage
- Ship ownership progression across 351 base hulls and a large outfit catalog with cargo, bunk, engine, scanner, cloak, Jump Drive, and expedition-gated equipment
- Free Worlds branching campaign with mutually exclusive routes, protected convoys, reconnaissance, diplomacy, timed evasion missions, and an earned ending with continued sandbox play
- Galaxy traversal across 694 systems with starmap route planning, directed wormholes, gas-giant, stellar-garden, ringworld, and station locations
- Local autosave with JSON save export/import, volume/mute/fullscreen options, diagnostics, handbook, and quality presets

## Tags

- space
- space-sim
- trading
- exploration
- story-campaign
- 3d
- low-poly
- single-player
- browser

## Controls

- Mobile controls: Supported
- Motion controls: Not established
- Gamepad: Supported
- Keyboard/mouse: Supported

## Player modes

- Human players: 1
- Modes: single-player

## Technologies

- **Three.js 0.186.1** — engine ([evidence](https://raw.githubusercontent.com/michaelcrosato/meridian-wake-g6a/main/package.json))
- **Rapier 0.21.0** — physics ([evidence](https://raw.githubusercontent.com/michaelcrosato/meridian-wake-g6a/main/package.json))
- **Vite 8.3.1** — build ([evidence](https://raw.githubusercontent.com/michaelcrosato/meridian-wake-g6a/main/package.json))
- **JavaScript** — language ([evidence](https://api.github.com/repos/michaelcrosato/meridian-wake-g6a))

## Reconstructed prompt

Build Meridian Wake: a brick-built 3D browser reimagining of Endless Sky with Vite plus Three.js WebGPU/WebGL2 and Rapier physics. Include three starting ships, a bank loan, ports with trading/contracts/shipyards/outfitters/fleet/bank/concourse, a Free Worlds branching campaign with endings plus sandbox and wiki side stories, ~694 systems with hundreds of ships and outfits, mining, boarding, escorts, keyboard plus touch plus standard gamepad controls with remapping, autosave with JSON export, and Vercel static deployment.

## Source evidence

- Repository michaelcrosato/meridian-wake-g6a is public, not a fork, described as a brick-built 3D browser reimagining of Endless Sky with Vite, Three.js WebGPU/WebGL2 and Rapier, generated 2026-09-26 with GPT-6 Astra; homepage points to the Vercel deployment and primary language is JavaScript. ([source](https://api.github.com/repos/michaelcrosato/meridian-wake-g6a))
- README titles the game Meridian Wake, attributes generation to GPT-6 Astra (g6a) on 26 September 2026, and describes trading, passengers, mining, ship equipment, escorts, and the Free Worlds story in a 3D browser adaptation of Endless Sky. ([source](https://raw.githubusercontent.com/michaelcrosato/meridian-wake-g6a/main/README.md))
- README documents keyboard controls (W/arrows thrust, A/D turn, S brake, Space primary, F secondary, Shift boost, L land/launch, M map, E operations, B board, G scoop fuel, R scan, C cloak, T contacts, J journal, I equipment, Esc pause), establishing keyboard support. ([source](https://raw.githubusercontent.com/michaelcrosato/meridian-wake-g6a/main/README.md))
- README states the same game is available through keyboard, touch and standard gamepads, and compatibility docs state keyboard, remapped controls, simultaneous touch and standard gamepads are supported, establishing gamepad support. ([source](https://raw.githubusercontent.com/michaelcrosato/meridian-wake-g6a/main/docs/compatibility.md))
- README and flight handbook describe simultaneous touch steering, thrust, brake, boost, primary/secondary fire and cloak controls with portrait and landscape layouts, and the touch screenshot shows on-screen direction, thrust, fire and boost buttons, establishing mobile touch support. ([source](https://raw.githubusercontent.com/michaelcrosato/meridian-wake-g6a/main/README.md))
- No accelerometer, gyroscope, or device-motion controls are documented in the README or compatibility docs; motion support is unestablished rather than ruled out. ([source](https://raw.githubusercontent.com/michaelcrosato/meridian-wake-g6a/main/docs/compatibility.md))
- Progress autosaves in browser storage as a single captain where a new captain replaces the save, with JSON export/import and no multiplayer, lobby, or netcode documented, establishing single-player with one human player. ([source](https://raw.githubusercontent.com/michaelcrosato/meridian-wake-g6a/main/README.md))
- package.json pins three 0.186.1, @dimforge/rapier3d-compat 0.21.0, vite 8.3.1 and @playwright/test 1.63.0, establishing engine, physics, and build versions. ([source](https://raw.githubusercontent.com/michaelcrosato/meridian-wake-g6a/main/package.json))
- README rendering section documents Three.js WebGPU with WebGL2 fallback, node materials, bloom/AO, automatic quality selection, and fixed-step Rapier simulation with interpolation. ([source](https://raw.githubusercontent.com/michaelcrosato/meridian-wake-g6a/main/README.md))
- Content docs pin Endless Sky data, describe 694 systems, 2344 native mission declarations, 351 base hull names, a large outfit catalog, Free Worlds Reconciliation/Checkmate paths plus sandbox, and authored wiki side stories; counts describe inventory, not proof every script is playable. ([source](https://raw.githubusercontent.com/michaelcrosato/meridian-wake-g6a/main/docs/content.md))
- Deployed homepage returns HTTP 200 and serves the game shell with scene/app mounts, MERIDIAN WAKE loading text, and game bundles for universe, render-engine, and physics-engine, verifying a publicly reachable playable URL. ([source](https://meridian-wake-g6a.vercel.app))
- Existing catalog directory games/michaelcrosato--meridian-wake-g6a matches this repository and playable URL exactly, so the existing slug is reused; it was identified by repository and deployment match, not title alone. ([source](https://github.com/michaelcrosato/meridian-wake-g6a))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 82/100: Fictional review: I ran the first passenger contract from New Boston exactly as the handbook says, and the loop clicked — launch, plot, jump, assisted landing, payday. The brick-built ships give every system real charm.
- 64/100: Fictional review: Huge galaxy and loads of outfits to chase, but I spent more time reading journals and starmaps than dogfighting. A thoughtful trader's space game rather than an arcade rush.
- 95/100: Fictional review: A one-person loan, a tiny Sparrow, and hundreds of star systems of possibility — the Free Worlds story threading through trading, mining, and boarding is the most ambitious browser voyage I have seen this year.

## Links

- [Source repository](https://github.com/michaelcrosato/meridian-wake-g6a)
- [Playable game](https://meridian-wake-g6a.vercel.app)
