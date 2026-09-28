# HOMUNCULUS

[View source](https://github.com/Efkrdnz/opus-test-game)

| Overall rating | Screenshot score |
| :---: | :---: |
| **49/100** | **55/100** |

<details>
<summary>Read the scoring rationale</summary>

### Overall rating

Far from AAA: flat 2D vector presentation, no multiplayer, no voice or cinematics, zero stars, unreleased single-author test project with no hosted playable build to verify performance, balance or pacing. Most relevant comparators excluding the target: neverquest (45 overall, deepest prior systems scope with 8 attributes and 100+ quests but monochrome text UI only), THORNMERE (46, broadest retro-RPG package with 57 monsters and 84 spells), The Nine Lives of Ash (47, deep deckbuilder rules core with tests but local-only), Kart Royale (50, complete polished 3D loop on a single track), and OSRS Tower Defense (52, 12 towers and 61 monsters plus 130 waves with dense 2D scenes). HOMUNCULUS exceeds neverquest and THORNMERE on simulation breadth (120 reagents, 37 recipes, 87 effects, 43 diseases, fixed-step physiology plus chemistry, pharmacology, behaviour and environment models, all covered by a node:test suite with DOM-free sim core), but trails Kart Royale and OSRS Tower Defense on verified pick-up-and-play completeness and moment-to-moment action feel, and sits far below moorestech (64, catalog top on systems plus co-op, story and mod tools). Evidence gaps: judged from GitHub API metadata, raw files and one inspected still only; the self-contained dist build was not executed, so playability, performance and balance are unverified and not proven by code or screenshots.

### Screenshot score

The single inspected frame is the game's own runtime output with coherent stylized flat-vector anatomy across six layers, clean silhouettes and consistent chamber staging. Against catalog calibration it sits with Taipo (55, sparse flat pixel TD board) and below THORNMERE (60, textured viewport plus detailed portraits) and OSRS Tower Defense (65, dense 2D scene with HUD), and far below the catalog 70s (Kart Royale, Turbo Kart Rally, Neural Sight) with 3D lighting and scenery; well above neverquest (30) and TypeScript-Blackjack (35) flat DOM dashboards on scene composition. Only one still inspected and it lacks HUD, monitor and effects views, so no motion, feel, performance or balance is inferred.

</details>

## At a glance

| Detail | Value |
| --- | --- |
| Repository created | 26 Sep 2026 · 15:34 UTC |
| Added to catalog | 27 Sep 2026 · 06:04 UTC |
| Last updated | 27 Sep 2026 · 06:04 UTC |
| Documented creation models | Not established |

## Screenshots

![HOMUNCULUS gameplay](screenshots/2d2c6537953a472f5184f64c6470b9325dfac3f8ad0f0db2268ac02bb75f24f4.png)

Inspected downloaded copy of docs/layers.png: six full-body figures side by side on a dark chamber background with hazard-stripe floor, showing skin, muscle, circulatory, organs, skeleton and nervous layers in flat vector style; the game's own runtime output, no HUD or monitor visible in this frame.

[Original screenshot](https://raw.githubusercontent.com/Efkrdnz/opus-test-game/claude/affectionate-fermat-tluz0w/docs/layers.png)

## Play

- Open dist/homunculus.html in a modern browser, or run npm start and open http://localhost:8080
- Click reagents on the shelf to pour 10 ml doses into the flask
- Set burner temperature, stir mode, steeping time and treatments, then brew
- Choose an administration route, site and dose, then administer to the subject
- Observe the chamber layers and bedside monitor waveforms and tabs
- Issue commands with keys (W walk, R run, J jump, L lift, P punch, Q solve) or typed commands; Space pauses, 1-6 switch anatomy layers

## Mechanics

- Pour and brew 120 reagents across 5 categories with burner, stir, steep and 12 treatments
- Real pH mixing and neutralisation plus 24 aspect-driven reaction rules and 37 discoverable recipes
- Ten administration routes with dose scaling, contact temperature and pH injury, and embolism risk
- Full body simulation at fixed 0.1 s steps: heart rhythm, blood pressure, breathing, SpO2, temperature, glucose, 13 organs, 10 brain regions, 8 neurotransmitters, nerves, muscles, 16 bones
- 87 effect types, 43 staged diseases, and transformations including stone, zombie, werewolf, vampire, ghost, crystal, metal, gold, rubber and divine
- Six peelable anatomy layers with X-ray, thermal and damage overlays plus hover-to-inspect body parts
- Bedside monitor with 8 vital tiles with alarms, ECG and pleth and respiration and EEG sweeps, and system tabs
- 24 subject commands gated by hearing, comprehension, willingness and ability, with obedience, involuntary behaviour and brain-state-dependent speech
- Measured performance tests per command with numbers and baselines, plus environment controls for air temperature, gravity, oxygen and radiation
- Defibrillator, stabilisation, dialysis, full restore and new-subject tools; localStorage persistence of cabinet and discoveries

## Tags

- sandbox
- simulation
- alchemy
- sci-fi
- educational
- single-player
- browser
- 2d

## Controls

- Mobile controls: Not established
- Motion controls: Not established
- Gamepad: Not established
- Keyboard/mouse: Supported

## Player modes

- Human players: 1
- Modes: single-player

## Technologies

- **JavaScript** — language ([evidence](https://api.github.com/repos/Efkrdnz/opus-test-game/languages))
- **HTML** — language ([evidence](https://raw.githubusercontent.com/Efkrdnz/opus-test-game/claude/affectionate-fermat-tluz0w/index.html))
- **CSS** — language ([evidence](https://raw.githubusercontent.com/Efkrdnz/opus-test-game/claude/affectionate-fermat-tluz0w/index.html))
- **Canvas 2D** — rendering ([evidence](https://raw.githubusercontent.com/Efkrdnz/opus-test-game/claude/affectionate-fermat-tluz0w/js/render/scene.js))
- **Web Audio** — audio ([evidence](https://raw.githubusercontent.com/Efkrdnz/opus-test-game/claude/affectionate-fermat-tluz0w/js/ui/audio.js))
- **Node.js \>=18** — build ([evidence](https://raw.githubusercontent.com/Efkrdnz/opus-test-game/claude/affectionate-fermat-tluz0w/package.json))

## Reconstructed prompt

Build a self-contained browser sandbox game called HOMUNCULUS, an alchemy and clinical observation lab: 120 reagents in 5 categories, a flask bench with burner/stir/steep/12 treatments, real pH mixing and aspect-driven reactions with 37 discoverable recipes, 10 administration routes into a fully simulated homunculus (heart, lungs, organs, brain regions, neurotransmitters, nerves, muscles, bones), 87 effects, 43 diseases, transformations and mutations, 6 peelable anatomy layers with overlays, a bedside monitor with vitals and waveforms, 24 obey-or-refuse subject commands recorded as performance tests, environment controls, rescue tools, localStorage persistence, keyboard controls, and a node:test suite over a DOM-free simulation core bundled into one dist HTML file with no npm dependencies.

## Source evidence

- Repository Efkrdnz/opus-test-game is public, not a fork, default branch claude/affectionate-fermat-tluz0w, primary language JavaScript, 0 stars, 0 forks, no homepage, Pages disabled. ([source](https://api.github.com/repos/Efkrdnz/opus-test-game))
- README titles the game HOMUNCULUS, an alchemy and clinical observation lab about brewing mixtures and testing them on a simulated homunculus with a live clinical monitor, and documents Play via dist/homunculus.html with no install or npm start on localhost:8080. ([source](https://github.com/Efkrdnz/opus-test-game/blob/claude/affectionate-fermat-tluz0w/README.md))
- README documents game systems: 120 reagents, bench with burner/stir/steep/12 treatments, pH mixing with 24 reaction rules and 37 recipes, 10 administration routes, body model with heart rhythm, pressure, breathing, SpO2, 13 organs, 10 brain regions, 8 neurotransmitters, nerves, muscles, 16 bones, 87 effects, 43 diseases, transformations, 6 anatomy layers with overlays, 24 commands, 8-tile monitor with waveforms, environment controls and rescue tools. ([source](https://github.com/Efkrdnz/opus-test-game/blob/claude/affectionate-fermat-tluz0w/README.md))
- README Controls section lists keyboard bindings: Space pause, 1-6 anatomy layers, W/R/J/L/P/K/D/B/T/Q action keys, arrow keys to move, plus typed commands such as say hello or sprint. ([source](https://github.com/Efkrdnz/opus-test-game/blob/claude/affectionate-fermat-tluz0w/README.md))
- chamber.js registers a document keydown handler mapping Space, 1-6 and command keys, and canvas click plus button click handlers for layers, tools and inspection, evidencing keyboard and mouse input; no touch joystick, gamepad or motion handlers found. ([source](https://raw.githubusercontent.com/Efkrdnz/opus-test-game/claude/affectionate-fermat-tluz0w/js/ui/chamber.js))
- DESIGN.md describes the core loop (pour, brew, administer, observe, command, learn), fixed 0.1 s simulation steps, DOM-free sim core runnable headless in Node, and the chemistry, pharmacology, body, behaviour and rendering models. ([source](https://raw.githubusercontent.com/Efkrdnz/opus-test-game/claude/affectionate-fermat-tluz0w/docs/DESIGN.md))
- package.json names the project homunculus-lab 1.0.0, type module, zero npm dependencies, scripts for serve/build/test, and engines node \>=18. ([source](https://raw.githubusercontent.com/Efkrdnz/opus-test-game/claude/affectionate-fermat-tluz0w/package.json))
- Repository tree contains index.html, css, js/data, js/sim, js/render, js/ui, scripts, tests and a 561004-byte dist/homunculus.html self-contained build; no hosted playable URL, releases or deployments verified. ([source](https://api.github.com/repos/Efkrdnz/opus-test-game/contents/dist?ref=claude/affectionate-fermat-tluz0w))
- audio.js implements optional monitor sounds via AudioContext with pulse-oximeter pitch tied to SpO2, flatline tone and lab effects, evidencing Web Audio usage. ([source](https://raw.githubusercontent.com/Efkrdnz/opus-test-game/claude/affectionate-fermat-tluz0w/js/ui/audio.js))
- No verified catalog match: no existing game directory or report references Efkrdnz or opus-test-game; scoring calibrated against moorestech (64), OSRS Tower Defense (52), Kart Royale (50), The Nine Lives of Ash (47), THORNMERE (46) and neverquest (45). ([source](https://github.com/AwesomeClaude/.github))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 85/100: Poured moonlight-treated werewolf saliva into my test subject and it actually started howling at the monitor. The six-layer anatomy peel is the best mad-science toy I have used all year.
- 60/100: Fascinating simulation buried in a stark lab UI. Brewing and dosing is fun, but long stretches are just watching waveforms drift while the little fellow refuses to cooperate.
- 100/100: Injected liquid nitrogen, froze the subject solid, thawed it back, and the ECG came back to life. I have never felt more like a genius or more like a monster.

## Links

- [Source repository](https://github.com/Efkrdnz/opus-test-game)
- [Repository README](https://github.com/Efkrdnz/opus-test-game/blob/claude/affectionate-fermat-tluz0w/README.md)
- [Design document](https://github.com/Efkrdnz/opus-test-game/blob/claude/affectionate-fermat-tluz0w/docs/DESIGN.md)
