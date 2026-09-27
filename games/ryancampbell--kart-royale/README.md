# Kart Royale

[Open the game source](https://github.com/ryancampbell/kart-royale)

**Overall rating:** 50/100. Strong technical execution for a 4-day multi-agent demo (~60k lines, kart physics, AI, synthesis, test harnesses) and cohesive indie visuals, but single 1.6km track, thin drift-skill ladder per author's own 62/100 vs Mario Kart measurement, known mobile/iGPU gaps and dead post-FX chain for rounds. Evidence gaps: judged only 2 still screenshots plus source via gh api, did not play live build, no video/menus/results flow inspected, no low-end performance data.

**Screenshot score:** 70/100. Both gameplay frames show coherent stylized golden-hour art: banked tarmac with aggregate detail, red-white kerbs, grass/crowd/props trackside, glossy chunky karts with drivers, full kart-racer HUD. Composition is dynamic with strong sense of speed. Deducted for low-poly blocky crowd, flat distant foliage, dark crushed tarmac, and heavy blur obscuring detail in drift shot. Good polished indie look, not photoreal AAA.

## Screenshots

![Inspected 1920x1080 gameplay frame: chase view behind red kart chasing blue kart on wide sunset tarmac, red-white kerbs, crowd figures and grass left, AMALFI/TURBO signs, cliffs and sea right, HUD with LAP 1/3, 2nd place +0.20 vs KOA, minimap, 0:04.91 timer, item icon, 88 KM/H speedometer. Sharpest and most detailed inspected frame, clearly the game's own runtime output.](https://raw.githubusercontent.com/ryancampbell/kart-royale/main/docs/hero-coast.png)

Inspected 1920x1080 gameplay frame: chase view behind red kart chasing blue kart on wide sunset tarmac, red-white kerbs, crowd figures and grass left, AMALFI/TURBO signs, cliffs and sea right, HUD with LAP 1/3, 2nd place +0.20 vs KOA, minimap, 0:04.91 timer, item icon, 88 KM/H speedometer. Sharpest and most detailed inspected frame, clearly the game's own runtime output.

![Inspected 1280x720 gameplay frame: red kart mid-drift on kerb edge emitting orange sparks and smoke, motion blur and speed lines, crowd and hillside left, rival karts ahead, HUD with LAP 1/3, 2nd place -0.84, minimap, 0:10.25 timer, 101 KM/H. Same runtime procedural style as above but softer/blurrier from drift effects. Game's own output, not reference art.](https://raw.githubusercontent.com/ryancampbell/kart-royale/main/docs/hero-drift.png)

Inspected 1280x720 gameplay frame: red kart mid-drift on kerb edge emitting orange sparks and smoke, motion blur and speed lines, crowd and hillside left, rival karts ahead, HUD with LAP 1/3, 2nd place -0.84, minimap, 0:10.25 timer, 101 KM/H. Same runtime procedural style as above but softer/blurrier from drift effects. Game's own output, not reference art.

## Play

- Open https://racing.ryancampbell.com in a desktop browser, or run locally with npm install then npm run dev at http://localhost:5173.
- Hold throttle (ArrowUp/W) through the countdown lights: release timing earns a rocket start, holding too long causes a burnout spin.
- Steer with ArrowLeft/ArrowRight or A/D, accelerate with ArrowUp/W, brake with ArrowDown/S; race 3 laps against 7 AI karts on Sunset Bay Circuit.
- Hold Shift while steering to drift; keep the slide to charge blue/orange/purple mini-turbo tiers, then release for a boost — drifting lines are measurably faster.
- Drive through item-box rows to spin the roulette, then press Space/Enter/E to fire: leaders get defensive shells/bananas, trailers get mushrooms/star/bolt; press with reverse to trail behind as a shield.
- Follow checkpoints in order — cutting corners does not advance position; go off-track or get stuck and you respawn via crane drop after ~1.5s off-track.
- Finish 3 laps to see results; press R in dev console to record .webm, use ?quality=low\|medium\|high\|ultra and ?debug=gl flags if needed.

## Mechanics

- Drift into tiered mini-turbo boost with drift-carry window preserving charge over brief slide dips
- Slip-angle tyre model with raycast suspension, surface zones (road/dirt/grass/sand/boost) altering grip, drag and top speed
- Position-weighted item distribution with hold-behind shield play, floating item boxes in full-width rows
- Rocket start vs burnout on the start lights, countdown state machine with grid formation behind the line
- Checkpoint-validated lap/progress and anti-cut placement (lap x length + checkpoint anchor), wall collision and OOB/stuck respawn
- Racing-line AI field of 8 distinct karts with accel/top-speed/handling/weight roster stats
- Boost pads, tunnel sodium lighting section, banked 20-degree coastal curve and off-camber village corner
- Chase camera with lag/swing tuning, minimap with live dots, rival interval delta, speedometer and item roulette HUD

## Tags

- kart-racer
- racing
- 3d
- threejs
- webgl
- browser-game
- procedural-generation
- single-track
- ai-racers
- stylized

## Reconstructed prompt

Build Kart Royale, a Mario Kart-style 3D kart racer in Three.js that runs in the browser with zero downloaded art assets — all karts, track, textures, sounds and music generated procedurally in code. One sunset coastal circuit (~1.6km, 3 laps, 8 racers), raycast kart physics with drift into tiered mini-turbo boosts, position-weighted items (mushrooms, shells, bananas, star, bolt), rocket-start countdown, racing-line AI, chase camera, minimap/HUD/speedometer, touch + keyboard + gamepad, golden-hour stylized polish with post-processing.

## Source evidence

- Mario Kart-style browser racer with zero art assets: every mesh, texture, material and sound is generated in code at load time. ([source](https://github.com/ryancampbell/kart-royale/blob/main/README.md))
- Built by Claude Opus 5 from a single prompt then improved over nine orchestrated multi-agent Gauntlet Loop rounds with separate hostile critic agents judging rendered screenshots. ([source](https://github.com/ryancampbell/kart-royale/blob/main/README.md))
- Self-reported honest score is 62/100 against a shipped Mario Kart bar (60-75 = good indie, clearly not first-party); drift-to-boost loop scores 74/100 and drifting is 2.03s/lap faster but 83% of attempts never bank a mini-turbo tier. ([source](https://github.com/ryancampbell/kart-royale/blob/main/README.md))
- Single course Sunset Bay Circuit: ~1600m coastal Mediterranean track at golden hour with 8 sections (harbour, village climb, cliff traverse, tunnel, beach descent, 20-degree banked curve, bridge), elevation 0 to +42m. ([source](https://github.com/ryancampbell/kart-royale/blob/main/ART_DIRECTION.md))
- Tech: ~60,500 lines across 49 files, Three.js + postprocessing + n8ao + simplex-noise; raycast-suspension kart with slip-angle tyre model and mini-turbo drifting, spline circuit with banking/surface zoning, procedural materials, racing-line AI, Web Audio synthesis. ([source](https://github.com/ryancampbell/kart-royale/blob/main/README.md))
- Keyboard controls from Input.ts: steer ArrowLeft/ArrowRight or A/D, accel ArrowUp/W, brake ArrowDown/S, drift ShiftLeft/ShiftRight, use item Space/Enter/E/Ctrl, look-back Q/Alt, pause Esc/P; plus gamepad and on-screen touch controls with auto-accelerate. ([source](https://github.com/ryancampbell/kart-royale/blob/main/src/core/Input.ts))
- Items use classic position-weighted distribution (leader gets bananas/shells to defend, backmarkers get mushrooms/star/bolt to catch up), item boxes respawn in 2.5s rows spanning road width, rocket start for short throttle hold at GO and burnout if held too long. ([source](https://github.com/ryancampbell/kart-royale/blob/main/src/game/Items.ts))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 80/100: \[Fictional review\] Imagined weekend racer: the sunset bay looks way better than code has any right to, and nailing a drift past the Amalfi signs feels great — just wish there were a second track already.
- 60/100: \[Fictional review\] Made-up casual player note: fun for three laps, but I kept losing my mini-turbo and the backmarker bolt ended my lead on the bridge. Needs a tutorial for drift tiers.
- 100/100: \[Fictional review\] Invented dev-fan take: zero art files and it still pulls off backlit palms and chrome roll-bars in a browser tab? As a tech demo this is pure joy, even if it is not Mario Kart yet.

## Links

- [Source repository](https://github.com/ryancampbell/kart-royale)
- [Related link](https://racing.ryancampbell.com)
- [Related link](https://www.ryancampbell.com/kart-royale)
