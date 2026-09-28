# Neon Hunter

[View source](https://github.com/Prashant7380/Neon-Hunter)

| Overall rating | Screenshot score |
| :---: | :---: |
| **37/100** | **Not scored** |

<details>
<summary>Read the scoring rationale</summary>

### Overall rating

Far from AAA (single snake loop, 8 small zones, no multiplayer, narrative, online, or live-ops scale; 0 stars/forks; no verified hosted build, performance, or balance). Calibrated against the full catalog: closest comparators are T-Rex Runner (35 overall, single-reflex loop with shipped maturity and mass validation), 2048 (38, flawless single-mechanic classic), Ballz (40, deeper brick-breaker systems with CI builds but no browser play), Turbo Kart Rally (40, complete 3D racer), and Neon Arena (48, far deeper 3D roguelite with co-op/meta). Neon Hunter sits just above T-Rex on scope (8 zones, 5 wall patterns, hazards, 4 pickup types, combo economy, stars/persistence, synth audio, touch+dpad) but below Ballz/Turbo Kart on technical ambition and below 2048 on validation and loop polish, and far below Neon Arena despite the shared neon name. Evidence gaps: no playable URL, no screenshots, and no playthrough; source text alone does not prove playability, frame rate, or difficulty balance.

### Screenshot score

No inspectable gameplay screenshot.

</details>

## At a glance

| Detail | Value |
| --- | --- |
| Repository created | 26 Sep 2026 · 15:13 UTC |
| Added to catalog | 27 Sep 2026 · 06:09 UTC |
| Last updated | 27 Sep 2026 · 06:09 UTC |
| Documented creation models | [Claude Opus 5.5](https://github.com/Prashant7380/Neon-Hunter) |

## Play

- Open Neon Hunter/index.html in a browser (no hosted playable URL is verified)
- Press PLAY or Enter, then steer the neon snake with Arrow keys or WASD, or swipe / use the on-screen D-pad on touch devices
- Eat the glowing orbs to raise your count toward the zone target and grow longer; chained orbs build a combo multiplier up to x8
- Grab coins for currency, stars for +100 points, and phase diamonds for 5 seconds of ghost wall-passing
- Avoid walls (fatal on no-wrap zones), your own body, and red hazard blocks; dying ends the run, reaching the orb target clears the zone
- Clear a zone to earn 1-3 stars and coins, unlock the next of 8 zones, and persist progress, best scores, and pilot name in localStorage
- Pause with Space, P, or Esc; restart with R; mute with M

## Mechanics

- Grid snake movement with queued turns, constant step timer, and per-orb speed ramp
- 8 hand-tuned zones (NEON GRID, PILLARS, STEEL CAGE, THE MAZE, SPEED RUSH, HAZARD ZONE, GAUNTLET, VOID MASTER) with distinct wall patterns, wrap rules, speeds, and orb targets
- Orb chaining with combo counter and score multiplier up to x8 plus combo-timeout reset
- Coin pickups with persistent wallet, gold star pickups for +100 x multiplier, and phase pickups granting 5s ghost pass-through
- Timed hazard blocks that warn then solidify in later zones, plus blinking expiry timers on coin, star, and phase items
- Wall-pattern generator (pillars, cross, maze, corridors, rings) with guaranteed clear spawn lane
- Star rating, zone-best score, and sequential unlock progression persisted in localStorage
- HUD with zone name, orb progress bar, score with pop animation, multiplier readout, and coin pill
- Juice: particles, shockwave ripples, floating score text, screen shake, hitstop, chromatic flash, and banner announcements
- Fully synthesized WebAudio sound effects (eat pitch-ladder, coin, star arpeggio, phase sweep, warn, death, win) with mute toggle

## Tags

- arcade
- snake
- 2d
- neon
- browser-game
- single-player
- level-based
- combo
- html5
- canvas

## Controls

- Mobile controls: Supported
- Motion controls: Not established
- Gamepad: Not established
- Keyboard/mouse: Supported

## Player modes

- Human players: 1
- Modes: single-player

## Technologies

- **HTML5** — language ([evidence](https://raw.githubusercontent.com/Prashant7380/Neon-Hunter/main/Neon%20Hunter/index.html))
- **JavaScript** — language ([evidence](https://raw.githubusercontent.com/Prashant7380/Neon-Hunter/main/Neon%20Hunter/index.html))
- **Canvas 2D** — rendering ([evidence](https://raw.githubusercontent.com/Prashant7380/Neon-Hunter/main/Neon%20Hunter/index.html))
- **Web Audio API** — audio ([evidence](https://raw.githubusercontent.com/Prashant7380/Neon-Hunter/main/Neon%20Hunter/index.html))
- **Vite 7.3.2** — build ([evidence](https://raw.githubusercontent.com/Prashant7380/Neon-Hunter/main/Neon%20Hunter/package.json))

## Reconstructed prompt

Build NEON HUNTER, a single self-contained HTML5 arcade snake game in one index.html file (canvas 2D + WebAudio, no assets): steer a glowing neon snake on a responsive grid, eat orbs to hit per-zone targets across 8 zones with distinct wall patterns, wrap rules, speeds and colors, add combo multiplier up to x8, coin/star/phase-ghost pickups with expiry, timed red hazard blocks, 1-3 star ratings with sequential unlocks and localStorage persistence for coins/best/name, HUD with progress bar/score/multiplier, home/level-select/pause/win/game-over screens, swipe plus on-screen D-pad and Arrows/WASD/Space/R/M/Enter keyboard controls, particles/ripples/shake/flash juice, and fully synthesized sound effects.

## Source evidence

- Repository page identifies Prashant7380/Neon-Hunter as public with description 'So I made a game using Claude Opus 5.5, a simple arcade 2D platformer game, made using HTML5', 0 stars, 0 forks, 4 commits, and a top-level 'Neon Hunter' folder plus README.md. ([source](https://github.com/Prashant7380/Neon-Hunter))
- Root README.md contains only the title and the same one-line description attributing creation to Claude Opus 5.5 as an HTML5 arcade game. ([source](https://github.com/Prashant7380/Neon-Hunter/blob/main/README.md))
- Neon Hunter folder lists src/, index.html, package-lock.json, package.json, tsconfig.json, and vite.config.ts. ([source](https://github.com/Prashant7380/Neon-Hunter/tree/main/Neon%20Hunter))
- src/ lists App.tsx, index.css, main.tsx, and utils/, establishing a React+Vite scaffold around the game. ([source](https://github.com/Prashant7380/Neon-Hunter/tree/main/Neon%20Hunter/src))
- App.tsx states the game is now a pure HTML5 build with all markup, CSS, canvas rendering and WebAudio sound in index.html as a single self-contained file with no React, and the stub exists only so scaffolding type-checks. ([source](https://raw.githubusercontent.com/Prashant7380/Neon-Hunter/main/Neon%20Hunter/src/App.tsx))
- index.html title is 'NEON HUNTER — HTML5 Arcade' with mobile viewport, HUD, home/level-select/pause/win/game-over screens, on-screen D-pad, and tagline 'Eight neon zones. Chain orbs, grab coins, dodge the walls.' ([source](https://raw.githubusercontent.com/Prashant7380/Neon-Hunter/main/Neon%20Hunter/index.html))
- index.html defines 8 LEVELS (NEON GRID, PILLARS, STEEL CAGE, THE MAZE, SPEED RUSH, HAZARD ZONE, GAUNTLET, VOID MASTER) with pattern, wrap, speed, ramp, orb target, coin count, gold/phase odds, hazard interval, and accent color. ([source](https://raw.githubusercontent.com/Prashant7380/Neon-Hunter/main/Neon%20Hunter/index.html))
- index.html implements canvas 2D rendering (getContext('2d')), grid snake with queued turns, orb/coin/star/phase items, wall patterns, hazards, particles, ripples, floaters, screen shake, and synthesized WebAudio SFX with AudioContext, plus localStorage save under neonHunterHTML5.v1. ([source](https://raw.githubusercontent.com/Prashant7380/Neon-Hunter/main/Neon%20Hunter/index.html))
- Keyboard controls are Arrows/WASD to steer, Space/P/Esc pause, R restart, M mute, Enter confirm; touch controls are swipe-to-steer anywhere plus bottom-right D-pad buttons; pause button and clickable menus give pointer/mouse operability; no gamepad, accelerometer, gyroscope, multiplayer, or second-player code was found. ([source](https://raw.githubusercontent.com/Prashant7380/Neon-Hunter/main/Neon%20Hunter/index.html))
- package.json names the scaffold react-vite-tailwind with react 19.2.6, vite 7.3.2, vite-plugin-singlefile 2.3.0, typescript 5.9.3, and tailwindcss; vite.config.ts wires react, tailwindcss, and singlefile plugins. ([source](https://raw.githubusercontent.com/Prashant7380/Neon-Hunter/main/Neon%20Hunter/package.json))
- No homepage, deploy target, itch/vercel/netlify link, image asset, screenshot, or og:image was found in the fetched game file; both probed GitHub Pages URLs return HTTP 404, so no publicly reachable playable URL is established. ([source](https://github.com/Prashant7380/Neon-Hunter))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 78/100: Fictional illustrative review: chaining orbs to x5 on PILLARS while a coin blinked out felt great — the neon trail and combo pop make a simple snake loop surprisingly tense.
- 55/100: Fictional illustrative review: eight zones with mazes and hazards kept me busy for a while, but with no hosted build or screenshots I had to run the file myself and runs blur together fast.
- 100/100: Fictional illustrative review: a single self-contained HTML file with synth sound, ghost phase pickups, and star-rated zones is absurd efficiency — my favorite tiny neon time-waster here.

## Links

- [Source repository](https://github.com/Prashant7380/Neon-Hunter)
- [Game file (single-file HTML5 build)](https://github.com/Prashant7380/Neon-Hunter/blob/main/Neon%20Hunter/index.html)
- [Scaffolding manifest](https://github.com/Prashant7380/Neon-Hunter/blob/main/Neon%20Hunter/package.json)
