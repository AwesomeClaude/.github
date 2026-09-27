# Crabhouse v2

[Play the game](https://kamibukuro18.github.io/opuscrabhouse/) · [View source](https://github.com/kamibukuro18/opuscrabhouse)

| Overall rating | Screenshot score |
| :---: | :---: |
| **43/100** | **Not scored** |

<details>
<summary>Read the scoring rationale</summary>

### Overall rating

Far from AAA: single 192x144 canvas room, no 3D, voice, cinematics or multiplayer; one small static-file browser build. Most relevant comparators: neverquest (45, deeper RPG systems but text-UI only), Pizza Chef (44, similarly broad arcade plus economy scope with unverified visuals), Zoo Keeper (42, broader paper simulation scope but no playable build or screenshots) and 2048 (38, tight minimal loop). Crabhouse v2 sits just below neverquest on mechanical depth but above Zoo Keeper and 2048 because it has a verified live playable build, a complete idle loop with expeditions, dailies, achievements and prestige, plus fully procedural pixel art and 6-track chiptune. Evidence gaps: no inspectable gameplay screenshot; no live playthrough, so playability, pacing, balance and performance are unverified from docs and code excerpts alone.

### Screenshot score

No inspectable gameplay screenshot.

</details>

## At a glance

| Detail | Value |
| --- | --- |
| Repository created | 26 Sep 2026 · 07:07 UTC |
| Added to catalog | 27 Sep 2026 · 06:08 UTC |
| Last updated | 27 Sep 2026 · 06:08 UTC |
| Documented creation models | Not established |

## Play

- Open https://kamibukuro18.github.io/opuscrabhouse/ in a browser and press Go To House (sound on for chiptune music).
- Tap anywhere in the room to earn KP with scissor power; chain taps for combo bonus up to 1.5x and fill the fever gauge.
- When the gauge fills, fever starts: taps pay 3x for 10 seconds with music change, confetti and dancing crabs; tap 60 times for super fever at 5x.
- Spend KP at the door to invite new crabs, in training on 9 uncapped upgrades, and on food to level crabs for per-minute income.
- Send crabs on expeditions (5 min to 8 h, offline progress), collect hats that boost income, catch the golden lucky crab, and finish 3 daily wishes.
- Rearrange furniture, expand the house through 5 stages, toggle the wall light switch, change chiptune tracks, and prestige via molting for permanent +10% per pearl.

## Mechanics

- Tap-anywhere clicker with combo multiplier and 10-second fever meter with super-fever extension
- 9 uncapped training upgrades including auto-tapper, savings, combo mastery and expedition maps
- Crab raising: 13 illustrated species, per-crab levels, growth stages, per-minute KP income and rarity multipliers
- 4 real-time expeditions with offline progress, KP souvenirs and 9 income-boosting hats
- Golden lucky crab random event with KP, buff, instant-fever, hat or pearl rewards
- 3 daily wishes with streak bonus, 29 achievements, prestige molting for permanent multipliers, furniture, 5 house expansions and localStorage saves

## Tags

- clicker
- idle
- pet-raising
- simulation
- management
- pixel-art
- cozy
- single-player
- browser

## Controls

- Mobile controls: Supported
- Motion controls: Not established
- Gamepad: Not established
- Keyboard/mouse: Supported

## Player modes

- Human players: 1
- Modes: single-player

## Technologies

- **JavaScript** — language ([evidence](https://raw.githubusercontent.com/kamibukuro18/opuscrabhouse/main/game.js))
- **HTML5** — language ([evidence](https://raw.githubusercontent.com/kamibukuro18/opuscrabhouse/main/index.html))
- **CSS** — language ([evidence](https://raw.githubusercontent.com/kamibukuro18/opuscrabhouse/main/style.css))
- **Canvas 2D** — rendering ([evidence](https://raw.githubusercontent.com/kamibukuro18/opuscrabhouse/main/game.js))
- **Web Audio API** — audio ([evidence](https://raw.githubusercontent.com/kamibukuro18/opuscrabhouse/main/game.js))

## Reconstructed prompt

Create a cozy Japanese browser idle game called Crabhouse v2: a pixel-art crab-raising clicker in one room. Tap anywhere for KP with combos and a fever mode, 9 uncapped upgrades, 13 crab species with levels and hats, real-time expeditions with offline progress, daily wishes, achievements, prestige, furniture and house expansions, procedural canvas pixel art and Web Audio chiptune with no external assets, and localStorage saves.

## Source evidence

- Repository page exists as kamibukuro18/opuscrabhouse titled Crabhouse v2 with 1 commit, 0 stars/forks, and files .gitignore, .nojekyll, README.md, game.js, index.html, style.css; no image assets listed. ([source](https://github.com/kamibukuro18/opuscrabhouse))
- README describes a browser crab-raising clicker: tap room for KP, combos to 1.5x, 10s fever at 3x with dedicated BGM, 9 uncapped upgrades, crab levels with per-minute KP, 4 expeditions (5 min/30 min/2 h/8 h) with offline progress, 9 hats, golden lucky crab, 3 daily wishes, prestige pearls, 13-species encyclopedia, 11 furniture items, 5 house stages, 5 chiptune tracks, 29 achievements and localStorage saves. All pixel art and music are code-generated with no image or audio files. ([source](https://github.com/kamibukuro18/opuscrabhouse))
- README gives the playable browser URL and local-run instructions (python3 -m http.server). ([source](https://github.com/kamibukuro18/opuscrabhouse))
- Playable page opens the actual game, not just a repo: title Crabhouse with Go To House start button, KP header, 192x144 room canvas, fever gauge, dialog box and menu buttons for door, crabs, training, expedition, wishes, redecorating, encyclopedia and music. ([source](https://kamibukuro18.github.io/opuscrabhouse/))
- index.html shows a mobile-ready shell: viewport-fit meta, 192x144 room canvas plus title canvas, menu buttons, and script tag loading game.js. ([source](https://raw.githubusercontent.com/kamibukuro18/opuscrabhouse/main/index.html))
- game.js header states all pixel art and chiptune are procedural with no external assets; code excerpts show canvas 2D rendering (getContext('2d')), Web Audio chiptune (AudioContext, oscillators, track/lead/bass scheduler) and localStorage save key crabhouse-v2. No engine, multiplayer, gamepad or motion-control code was found in the inspected excerpts. ([source](https://raw.githubusercontent.com/kamibukuro18/opuscrabhouse/main/game.js))
- Keyboard/mouse support: canvas uses pointerdown plus click handlers for dialog, modal, menu and start button, so mouse clicks drive taps and UI. ([source](https://raw.githubusercontent.com/kamibukuro18/opuscrabhouse/main/game.js))
- Touch support: core verb is tap (README: tap anywhere for KP, tap speech bubbles and lucky crab), canvas input uses Pointer Events which unify mouse/touch, and the page sets a mobile viewport with touch-action manipulation CSS. ([source](https://raw.githubusercontent.com/kamibukuro18/opuscrabhouse/main/index.html))
- Single-player with one human: single-room idle game with one localStorage save and no multiplayer, lobby, versus or network-play systems in the README or inspected code. ([source](https://github.com/kamibukuro18/opuscrabhouse))
- gh api could not be used: gh CLI has no login in this runner and unauthenticated api.github.com calls were rate-limited, so evidence was gathered by inspecting the repository page, raw files and live playable page instead. ([source](https://github.com/kamibukuro18/opuscrabhouse))
- No gameplay screenshot could be inspected: the repo contains no image files and no screenshot was reachable, so graphics scoring is null and no motion or feel is inferred. ([source](https://github.com/kamibukuro18/opuscrabhouse))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 85/100: My crabs do tiny wave dances during fever and the tap-melody climbs with every click. I came for the clicker and stayed to collect all thirteen species.
- 62/100: Cozy and generous with hats, expeditions and daily wishes, but most of the day it plays itself. Best in short happy bursts.
- 100/100: The golden lucky crab sprinted past and my whole living room glowed gold. A perfect little crab diorama that sings back.

## Links

- [Source repository](https://github.com/kamibukuro18/opuscrabhouse)
- [Play the game](https://kamibukuro18.github.io/opuscrabhouse/)
