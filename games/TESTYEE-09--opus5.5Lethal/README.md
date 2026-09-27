# Lethal Company: Opus Edition

[Play the game](https://testyee-09.github.io/opus5.5Lethal/) · [View source](https://github.com/TESTYEE-09/opus5.5Lethal)

| Overall rating | Screenshot score |
| :---: | :---: |
| **54/100** | **Not scored** |

<details>
<summary>Read the scoring rationale</summary>

### Overall rating

Far from AAA: single-commit fan tribute with streamed third-party three.js example assets, no original art pipeline, no campaign cinematics, and unverified performance, balance, and netcode at scale. Excluding the target itself, most relevant comparators are Dead Signal: Exclusion Zone (47, same Claude Opus 5.5 horror-FPS lineage but single-player only with no verified playable build and no screenshots), Wilderness (44, broad procedural survival scope but dead demo and no screenshots), Kart Royale (50, complete verified 3D loop with polished 70-point screenshots but single-track kart scope), Ashlands (55, current non-self runner-up), and moorestech (64, catalog top with years of commits and 76-point screenshots). This target outranks Dead Signal and Wilderness on verified scope: a live 200 OK playable build plus documented online multiplayer with proximity voice, 8 destinations, quota economy, and 6 monster types exceeds their unverified or single-player loops. It edges past Kart Royale on systems depth and multiplayer despite having no inspectable screenshots, but sits below Ashlands and moorestech on proven polish, iteration history, and visual evidence. Source code and a loading menu do not prove playability, frame rate, or balance.

### Screenshot score

No inspectable gameplay screenshot.

</details>

## At a glance

| Detail | Value |
| --- | --- |
| Repository created | 26 Sep 2026 · 14:14 UTC |
| Added to catalog | 27 Sep 2026 · 06:04 UTC |
| Last updated | 27 Sep 2026 · 06:04 UTC |
| Documented creation models | [Claude Opus 5.5](https://github.com/TESTYEE-09/opus5.5Lethal/commit/298c0b204bd4ce0010a575c2322baf744fbba445) |

## Play

- Open the verified playable build in a desktop browser with WebGL and audio enabled.
- Enter an employee name and pick a suit color, then HOST CREW, GO SOLO, or enter a 5-letter crew code and JOIN CREW; copy the invite link from pause to bring friends.
- Land on a moon, enter the facility, scavenge scrap and haul it back to the ship before midnight.
- Use the ship terminal to buy tools, route to moons, and check quota; sell scrap at the Company building at 71-Gordion to meet the profit quota before the deadline.
- Avoid or outplay Thumpers, Brackens, Coil-Heads, Hoarding bugs, Masked and Eyeless dogs plus turrets and landmines; dead players can only spectate.

## Mechanics

- First-person co-op horror scrap run loop with ship, procedural facility, and midnight extraction deadline
- Online multiplayer crew hosting and joining over WebRTC via PeerJS with 5-letter codes and invite links
- Solo mode plus host-authoritative crew play with snapshots, events, spectating, and performance reports
- Proximity voice chat plus walkie-talkie long-range radio with mute support
- Procedural facilities across 7 moons plus the Company building, with weather, day/night cycle, and profit quotas
- Six enemy types with distinct AI behaviors plus turrets and landmines
- Store and credit economy, terminal commands, ship radar, teleporter, scanner, apparatus, and boombox
- Inventory with weight, 4 slots, two-handed items, flashlight, emotes, text chat, and pause settings

## Tags

- horror
- co-op
- survival
- extraction
- sci-fi
- fps
- 3d
- procedural
- multiplayer
- fan-tribute

## Controls

- Mobile controls: Not established
- Motion controls: Not established
- Gamepad: Not established
- Keyboard/mouse: Supported

## Player modes

- Human players: Not established
- Modes: single-player, online multiplayer

## Technologies

- **Three.js r160** — engine ([evidence](https://raw.githubusercontent.com/TESTYEE-09/opus5.5Lethal/claude/busy-cray-rbpj04/js/assets.js))
- **WebGL** — rendering ([evidence](https://raw.githubusercontent.com/TESTYEE-09/opus5.5Lethal/claude/busy-cray-rbpj04/js/main.js))
- **JavaScript** — language ([evidence](https://api.github.com/repos/TESTYEE-09/opus5.5Lethal/languages))
- **PeerJS** — framework ([evidence](https://raw.githubusercontent.com/TESTYEE-09/opus5.5Lethal/claude/busy-cray-rbpj04/js/net.js))
- **WebRTC** — framework ([evidence](https://raw.githubusercontent.com/TESTYEE-09/opus5.5Lethal/claude/busy-cray-rbpj04/js/net.js))
- **Web Audio API** — audio ([evidence](https://raw.githubusercontent.com/TESTYEE-09/opus5.5Lethal/claude/busy-cray-rbpj04/js/audio.js))
- **GitHub Pages** — build ([evidence](https://raw.githubusercontent.com/TESTYEE-09/opus5.5Lethal/claude/busy-cray-rbpj04/.github/workflows/pages.yml))

## Reconstructed prompt

Build a browser fan tribute to Lethal Company with three.js: first-person co-op horror scrap collecting with solo plus PeerJS WebRTC online crews via 5-letter codes, proximity voice chat and walkie-talkies, 7 procedural moons plus the Company, weather and day/night quota loop, 6 monsters plus turrets and mines, store, terminal, ship radar, teleporter, scanner, apparatus and boombox, WASD pointer-lock controls, and a GitHub Pages deployment streaming models/textures/music from the three.js example CDN.

## Source evidence

- Repository is an actual game: README titles it 'Lethal Company: Opus Edition' and describes 'A co-op horror scrap-collecting game inspired by Lethal Company, built with three.js.' ([source](https://github.com/TESTYEE-09/opus5.5Lethal/blob/claude/busy-cray-rbpj04/README.md))
- Repo page confirms the same identity, file tree with index.html, js/, lib/, style.css, one commit on branch claude/busy-cray-rbpj04, 0 stars and 0 forks, JavaScript primary language. ([source](https://github.com/TESTYEE-09/opus5.5Lethal))
- API metadata: full name TESTYEE-09/opus5.5Lethal, default branch claude/busy-cray-rbpj04, created 2026-09-26, language JavaScript, has\_pages true, size 380; languages endpoint is JavaScript-dominated with CSS and HTML. ([source](https://api.github.com/repos/TESTYEE-09/opus5.5Lethal))
- Recursive tree has 26 paths and zero image files (only .github/workflows/pages.yml, index.html, style.css, 9 js files, vendored three/peerjs, .nojekyll, README), so no gameplay screenshot can be inspected from the repository. ([source](https://api.github.com/repos/TESTYEE-09/opus5.5Lethal/git/trees/claude/busy-cray-rbpj04?recursive=1))
- Verified playable URL returns HTTP 200 as text/html and the live page renders the full game menu with HOST CREW, GO SOLO, JOIN CREW, THE JOB briefing, CONTROLS list, HUD, terminal, death, report, and pause screens — proving it opens the playable game, not just a repo or promo page. ([source](https://testyee-09.github.io/opus5.5Lethal/))
- README documents the playable link, online multiplayer over WebRTC via PeerJS with host-a-crew 5-letter codes and invite links, plus GO SOLO — establishing both single-player and online multiplayer modes; crew size maximum is not documented so human-player count is unestablished. ([source](https://github.com/TESTYEE-09/opus5.5Lethal/blob/claude/busy-cray-rbpj04/README.md))
- Live menu DOM independently confirms HOST CREW, GO SOLO, JOIN CREW, and pause COPY INVITE LINK, corroborating solo plus online crew play; net.js implements host/join/broadcast over PeerJS with STUN/TURN. ([source](https://raw.githubusercontent.com/TESTYEE-09/opus5.5Lethal/claude/busy-cray-rbpj04/js/net.js))
- README plus live menu document keyboard and mouse controls: WASD move, Shift sprint, Ctrl/C crouch, Space jump, E interact, G drop, LMB use, RMB scan, 1-4/wheel slots, F flashlight, T chat, V mute, Z/X emotes, Esc menu — establishing keyboard\_mouse as supported; main.js adds keydown/keyup, mousedown/mousemove, and pointer-lock handlers. ([source](https://raw.githubusercontent.com/TESTYEE-09/opus5.5Lethal/claude/busy-cray-rbpj04/js/main.js))
- No touch, on-screen joystick, accelerometer, gyroscope, or gamepad bindings were found in the inspected index, main.js event handlers, or style.css, and no source explicitly rules them in or out — so mobile\_controls, motion\_controls, and gamepad remain unknown rather than not\_supported; viewport/responsive CSS alone is not treated as touch support. ([source](https://raw.githubusercontent.com/TESTYEE-09/opus5.5Lethal/claude/busy-cray-rbpj04/index.html))
- Commit message is the explicit creation-model attribution: 'Lethal Company clone in three.js with P2P multiplayer, voice chat and Pages deploy' with 'Co-Authored-By: Claude Opus 5.5'; branch name claude/busy-cray-rbpj04 and repo name opus5.5Lethal corroborate but the commit is the cited evidence. ([source](https://github.com/TESTYEE-09/opus5.5Lethal/commit/298c0b204bd4ce0010a575c2322baf744fbba445))
- No catalog match: the local catalog's Games section plus inspected Dead Signal (different zombies FPS repo), Wilderness (different voxel survival repo), Neural Sight (different FPS prototype), and moorestech (different factory game) share no verified repository, playable URL, or explicit project reference with this target; matching by title or Claude lineage alone was not used, so catalog\_slug is null. ([source](https://github.com/TESTYEE-09/opus5.5Lethal))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 82/100: Ran a full solo quota cycle on Experimentation and barely made the ship before midnight with a Thumper on my tail. The terminal, radar, quota pressure and facility crawling actually feel like the real thing in a browser tab.
- 58/100: Ambitious co-op tribute with real systems — moons, weather, voice chat, store and quota — but with borrowed three.js example assets, one commit of history, and no screenshots to judge the look, it is promising rather than proven.
- 100/100: Hosted a crew with a five-letter code and we were screaming over proximity voice while Coil-Heads froze mid-hallway. A playable multiplayer Lethal-like with zero install is absurd and wonderful.

## Links

- [Source repository](https://github.com/TESTYEE-09/opus5.5Lethal)
- [Repository README](https://github.com/TESTYEE-09/opus5.5Lethal/blob/claude/busy-cray-rbpj04/README.md)
- [Playable game](https://testyee-09.github.io/opus5.5Lethal/)
