# CARVE LINE — Snowboard Downhill

[View source](https://github.com/TetrisSQC/carveline)

| Overall rating | Screenshot score |
| :---: | :---: |
| **53/100** | **Not scored** |

<details>
<summary>Read the scoring rationale</summary>

### Overall rating

Compared against the full catalog excluding the target: moorestech (64, broadest verified systems plus dense inspected 3D HUDs), Ashlands (55, current non-self top on systems scope), Kart Royale (50, complete polished single-track 3D racer with AI/HUD), and Turbo Kart Rally (40, complete single-circuit indie kart loop). CARVE LINE documents broader racing scope than both kart games (three 2.6-3.2 km courses, edge/grip carve model, tricks/combos/landing aid, 2 AI rivals plus ghost, gates/stars, skier traffic, resort/weather/day-night, character customization, dynamic music, PWA offline) with a credible single-file three.js plus Pascal-port architecture. Capped at mid-50s well below AAA because no gameplay screenshot or public playable build could be inspected (0 stars, 5 commits, created 26 Sep 2026, no homepage, no GitHub Pages), so visual polish, performance, balance, and the full race loop remain unverified from stills/source claims alone.

### Screenshot score

No inspectable gameplay screenshot.

</details>

## At a glance

| Detail | Value |
| --- | --- |
| Repository created | 26 Sep 2026 · 19:52 UTC |
| Added to catalog | 27 Sep 2026 · 06:15 UTC |
| Last updated | 27 Sep 2026 · 06:15 UTC |
| Documented creation models | [Claude Opus](https://github.com/TetrisSQC/carveline/blob/main/README.md) |

## Play

- Serve the folder over HTTP (for example \`python -m http.server 8000\`) and open it in a browser; \`file://\` does not work because of ES modules.
- Pick one of three courses (Classic 3.2 km, Waldpfad 2.6 km, Nordwand 2.8 km), then ride the countdown-to-finish downhill run and beat the per-course best time.
- Steer with A/D or arrows (left stick / side-stick on touch), crouch with W/Up, brake with S/Down, Ollie by holding and releasing Space, grab/flip/spin in the air, switch camera with C, pause with P/Esc.

## Mechanics

- Edge/grip/sidecut snowboard physics with carving, skidding, braking, Ollie charging, and push-to-start at very low speed
- Aerial tricks: spins, front/backflips, Indy grab with combo scoring plus an in-air landing aid
- Three courses with distinct width/grade/character, slalom gates with bonus/penalty time, collectible stars, and per-course best time
- AI rivals Mia and Tom on the same physics with nameplates, live/finish placement, and graded collisions; transparent ghost of personal best
- NPC skiers with near-miss scoring and slow motion; chairlifts, huts, hamlet with church, valley town, safety nets, day/night and snow/fog weather
- Procedural comic look: cel-shading, outline pass, bloom, color grading, three graphics presets with auto step-down; dynamic Web Audio music with crash/overtake/finish stingers

## Tags

- snowboard
- downhill
- racing
- sports
- 3d
- procedural
- comic
- cel-shading
- single-player
- pwa

## Controls

- Mobile controls: Supported
- Motion controls: Not established
- Gamepad: Supported
- Keyboard/mouse: Supported

## Player modes

- Human players: 1
- Modes: single-player

## Technologies

- **three.js 0.186.1** — rendering ([evidence](https://github.com/TetrisSQC/carveline/blob/main/index.html))
- **Web Audio API** — audio ([evidence](https://github.com/TetrisSQC/carveline/blob/main/downhill-music.js))
- **JavaScript** — language ([evidence](https://github.com/TetrisSQC/carveline/blob/main/index.html))
- **Quartex Pascal** — language ([evidence](https://github.com/TetrisSQC/carveline/blob/main/qtx/PORTING.md))

## Reconstructed prompt

Build a browser downhill snowboard game called CARVE LINE in comic cel-shaded style as a single index.html (no build step) using three.js via import map plus Web Audio dynamic music; include carve/grip sidecut physics, Ollie, spins/flips/grabs with combos and landing aid, 3 courses, AI rivals plus best-time ghost, slalom gates, stars, skier traffic with near-miss slow-mo, ski-resort world with lifts/villages, day/weather options, rider customization, keyboard/gamepad/touch controls, HUD/menus/pause/best times, and installable PWA offline support.

## Source evidence

- Repository TetrisSQC/carveline is public, not a fork, described as 'A downhill snowboard game'; default branch main; no homepage URL configured. ([source](https://github.com/TetrisSQC/carveline))
- Repo file list is index.html, downhill-music.js, PROMPT.md, README.md, manifest.webmanifest, sw.js, icons/, qtx/; recursive tree contains only app icons (192/512/maskable, apple-touch-icon, html5.png) and no gameplay screenshots. ([source](https://github.com/TetrisSQC/carveline))
- README documents the full game: comic-look browser snowboard downhill, single HTML file, procedural characters/trees/houses/terrain/textures/sound, installable PWA playable offline on desktop and phone. ([source](https://github.com/TetrisSQC/carveline/blob/main/README.md))
- README features list documents snowboard edge/grip/sidecut physics, spins/flips/Indy grab with combos and landing aid, 3 courses, AI rivals Mia and Tom on same physics, best-time ghost, slalom gates, stars, skiers with near-miss slow motion, lifts/huts/hamlet/valley town, noon/evening plus clear/snow/fog, rider color customization, dynamic music, cel-shading/outlines/bloom/grading with 3 presets. ([source](https://github.com/TetrisSQC/carveline/blob/main/README.md))
- README control table explicitly maps keyboard (A/D/arrows, W/S, Space, E/Shift, C, P/Esc), gamepad (left stick, RT/LT, A, X/RB, Y, Start), and touch (side stick, up/down stick, jump/grab/cam/pause buttons, virtual stick) plus responsive landscape phone layout. ([source](https://github.com/TetrisSQC/carveline/blob/main/README.md))
- README course table lists Classic 3.2 km, Waldpfad 2.6 km, Nordwand 2.8 km with widths, grades, and characters; start section requires a web server and first-run internet for three.js r0.186.1 via jsDelivr import map. ([source](https://github.com/TetrisSQC/carveline/blob/main/README.md))
- index.html import map pins three@0.186.1 module and three/addons paths and imports EffectComposer, RenderPass, UnrealBloomPass, SMAAPass, ShaderPass, OutputPass, and Sky addons. ([source](https://github.com/TetrisSQC/carveline/blob/main/index.html))
- GitHub Pages API returns 404 and repo metadata reports has\_pages false with homepage null, so no verified hosted playable URL; README only documents local \`python -m http.server\` play plus PWA install/offline caching. ([source](https://github.com/TetrisSQC/carveline))
- Inspected 512px app icon shows a chibi snowboarder carving with red trail, pines, and mountains; it is promotional/app icon art, not an inspectable gameplay screenshot, so no screenshot-based graphics score is given. ([source](https://github.com/TetrisSQC/carveline/blob/main/icons/icon-512.png))
- README Entstehung section explicitly attributes the entire JS game (code, shaders, models, physics, AI, PWA, README) exclusively to Claude Opus via Claude Code; qtx/PORTING.md further documents the Pascal port by Claude Opus through Claude Code using Quartex Pascal IDE MCP. ([source](https://github.com/TetrisSQC/carveline/blob/main/README.md))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 85/100: Fictional review: finally a browser carver with real edges — laying trenches down Classic at dusk while the ghost of my best run breathes down my neck is pure flow.
- 62/100: Fictional review: ambitious package with tricks, gates, and skiers everywhere, but without a demo to test the landings and frame pacing it reads better than it can prove.
- 95/100: Fictional review: three mountains, a living resort, and music that swells with every combo — the most complete arcade snowboard fantasy I have seen in a single HTML file.

## Links

- [Source repository](https://github.com/TetrisSQC/carveline)
