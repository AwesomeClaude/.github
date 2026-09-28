# DRIFTWING

[Play the game](https://kylebuildsai.github.io/driftwing/) · [View source](https://github.com/KyleBuildsAI/driftwing)

| Overall rating | Screenshot score |
| :---: | :---: |
| **52/100** | **72/100** |

<details>
<summary>Read the scoring rationale</summary>

### Overall rating

Excluding the target, most relevant comparators are Kart Royale (50 overall / 70 screenshots: complete polished 3D loop but single 1.6km track), Turbo Kart Rally (40/70: full kart loop with items and AI but single circuit and simple art), Neural Sight (30/70: striking 3D output but narrow prototype scope), and moorestech (64/76: broadest verified systems and densest HUDs, current catalog top). DRIFTWING sits above the kart racers on technical scope (infinite seeded worker terrain with LOD, WebGPU+WebGL2, day/night/aurora/weather/water/boids, voice copilot with executable actions, rings/journal/photo mode) and stronger atmospheric polish in both inspected stills, but below moorestech and Ashlands (55) on gameplay depth since it is deliberately ambient with no fail state, enemies, progression, or multiplayer. Evidence gaps: gh api unavailable (no token, rate-limited) so commit/version history unverified; no GPU-backed live playtest, performance, audio, balance, or motion verification; screenshots show only snow biome without UI, landmarks, or vegetation detail.

### Screenshot score

Both inspected frames are the game's own runtime output with coherent flat-shaded low-poly style, strong sky work (golden-hour sun with god rays; night aurora with stars and wingtip lights) and clean composition centered on the glider. Above Kart Royale (screenshots 70) and Turbo Kart Rally (70) on lighting/atmosphere cohesion, and above Neural Sight (70) on composed game framing, but below moorestech (76) because only one snow-peaks biome is visible with no trees, water, landmarks, birds, rings, or HUD/UI density in either still. Stills cannot prove motion, performance, or feel.

</details>

## At a glance

| Detail | Value |
| --- | --- |
| Repository created | 26 Sep 2026 · 17:46 UTC |
| Added to catalog | 27 Sep 2026 · 06:13 UTC |
| Last updated | 27 Sep 2026 · 06:13 UTC |
| Documented creation models | [Claude Opus 5.5](https://github.com/KyleBuildsAI/driftwing) |

## Screenshots

![DRIFTWING gameplay](screenshots/19e1980fbc01b3b82335a13685bfa95fa3591374bc20653598f703d4508c43e8.jpg)

Inspected downloaded copy of docs/screenshot.jpg (1600x900): chase view directly behind a white low-poly glider with orange wingtip marks flying between jagged dark snow peaks at golden hour; warm orange-pink gradient sky, bright sun disc with radial god-ray streaks upper right, soft clouds, flat-shaded white/grey terrain with long shadows. No HUD visible (auto-hide). Clearly the game's own runtime output.

[Original screenshot](https://raw.githubusercontent.com/KyleBuildsAI/driftwing/main/docs/screenshot.jpg)

![DRIFTWING gameplay](screenshots/8565ac163e2b4542b8688df0e47758b63a1ec090736904b8669f0870c4853d3d.jpg)

Inspected downloaded copy of docs/screenshot-night.jpg (1600x900): same white glider from behind over dark low-poly snow spires at night under vivid green aurora curtains, scattered stars and soft clouds; red left and green right wingtip lights visible, cool blue-grey flat-shaded terrain. No HUD visible. Clearly the game's own runtime output, companion night/aurora showcase to the day shot.

[Original screenshot](https://raw.githubusercontent.com/KyleBuildsAI/driftwing/main/docs/screenshot-night.jpg)

## Play

- Open https://kylebuildsai.github.io/driftwing/ in a WebGPU or WebGL2 browser; the game opens already airborne at golden hour after a short fade with no menu wall.
- Steer pitch and bank with the mouse (click to capture, Esc releases) or drag, or use A/D and arrow keys; banking turns the glider and wings level when released.
- Control speed with W/S or the mouse wheel, press Space for a cooldown boost, double-tap A or D for a barrel roll, Q/E for rudder and hold Shift for fine control.
- Press C, Enter or / to ask WREN (or M/mic button for voice): try 'find mountains', 'set waypoint', 'autopilot on', 'make it night', 'ring course'.
- Press R to start or cancel a fly-through ring course, G to drop a waypoint ahead (X clears), O for autopilot, T to cycle time of day.
- Press P for photo mode (WASD/QE move, mouse look, wheel zoom, K captures), J for the discovery journal, H for help, I/Tab for stats/HUD.
- Share a world by copying the URL since it always carries the seed, e.g. ?seed=D27TEH or ?seed=ARCH1&time=0.02.

## Mechanics

- Arcade glider flight with banking-induced yaw, climb/dive speed exchange, soft stall, chase cam with speed FOV and shake
- Infinite seeded simplex-noise chunked terrain with ring LOD, skirts, pooled meshes and Web Worker generation
- Five blended low-poly biomes: snow peaks, pine valleys, dune sea, archipelago ocean, flower meadows
- Procedural landmarks every few km: stone arches, monolith circles, island lighthouses, drifting hot-air balloons
- Day/night cycle with sun, moon, stars, aurora, god rays, matched fog, drifting instanced clouds, animated water with glint and shoreline foam
- Boid bird flocks that scatter, wingtip contrails, wind streaks, bloom/vignette/grade/grain post stack
- WREN AI copilot with local keyword grammar plus speech recognition/synthesis and optional remote endpoint with 800ms fallback
- Copilot actions: waypoint beacons, autopilot headings, time-of-day changes, ring-course spawning, biome/altitude narration
- Optional ring courses with chime feedback, times and best streaks; discovery journal with biomes, landmarks, distance and altitude
- Photo mode with free camera, hidden UI, letterbox and screenshot capture; deterministic shareable seeds

## Tags

- flight
- exploration
- ambient
- procedural-generation
- low-poly
- threejs
- webgpu
- webgl
- browser-game
- single-player
- ai-copilot
- glider

## Controls

- Mobile controls: Supported
- Motion controls: Not established
- Gamepad: Not established
- Keyboard/mouse: Supported

## Player modes

- Human players: 1
- Modes: single-player

## Technologies

- **three.js r184** — engine ([evidence](https://github.com/KyleBuildsAI/driftwing))
- **JavaScript** — language ([evidence](https://github.com/KyleBuildsAI/driftwing))
- **WebGPU** — rendering ([evidence](https://github.com/KyleBuildsAI/driftwing))
- **WebGL2** — rendering ([evidence](https://github.com/KyleBuildsAI/driftwing))
- **Web Workers** — framework ([evidence](https://github.com/KyleBuildsAI/driftwing))

## Reconstructed prompt

Build DRIFTWING, an ambient infinite-flight exploration browser game in a single index.html with no build step: three.js WebGPU with WebGL2 fallback via CDN import map; arcade glider flight (mouse + WASD/arrows, throttle, boost, banking turns, stall, barrel rolls, chase cam); infinite seeded simplex-noise chunked terrain in Web Workers with LOD/skirts, 5 blended low-poly biomes and procedural landmarks with discovery journal; day/night cycle with sun/moon/stars/aurora/god-rays, clouds, water, birds, contrails; keyword/voice AI copilot with waypoint/autopilot/time/ring-course actions plus remote endpoint fallback; optional ring courses, journal, photo mode; golden-hour glass UI, bloom/vignette/grade/grain post stack, 60fps governor, touch joystick support, deterministic shareable seeds.

## Source evidence

- Repository is an actual game: DRIFTWING, an ambient infinite-flight exploration game in a single index.html where you pilot a low-poly glider over an endless procedural world with no fail state, no fuel and no enemies, plus an AI copilot named WREN. ([source](https://github.com/KyleBuildsAI/driftwing))
- Engine is three.js r184 with WebGPURenderer and automatic WebGL2 fallback loaded from a CDN import map with SHA-384 integrity checks; there is no build step and r184 is deliberately pinned. ([source](https://github.com/KyleBuildsAI/driftwing))
- World is chunked heightmap terrain from seeded simplex noise generated in Web Workers with transferable buffers, ring LOD with skirts and pooled meshes, five blended biomes (snow peaks, pine valleys, dune sea, archipelago, flower meadows), deterministic shareable seeds, and procedural landmarks (stone arches, monolith circles, lighthouses, hot-air balloons) logged to a discovery journal. ([source](https://github.com/KyleBuildsAI/driftwing))
- Keyboard/mouse controls are established: mouse steers pitch and roll (click to capture, Esc releases) or drag, WASD/arrows work, W/S or wheel throttle, Space boost on cooldown, double-tap A/D barrel roll, plus keys C/Enter// for WREN, P photo mode, J journal, H help, T time, R rings, G/X waypoint, O autopilot, V voice, I/Tab stats/HUD. ([source](https://github.com/KyleBuildsAI/driftwing))
- Touch controls are established: virtual left joystick for pitch/bank plus right throttle slider and on-screen Boost, roll, WREN and menu buttons; ?touch=1 forces on-screen touch controls. ([source](https://github.com/KyleBuildsAI/driftwing))
- Single-player structure is established: one pilot glider, optional ring courses, discovery journal (biomes, landmarks, distance, altitude), photo mode, day/night cycle and copilot actions; no multiplayer, co-op, versus, or human-player-count range is documented. ([source](https://github.com/KyleBuildsAI/driftwing))
- Game is publicly playable at GitHub Pages https://kylebuildsai.github.io/driftwing/ with seed/time/renderer/debug/touch URL parameters and example worlds ?seed=D27TEH (golden hour) and ?seed=ARCH1&time=0.02 (night aurora); the live page renders the full DRIFTWING HUD, settings, journal, help and WREN command bar. Locally it runs by double-clicking index.html or npm run serve on localhost:8080. ([source](https://kylebuildsai.github.io/driftwing/))
- Project is explicitly a single-shot prompt test of Claude Opus 5.5 built from one prompt with no human code edits; gh api could not be used in this runner (no GH\_TOKEN and unauthenticated REST was rate-limited), so the public repository page, raw screenshots and live playable page were inspected instead and no source files were cloned. ([source](https://github.com/KyleBuildsAI/driftwing))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 85/100: Fictional review: I loaded the golden-hour seed just to check the lighting and ended up gliding for twenty minutes while WREN found me a lighthouse. No score, no crash, just wind and sun — the calmest tab I own.
- 60/100: Fictional review: Made-up weekend pilot note: gorgeous sky and clever copilot tricks, but I wished the rings and journal pushed back a little more. Lovely to drift in, easy to put down.
- 100/100: Fictional review: Invented dev-fan take: one HTML file that streams endless mountains, auroras, balloons and a talking copilot without a build step? As a single-prompt artifact this feels absurd and wonderful.

## Links

- [Source repository](https://github.com/KyleBuildsAI/driftwing)
- [Play the game](https://kylebuildsai.github.io/driftwing/)
