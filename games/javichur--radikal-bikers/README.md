# Radikal Riders

[Play the game](https://javichur.github.io/radikal-bikers/leoGjAW41OH-fIkg/) · [View source](https://github.com/javichur/radikal-bikers)

| Overall rating | Screenshot score |
| :---: | :---: |
| **54/100** | **55/100** |

<details>
<summary>Read the scoring rationale</summary>

### Overall rating

Strong indie arcade scope: 5 difficulty-ordered stages plus a Valencia Fallas stage and night variant, 3 riders with stats, checkpoint/combo/challenge/grade/XP/ghost/rival systems, deterministic fixed-step sim with Vitest and Playwright (desktop + emulated iPhone) coverage. That breadth exceeds single-track catalog racers Kart Royale (50/100) and Turbo Kart Rally (40/100), but the single-AI-rival field is thinner than their 8-kart grids, cel-shaded low-poly art is simpler than Kart Royale's golden-hour coast, and there is no multiplayer or live-ops scale, so it sits below moorestech (64/100). Evidence gaps: judged from repo docs, config and one 480x360 still plus game shell only; no full live playthrough, performance or balance data, so playability and tuning are not proven.

### Screenshot score

The single inspected 480x360 gameplay still shows coherent cel-shaded city racing with readable bike, traffic, clubs/billboards and a full HUD (time, score, combo banner, 150 km/h speedometer, touch GAS/FRENO/CABALLITO and joystick), so it is the game's own output, not concept art. It sits below Kart Royale (70) and Turbo Kart Rally (70), whose 1080p frames show denser tracksides, lighting and detail, and below moorestech (76); flat building facades, simple road texture and low capture resolution limit detail. Still image only: no inference about motion, performance or feel.

</details>

## At a glance

| Detail | Value |
| --- | --- |
| Repository created | 26 Sep 2026 · 06:14 UTC |
| Added to catalog | 27 Sep 2026 · 06:25 UTC |
| Last updated | 27 Sep 2026 · 06:25 UTC |
| Documented creation models | [Claude Opus 5.5](https://github.com/javichur/radikal-bikers/blob/main/README.md) |

## Screenshots

![Inspected downloaded copy of the YouTube demo thumbnail (480x360): third-person chase view behind a pizza-delivery bike on a multi-lane cel-shaded city avenue, yellow taxi directly ahead, blue car at left, brick buildings both sides; HUD shows TIEMPO 60, PUNTOS 71858, combo banner BUUUM! +1000 and A UN PELO +250, progress bar, 150 km/h speedometer, and on-screen touch controls (left floating joystick, GAS / FRENO / CABALLITO buttons) plus pause button. Clearly the game's own runtime output.](https://img.youtube.com/vi/Ds_wtQz6IG0/hqdefault.jpg)

Inspected downloaded copy of the YouTube demo thumbnail (480x360): third-person chase view behind a pizza-delivery bike on a multi-lane cel-shaded city avenue, yellow taxi directly ahead, blue car at left, brick buildings both sides; HUD shows TIEMPO 60, PUNTOS 71858, combo banner BUUUM! +1000 and A UN PELO +250, progress bar, 150 km/h speedometer, and on-screen touch controls (left floating joystick, GAS / FRENO / CABALLITO buttons) plus pause button. Clearly the game's own runtime output.

## Play

- Open https://javichur.github.io/radikal-bikers/leoGjAW41OH-fIkg/ in a desktop or mobile landscape browser and wait for the title screen.
- Pick a rider (Rocco or Luna; Nitro unlocks with stars) and a stage ordered by difficulty, then start the 3-2-1-GO countdown.
- Accelerate with Up/W (RT/A on gamepad, GAS button on touch) and steer with Left/Right or A/D (left stick, or floating left-half joystick on touch).
- Deliver the pizza before time runs out; each CHECKPOINT adds extra time. Brake/reverse with Down/S (LT/X, FRENO button).
- Dodge two-way traffic (cars, taxis, vans, buses, trucks, police, ambulances, fire, garbage and tanker trucks), use ramps to jump over vehicles, and hold wheelie with Space/Shift (RB/Y, CABALLITO button) for extra top speed at the cost of handling.
- Chain tricks (near-misses, long wheelies, jumps, smashed glass, shortcuts, explosions) to raise the combo multiplier up to x5; crashing loses the pending combo.
- If time expires, use the 9-second CONTINUE from the last checkpoint (minus 5000 points); reach the finish for the PIZZA ENTREGADA results, S/A/B/C grade, stars, XP and unlocks.
- Pause with Esc/P (Start, II button); restart instantly with R (Select/Back, pause menu on touch).

## Mechanics

- Checkpoint time-attack pizza delivery with extra time per checkpoint and 9-second continue from last checkpoint with score penalty
- Wheelie system: +12% top speed with reduced handling, limited duration with cooldown, lets the bike jump over crossing vehicles
- Ramp jumps with airtime-scaled trick points and slow-motion camera on near-miss and jump tricks
- Combo engine: 7 trick types bank into a pending combo paid out with up to x5 multiplier; crashes forfeit it
- 3 star challenges per stage plus S/A/B/C score grades; stars unlock the Nitro rider and a night stage
- AI rival rider that dodges traffic with rubber-banding plus a translucent ghost of the best local delivery per stage+rider
- XP levels (max 10) unlocking bike paint jobs, persistent records/stars/shortcuts/ghosts in localStorage
- Procedural city stages with traffic mix, level crossings, roadworks cones, shortcuts, tunnels, bridges, parks and Valencia monuments

## Tags

- arcade
- racing
- moto
- 3d
- threejs
- webgl
- browser-game
- time-attack
- stylized
- single-player
- pizza-delivery
- spanish
- touch-controls

## Controls

- Mobile controls: Supported
- Motion controls: Not established
- Gamepad: Supported
- Keyboard/mouse: Supported

## Player modes

- Human players: 1
- Modes: single-player

## Technologies

- **Three.js ^0.186.1** — rendering ([evidence](https://github.com/javichur/radikal-bikers/blob/main/package.json))
- **TypeScript ~6.0.2** — language ([evidence](https://github.com/javichur/radikal-bikers/blob/main/package.json))
- **Vite ^8.3.0** — build ([evidence](https://github.com/javichur/radikal-bikers/blob/main/package.json))
- **Web Audio API** — audio ([evidence](https://github.com/javichur/radikal-bikers/blob/main/README.md))
- **Vitest ^5.0.2** — framework ([evidence](https://github.com/javichur/radikal-bikers/blob/main/package.json))

## Reconstructed prompt

Build Radikal Riders, a browser arcade tribute to Radikal Bikers: 3D cel-shaded pizza-delivery bike racing in Three.js with code-generated models and Web Audio synth sound. 5 difficulty-ordered stages plus a Valencia Fallas stage with real monuments and a night variant, 3 riders with speed/accel/handling stats, checkpoint time-attack with 9s continue, wheelies, ramps, shortcuts, 7 trick types with x5 combo multiplier, 3 star challenges and S/A/B/C grades per stage, AI rival plus best-delivery ghost, XP levels unlocking bike paints, localStorage saves, Spanish/English UI, keyboard + Gamepad API + floating-joystick touch controls, deterministic fixed-step sim with Vitest and Playwright coverage, Vite build deployable to GitHub Pages.

## Source evidence

- Repository javichur/radikal-bikers is a public non-fork, primary language TypeScript, default branch main, has\_pages true; no description/homepage/topics. ([source](https://api.github.com/repos/javichur/radikal-bikers))
- Game is Radikal Riders: arcade browser pizza-delivery bike racing inspired by Gaelco's 1998 Radikal Bikers; all art, audio and code original; cel-shaded code-generated 3D graphics and real-time Web Audio synth sound. ([source](https://github.com/javichur/radikal-bikers/blob/main/README.md))
- Arcade mode for 1 human player with 5 difficulty-ordered stages (Paseo Maritimo, Puerto Radikal, Centro Historico, Zona Industrial, Carretera de la Colina) plus a Valencia Fallas stage, 2 starting riders (Rocco, Luna) plus unlockable Nitro, in Spanish and English. ([source](https://github.com/javichur/radikal-bikers/blob/main/README.md))
- Playable browser build opens at the secret GitHub Pages path; page shell returns HTTP 200 with Radikal Riders title, game-canvas element, overlay/screens containers and rotate-device hint. ([source](https://javichur.github.io/radikal-bikers/leoGjAW41OH-fIkg/))
- Keyboard controls documented: steer Left/Right or A/D, accelerate Up/W, brake/reverse Down/S, wheelie Space/Shift, pause Esc/P, restart R, menus arrows+Enter. ([source](https://github.com/javichur/radikal-bikers/blob/main/README.md))
- Gamepad controls documented (Gamepad API): steer left stick/d-pad, accelerate RT/A, brake LT/X, wheelie RB/Y, pause Start, restart Select/Back, menus d-pad+A/B; src/input/gamepad.ts implements the Gamepad API source. ([source](https://github.com/javichur/radikal-bikers/blob/main/README.md))
- Touch controls documented and implemented (not just responsive layout): floating joystick on left half, GAS / FRENO / CABALLITO buttons, II pause button, tap menus, landscape play with portrait warning, iPhone safe-area and zoom/scroll locking; src/input/touch.ts implements TouchInput with floating analogue stick and gas/brake/wheelie buttons. ([source](https://github.com/javichur/radikal-bikers/blob/main/README.md))
- No accelerometer or gyroscope device-motion controls are documented; motion support is unestablished. ([source](https://github.com/javichur/radikal-bikers/blob/main/README.md))
- Single-player only: explicitly 1-player arcade mode; the rival is a machine-controlled rider and the ghost is the player's own best delivery, so human-player count is fixed at 1. ([source](https://github.com/javichur/radikal-bikers/blob/main/README.md))
- Systems: checkpoints add time, 9-second continue with -5000 points, near-miss/wheelie/jump/glass/shortcut/explosion/turbo tricks feed a combo multiplier up to x5 lost on falls, 3 star challenges and S/A/B/C grades per stage, rival + ghost, XP levels unlocking bike paints, instant restart. ([source](https://github.com/javichur/radikal-bikers/blob/main/docs/game-design.md))
- Built 26 Sept 2026 with the GitHub Copilot for iPhone app and the Claude Opus 5.5 model. ([source](https://github.com/javichur/radikal-bikers/blob/main/README.md))
- Tech: three ^0.186.1 dependency with toon-material Three.js renderer, TypeScript strict, Vite build with base './', Vitest unit tests with coverage thresholds, Playwright e2e on desktop plus emulated iPhone, ESLint + Prettier; simulation in sim/ and core/ is DOM/Three.js-free and deterministic at 1/60s fixed step with seeded PRNG. ([source](https://github.com/javichur/radikal-bikers/blob/main/package.json))
- Demo video thumbnail provides the only inspected gameplay still; repo file tree contains no gameplay PNG/JPG screenshots, only PWA icons under public/icons/. ([source](https://youtu.be/Ds_wtQz6IG0))
- No existing catalog entry matches javichur/radikal-bikers or Radikal Riders; the catalog's closest racing comparators are Kart Royale (50/100, screenshots 70), Turbo Kart Rally (40/100, screenshots 70) and moorestech (64/100, screenshots 76). ([source](https://github.com/agents-dev/Astra-Top-Games/blob/main/README.md))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 82/100: Fictional illustrative review: imagined arcade fan — threading the taxi gap at 150 km/h, popping a wheelie past the checkpoint and banking a x5 combo while the rival breathes down my neck feels exactly like the 1998 original, and the Valencia Fallas stage with the Micalet on the skyline is a lovely surprise.
- 64/100: Fictional illustrative review: made-up casual player note — great checkpoint tension and the ghost of my best delivery keeps me retrying, but the low-poly traffic gets samey after a few stages and I crashed more to pop-in buses than to my own mistakes. More rival variety would help.
- 100/100: Fictional illustrative review: invented tech-enthusiast take — a deterministic fixed-step sim decoupled from Three.js, procedural cel-shaded city, synthesized Web Audio, full Vitest plus Playwright on desktop and emulated iPhone, all built in a day from an iPhone? As a browser engineering feat this is pure joy.

## Links

- [Source repository](https://github.com/javichur/radikal-bikers)
- [Play game](https://javichur.github.io/radikal-bikers/leoGjAW41OH-fIkg/)
- [Demo video](https://youtu.be/Ds_wtQz6IG0)
