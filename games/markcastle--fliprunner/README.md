# Flip Runner Racing

[Open the game source](https://github.com/markcastle/fliprunner)

**Overall rating:** 33/100. Far from AAA with no 3D world, AI rivals, multiplayer, cinematics, or live-ops scale; single-file Canvas 2D heightfield art and WebAudio synth only. Most relevant comparators: Taipo (35 overall, complete niche Bevy typing-TD with one small map and acknowledged art and sound gaps), Beachy Beachy Ball (25 overall, single roll-to-star mechanic with two short tours and flat minimal art), and Turbo Kart Rally (40 overall, complete 3D kart loop with 8 racers, AI field, items, and menus). Flip Runner sits just below Taipo and below Turbo Kart Rally: it exceeds Beachy on scope with 10 themed levels, fuel plus flips plus chute plus ice plus collapsing bridges, 3-star progression, and bot-verified completability, and it beats Neural Sight (30, tiny prototype with no real loop) on finished-loop depth, but it trails the kart racers badly on visual scene rendering, opponents, and technical ambition, and trails Taipo on shipped validation (Taipo has multi-year releases and itch ratings; Flip Runner is a 2-commit one-shot with 2 stars, no live URL, and no inspectable screenshots). Evidence gaps: judged from repository file listing and README plus partial index.html source via unauthenticated fetch without cloning; gh api was unavailable without auth, no screenshots exist in the repo to inspect, and the live build was not played, so playability, balance, performance, and audio quality are unverified and source claims do not prove them.

**Screenshot score:** not scored. No inspectable gameplay screenshot.

## Play

- Open index.html (or deploy the single file to static hosting) and press PLAY, then pick a level.
- Reach the chequered flag without crashing and without running out of fuel.
- Drive with Up/Right/W/D for gas and Down/Left/S/A for brake and reverse; R restarts, P or Esc pauses.
- On touch use the GAS and BRAKE buttons or hold the right or left half of the screen; tap the parachute button in the air.
- Grab orange fuel cans to refill to 100%; collect coins and rarer gems along jump arcs and routes.
- Hold gas in the air to rotate backwards or brake to rotate forwards to land flips for bonus coins; landing on the helmet ends the run.
- Open the parachute only in the air after 0.12s of airtime to slow falls on big drops; it auto-releases on touchdown and kills forward speed.
- Keep moving on collapsing wood and faster ice bridges, carry speed onto ice since grip is near zero, and earn 1 star for finishing, 2 for 55% of coins, 3 for 80% of coins plus all gems.

## Mechanics

- 2D rigid-body car with two spring-damper wheel contacts on a heightfield, fixed 1/240s substep physics
- Gas and brake and reverse drive with grip-limited traction, rolling resistance, and top-speed taper
- Air rotation control for flips with landing flip bonus and big-air bonus, helmet-impact crash rule
- Fuel drain with idle trickle and refill-to-100% cans, out-of-fuel stuck fail state
- Coins and gems with star thresholds and level unlock progression saved to localStorage
- Collapsing bridge planks with wood versus faster ice shake timers, treated as drivable surfaces over pit gaps
- Zero-grip ice surfaces, parachute drag with auto-release and attitude leveling
- Terrain builder DSL with flat, hill, valley, bumps, drop, ramps, kicker, gap, bridge, and jump primitives plus seeded decorations
- Canvas 2D renderer with gradient sky, parallax clouds, camera lead, zoom, and shake; DOM HUD, menus, and touch controls
- Synthesized WebAudio engine, pickup and crash effects, and toggleable chiptune loop with no audio assets

## Tags

- 2d
- driving
- hill-climb
- physics
- browser-game
- canvas
- single-file
- single-player
- time-trial
- collectathon

## Reconstructed prompt

Build Flip Runner Racing, a remastered browser-native 2D hill-climb driving game in a single dependency-free index.html with zero network requests: one car with gas, brake, and parachute across 10 grass and snow levels with hills, jumps, collapsing wood and ice bridges, ice fields, fuel scarcity, and a final gauntlet; fuel, coins, gems, flip and air bonuses, 3-star scoring, and localStorage progression; Canvas 2D rendering with DOM HUD, menus, and touch controls; fully synthesized WebAudio engine, effects, and chiptune; deterministic fixed-step physics with a headless bot that proves every level is completable.

## Source evidence

- Repo is markcastle/fliprunner, Flip Runner Racing, a remastered browser-native rebuild of FlipRunner as a 2D hill-climb physics driving game living in a single index.html with zero dependencies and zero network requests. ([source](https://github.com/markcastle/fliprunner))
- File listing shows only .gitignore, LICENSE, README.md, and index.html with 2 commits, 2 stars, and 0 forks. ([source](https://github.com/markcastle/fliprunner))
- Game has 10 levels across grass and snow themes: tutorial, rolling hills, jumps, collapsing wood bridges, ice fields, big parachute drops, ice bridges, fuel scarcity, frozen heights, and a final gauntlet. ([source](https://github.com/markcastle/fliprunner/blob/master/README.md))
- Controls are arrows/WASD for gas and brake, Space for chute, R restart, P pause, plus GAS/BRAKE touch buttons and screen-half holds with a pulsing chute button. ([source](https://github.com/markcastle/fliprunner/blob/master/README.md))
- Mechanics include draining fuel refilled by cans, coins and rarer gems, flip and air bonuses, individually collapsing bridge planks with ice breaking about twice as fast, zero-grip ice, speedometer, 3-star scoring, and localStorage progression. ([source](https://github.com/markcastle/fliprunner/blob/master/README.md))
- Audio is synthesized engine, pickup/crash/win effects, and a toggleable chiptune loop generated live with WebAudio and no audio assets; ferries were descoped. ([source](https://github.com/markcastle/fliprunner/blob/master/README.md))
- Architecture is one HTML file with Canvas 2D rendering, DOM menus/HUD/touch buttons, requestAnimationFrame with fixed 1/240s physics substeps, heightfield terrain plus surface array, and a terrain builder DSL. ([source](https://github.com/markcastle/fliprunner/blob/master/README.md))
- Car model is a rigid body with two spring-damper wheel probes, traction-limited drive/brake, ice as low mu, air rotation, slope and velocity alignment helpers, helmet crash rule, and parachute drag with leveling. ([source](https://github.com/markcastle/fliprunner/blob/master/README.md))
- Verification claims three Node harnesses: a smoke suite, a completability bot that must finish all ten levels, and a jump parameter sweep; README lists foundational bugs found including top-speed friction, flat jump lips, suspension clamp, kill plane, and pit-center checks. ([source](https://github.com/markcastle/fliprunner/blob/master/README.md))
- No screenshots, demo URL, releases, or packages are listed on the repo page; deployment docs only explain manual Cloudflare Pages upload, and progress is stored under fliprunner\_save\_v1. ([source](https://github.com/markcastle/fliprunner/blob/master/README.md))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 75/100: \[Fictional review\] Imagined hill-climb fan: finally cleared The Big Drop with the chute open at the last second and stuck the landing for 3 stars — the flip coins and fuel tension make every slope feel earned.
- 50/100: \[Fictional review\] Made-up casual player note: fun for a few levels, but it is one car on bumpy heightfield hills with flat canvas art and no rivals — the ice bridges are brutal and I never saw what the later levels look like.
- 100/100: \[Fictional review\] Invented single-file nerd take: ten bot-completed levels, collapsing planks, parachute physics, and synth chiptune in one dependency-free HTML file with zero network requests? Absurdly tight engineering for a one-shot.

## Links

- [Source repository](https://github.com/markcastle/fliprunner)
- [Related link](https://github.com/markcastle/fliprunner/blob/master/README.md)
- [Related link](https://github.com/markcastle/fliprunner/blob/master/index.html)
