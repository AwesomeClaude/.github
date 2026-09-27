# SpaceHo2

[Open the game source](https://github.com/PierreHoule/SpaceHo2)

**Overall rating:** 42/100. Far from AAA: single 30-star map config, 4 empires, no campaign, multiplayer, diplomacy, cinematics, voice, or live-ops scale; small ~180KB HTML/JS/CSS codebase from 7 commits with 0 stars, judged from source plus README only without playing. Most relevant comparators: neverquest (45 overall, deepest catalog systems scope with 8 attributes, 15+ stats, 9 crew roles, 100+ quests across ~591 files) and Turbo Kart Rally (40 overall, complete single-track 3D arcade loop with AI field, items, menus and procedural audio). SpaceHo2 matches Turbo Kart on finished-loop completeness (explore/settle/research/fight to elimination, AI rivals, fog of war, tech obsolescence, two automated test suites) and rivals neverquest on strategic systems breadth (suitability economy, terraforming, mining, 6 tech tracks, 6 ship types, range/speed logistics), but its content breadth is narrower than neverquest's long-tail progression and its presentation is unverified 2D canvas versus Turbo Kart's inspected 3D world. Above Taipo (35, complete typing-TD loop but one small tilemap with acknowledged placeholder art/sound TODOs), Neural Sight (30, photographic prototype with almost no game loop), TypeScript-Blackjack (28, faithful single-table card rules but flat DOM), Beachy Beachy Ball (25, single roll-to-star mechanic with minimal art), and curiositY (18, static riddle pages). Evidence gaps: no screenshots or video inspected, no live playtest, so playability, balance, pacing, and rendering performance are unverified; source and text descriptions do not prove graphics quality or fun.

**Screenshot score:** not scored. No inspectable gameplay screenshot.

## Play

- Download or open index.html in a browser (fully self-contained, no build step); optionally add #seed=1234 to the URL to replay a specific galaxy.
- You command the blue empire against three AI rivals (Zorgon, Krell, Vexis); last empire standing wins.
- Click star systems on the animated canvas map to select planets; surveyed worlds show temperature-shaded spheres, ownership rings (solid = live intel, dashed = old survey), hats on your worlds, and chevrons counting parked ships.
- Build Scouts to explore and refresh intel, Colony Ships to settle uninhabited worlds, Satellites to defend, and Fighters / Destroyers / Dreadnoughts to fight; select ships, arm send mode, then click a destination star.
- Set per-planet terraforming and mining budgets, queue ships in the shipyard, and fund six research tracks (Range, Speed, Weapons, Shields, Miniaturization, Radical) via the tech panel.
- Press Ho! (or Enter) to end your turn and let the three AIs move; Esc or right-click cancels a fleet order; read turn reports for battles, bombardments and colonies.
- Expand to high-suitability worlds, mine metal for shipbuilding, obsolete old hulls with new tech, bombard undefended enemy worlds, and eliminate every rival empire.

## Mechanics

- Turn-based 4X loop (explore, expand, exploit, exterminate) on a 30-star seeded galaxy, you plus 3 AI empires, elimination victory
- Planet suitability from homeworld ideal temperature and gravity drives population growth and income; 0-100 temperature, 0.3-2.5g gravity, metal reserves
- Terraforming budget moves temperature toward ideal (gravity immutable); mining budget converts reserves to metal with galactic-market markup when dry
- Six research tracks (Range, Speed, Weapons, Shields, Miniaturization, Radical) with radical-discounted costs; ships retain build-time tech so hulls go obsolete
- Six ship types: Scout, Colony Ship, Satellite, Fighter, Destroyer, Dreadnought with tech-scaled attack/HP/speed/range, cost and metal
- Automatic combat when rival fleets share a system; orbiting warships bombard undefended enemy population
- Fog of war with last-survey snapshots; dashed ownership rings for stale intel versus solid rings for live intel
- Fleet dispatch with range limits, dashed courses, engine trails, and map bursts for battles, bombardments and colonies
- AI opponents managing research budgets, planet budgets, colony/scout/warship builds, scouting patrols and warfare
- Seeded galaxy generation with reproducible PRNG, well-separated homeworlds, and minimum star distance

## Tags

- 4x
- strategy
- turn-based
- space
- browser-game
- html5-canvas
- vanilla-js
- single-player
- ai-opponents
- fog-of-war
- single-file

## Reconstructed prompt

Build SpaceHo2, a browser tribute to Spaceward Ho! in pure HTML5 canvas + vanilla JS with no dependencies: seeded 30-star galaxy, you plus 3 AI empires, last-empire-standing wins. Planets with temperature/gravity/metal and homeworld-based suitability driving growth and income; terraform temperature, mine metal with market markup, six research tracks with hull obsolescence; six ship types (scout, colony, satellite, fighter, destroyer, dreadnought), automatic combat, bombardment, fog of war with stale-survey dashed rings. Animated device-resolution star map (temperature-shaded spheres, polar caps, city lights, ownership rings, hats, chevrons, fleet trails, battle bursts) plus side panels (planet/shipyard, tech sliders, empire standings, reports), Ho!/Enter end turn, Esc cancel, #seed replay. Single self-contained index.html built by node build.js from css/js sources; DOM-free testable model with AI-vs-AI smoke sims and jsdom UI tests.

## Source evidence

- Repo is PierreHoule/SpaceHo2, described as 'Second attempt to clone the game, this time with Fable 5', language HTML, 0 stars, 0 forks, created 2026-06-12, pushed 2026-07-25, MIT license. ([source](https://github.com/PierreHoule/SpaceHo2))
- README describes a browser-based tribute to Spaceward Ho! in pure HTML5 canvas + vanilla JS with no build step and no dependencies; open index.html which is fully self-contained. ([source](https://raw.githubusercontent.com/PierreHoule/SpaceHo2/main/README.md))
- Player commands the blue empire against three AI rivals; last empire standing wins; Ho!/Enter ends turn, Esc cancels fleet orders, #seed=1234 replays a galaxy. ([source](https://raw.githubusercontent.com/PierreHoule/SpaceHo2/main/README.md))
- Planets have temperature, gravity, metal reserves; suitability vs homeworld ideal drives growth and income; terraforming shifts temperature only; mining converts reserves to metal with steep market markup when dry. ([source](https://raw.githubusercontent.com/PierreHoule/SpaceHo2/main/README.md))
- Six research tracks (Range, Speed, Weapons, Shields, Miniaturization, Radical) with ships keeping build-time tech so old hulls go obsolete; six ship types with scouts, colony ships, satellites, fighters/destroyers/dreadnoughts, automatic combat and bombardment. ([source](https://raw.githubusercontent.com/PierreHoule/SpaceHo2/main/README.md))
- Fog of war shows live data only with owned planet or ship present, otherwise last survey shown as dashed rings; map legend covers unsurveyed points of light, temperature-shaded lit spheres with polar caps and city lights, ownership rings, hats, chevrons, fleet trails and event bursts. ([source](https://raw.githubusercontent.com/PierreHoule/SpaceHo2/main/README.md))
- Static data defines 30-star 1000x760 galaxy with 70-unit minimum separation, 4 default empires, economy constants, six tech costs and six ship stat blocks scaled by tech. ([source](https://raw.githubusercontent.com/PierreHoule/SpaceHo2/main/js/data.js))
- Model implements seeded Mulberry32 galaxy generation, separated homeworld picks, home fleets, per-player known snapshots, and DOM-free Game class testable headless. ([source](https://raw.githubusercontent.com/PierreHoule/SpaceHo2/main/js/model.js))
- AI module manages research budgets, planet terraform/mining budgets, colony/scout/satellite/warship builds, scout patrols and warship moves across all empires. ([source](https://raw.githubusercontent.com/PierreHoule/SpaceHo2/main/js/ai.js))
- Top-level file listing is only .gitignore, LICENSE, README.md, build.js, dev.html, index.html (~85KB) plus css/, js/ (ai, data, main, model, ui), test/ (smoke, ui.test); no image or screenshot assets exist and index.html contains no img/screenshot references. ([source](https://github.com/PierreHoule/SpaceHo2))
- Commit history has 7 commits including AI-branch merges for the initial SpaceHo! clone, a self-contained single-file build, and a star-map visual overhaul; headless smoke test sims full AI-vs-AI games across 5 seeds and asserts expansion, research and wins. ([source](https://raw.githubusercontent.com/PierreHoule/SpaceHo2/main/test/smoke.js))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 75/100: \[Fictional review\] Imagined 4X fan: seeding a galaxy, terraforming a frozen rock toward my ideal temp while my scouts keep the dashed-ring intel fresh, then watching a dreadnought fleet glide in with engine trails — scrappy but genuinely Spaceward Ho.
- 55/100: \[Fictional review\] Made-up casual player note: the Ho! turn loop, six tech tracks and obsolete hulls are clever, but one 30-star map, no diplomacy or multiplayer, and canvas circles instead of real planets make long wars blur together.
- 100/100: \[Fictional review\] Invented minimalist-dev take: DOM-free model with AI-vs-AI smoke sims, jsdom UI tests, seeded galaxies and a single self-contained HTML file with zero dependencies? Tiny, testable, and charmingly complete.

## Links

- [Source repository](https://github.com/PierreHoule/SpaceHo2)
- [Related link](https://raw.githubusercontent.com/PierreHoule/SpaceHo2/main/README.md)
- [Related link](https://raw.githubusercontent.com/PierreHoule/SpaceHo2/main/js/model.js)
- [Related link](https://raw.githubusercontent.com/PierreHoule/SpaceHo2/main/js/ai.js)
- [Related link](https://raw.githubusercontent.com/PierreHoule/SpaceHo2/main/js/data.js)
- [Related link](https://raw.githubusercontent.com/PierreHoule/SpaceHo2/main/test/smoke.js)
