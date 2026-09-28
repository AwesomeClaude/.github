# Uplift (Windborne)

[View source](https://github.com/Starwaves1/Uplift)

| Overall rating | Screenshot score |
| :---: | :---: |
| **53/100** | **Not scored** |

<details>
<summary>Read the scoring rationale</summary>

### Overall rating

Deep custom tech for a days-old solo repo: WebGL2 CDLOD terrain, atmosphere and volumetric-cloud path, dual relaxed plus 6-DOF flight models, 14MB designed island with Python erosion pipeline, and generative audio. That scope exceeds Turbo Kart Rally (40, single-track kart demo), Beachy Beachy Ball (25, minimal runner) and 2048 (38, flat DOM), and sits near Ashlands (55) and OSRS Tower Defense (52) on ambition, but below moorestech (64, verified multiplayer factory sim with dense HUD gameplay frames). Capped well below AAA because no playable URL was established, no gameplay screenshot could be inspected, the author calls it low-ish effort, and playability, performance and balance are unverified from stills and source snippets alone.

### Screenshot score

No inspectable gameplay screenshot.

</details>

## At a glance

| Detail | Value |
| --- | --- |
| Repository created | 27 Sep 2026 · 01:57 UTC |
| Added to catalog | 27 Sep 2026 · 06:07 UTC |
| Last updated | 27 Sep 2026 · 06:07 UTC |
| Documented creation models | Not established |

## Play

- Open windborne.html from a local static server so it can fetch island.bin and island\_maps.bin from the same folder
- Click Take flight on the Windborne title screen
- Move the mouse to lean and pitch the glider
- Hold left mouse button for jet boost and hold right mouse button to look around
- Scroll to switch first-person or chase view; press C to toggle camera, H for HUD, Esc to pause
- Dive to gather speed, pull up to trade speed for height, and circle in rising air beneath clouds to climb while collecting seeds

## Mechanics

- Mouse-steered hang-glider soaring with bank, pitch, dive-for-speed and pull-up-for-height energy exchange
- Thermal, ridge-lift and coastal soaring over a large hand-designed procedural island
- Jet boost limited by a breath meter plus crash, splash, respawn-at-bookmark and invulnerability handling
- Two flight models: relaxed assisted model and realistic 6-DOF rigid-body model with stalls, spins and wing drops
- Seed collecting with best-seeds persistence and speed, altitude and variometer HUD
- Selectable morning, afternoon and dusk atmosphere with aerial-perspective haze and auto exposure
- First-person and chase cameras with pointer-lock and absolute-fallback mouse modes
- Quality, resolution, sensitivity, invert, units, physics, assists, volume, music and variometer settings
- Generative music tracks with shuffle and skip plus wind, jet, variometer and chime sound synthesis
- Separate Gravity Loom prototype: slingshot comet tether-swinging between worlds with stardust, pulse and hull modes

## Tags

- flight-simulator
- glider
- soaring
- exploration
- 3d
- webgl
- single-player
- procedural-island
- physics

## Controls

- Mobile controls: Not established
- Motion controls: Not established
- Gamepad: Not established
- Keyboard/mouse: Supported

## Player modes

- Human players: 1
- Modes: single-player

## Technologies

- **JavaScript** — language ([evidence](https://raw.githubusercontent.com/Starwaves1/Uplift/main/wind/main.js))
- **HTML** — language ([evidence](https://raw.githubusercontent.com/Starwaves1/Uplift/main/wind/shell.html))
- **Python** — language ([evidence](https://raw.githubusercontent.com/Starwaves1/Uplift/main/island/gen_island.py))
- **WebGL2** — rendering ([evidence](https://raw.githubusercontent.com/Starwaves1/Uplift/main/wind/core.js))
- **GLSL** — rendering ([evidence](https://raw.githubusercontent.com/Starwaves1/Uplift/main/wind/core.js))
- **Web Audio API** — audio ([evidence](https://raw.githubusercontent.com/Starwaves1/Uplift/main/wind/audio.js))
- **Custom flight physics** — physics ([evidence](https://raw.githubusercontent.com/Starwaves1/Uplift/main/wind/flight.js))
- **Shell** — build ([evidence](https://raw.githubusercontent.com/Starwaves1/Uplift/main/build-wind.sh))

## Reconstructed prompt

Build a single-file WebGL2 hang-glider soaring game called Windborne over a big hand-designed island with thermals, ridge lift, jet boost on a breath meter, seed collecting, chase and first-person cameras, morning/afternoon/dusk lighting, relaxed and realistic flight models, settings, HUD, and generative music and wind audio.

## Source evidence

- Repository Starwaves1/Uplift is described as Low-ish effort Opus 5.5 flight game with HTML as primary language ([source](https://github.com/Starwaves1/Uplift))
- Repo metadata: 0 stars, 0 forks, default branch main, created 2026-09-27, no homepage, has\_pages false, languages HTML/JavaScript/Python/Shell ([source](https://api.github.com/repos/Starwaves1/Uplift))
- CLAUDE.md defines Windborne/Updraft as a single-HTML WebGL2 glider game over a big hand-designed fantasy island, built from wind/ modules by build-wind.sh and served locally because the page fetches island.bin and island\_maps.bin ([source](https://raw.githubusercontent.com/Starwaves1/Uplift/main/CLAUDE.md))
- Title screen text: Windborne, lean with mouse to bank and carve, dive for speed, pull up for height, circle in rising air beneath clouds, Take flight, Move lean and pitch, Hold left jet boost, Hold right look around, Scroll first person or chase view ([source](https://raw.githubusercontent.com/Starwaves1/Uplift/main/windborne.html))
- Input code shows pointer-lock plus absolute mouse steering, left-button jet boost, right-button free look, wheel camera switch, and keyboard C/H/N/Esc handling; no touch, gamepad, or motion handlers found ([source](https://raw.githubusercontent.com/Starwaves1/Uplift/main/wind/main.js))
- Flight module implements relaxed lift/drag control-law model and realistic 6-DOF rigid-body model with stalls, spins, breath, crash/splash/respawn and wind sampling ([source](https://raw.githubusercontent.com/Starwaves1/Uplift/main/wind/flight.js))
- Core module requests webgl2 context and #version 300 es shaders with shared JS/GLSL noise and terrain functions ([source](https://raw.githubusercontent.com/Starwaves1/Uplift/main/wind/core.js))
- Audio module uses AudioContext with wind, jet, variometer, chime buses plus separate generative music module; test builds stay muted via WB\_MUTE ([source](https://raw.githubusercontent.com/Starwaves1/Uplift/main/wind/audio.js))
- Island generator is Python with numpy, scipy, torch and numba landscape evolution plus finalize/export stages writing island.bin and island\_maps.bin ([source](https://raw.githubusercontent.com/Starwaves1/Uplift/main/island/gen_island.py))
- build-wind.sh concatenates wind/\*.js modules into windborne.html; build.sh concatenates src/\*.js into gravity-loom.html ([source](https://raw.githubusercontent.com/Starwaves1/Uplift/main/build-wind.sh))
- Gravity Loom is a second pixel-art comet tether game in the same repo with HOLD LEFT catch, LET GO fling, RIGHT CLICK pulse modes ([source](https://raw.githubusercontent.com/Starwaves1/Uplift/main/gravity-loom.html))
- No GitHub Pages site and no verified public playable URL; Claude artifact link requires login and returns 403 anonymously ([source](https://github.com/Starwaves1/Uplift))
- No gameplay screenshots, previews, or image assets established in the inspected file listing; graphics could not be scored from stills ([source](https://github.com/Starwaves1/Uplift))
- No existing catalog entry matches Starwaves1/Uplift, Windborne, or Uplift; catalog comparison uses Moorestech 64, Ashlands 55, OSRS Tower Defense 52, Kart Royale 50, Turbo Kart Rally 40, 2048 38, Beachy Beachy Ball 25 ([source](https://github.com/Starwaves1/Uplift))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 82/100: Fictional review: I caught my first thermal off the eastern cliffs and just kept circling upward while the sun dropped — the quietest, most peaceful flying I have felt in a browser game.
- 64/100: Fictional review: Ambitious little soaring sim with real energy-management ideas and a huge island, but without a public build to try I cannot judge landings, balance, or performance.
- 95/100: Fictional review: The dusk ridge run with the generative score swelling underneath felt like the opening of an arthouse flight film. I stayed aloft far longer than I planned.

## Links

- [Source repository](https://github.com/Starwaves1/Uplift)
