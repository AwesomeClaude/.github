# T-Rex Runner

[Open the game source](https://github.com/wayou/t-rex-runner)
[Play the game](https://wayou.github.io/t-rex-runner/)
**Repository created:** 2014-11-29T10:04:04Z
**Added to catalog:** 2026-09-27T03:35:32.755095+00:00
**Updated in catalog:** 2026-09-27T03:35:32.755095+00:00

**Overall rating:** 35/100. Far from AAA: one endless track, one reflex mechanic, no levels, rivals, multiplayer, progression, or live-ops scale. Calibrated against all 20 catalog games. Closest comparators: 2048 (38 overall, single-mechanic viral classic with mass validation and a flawless loop), Flip Runner Racing (33, ten-level hill-climb with fuel/flips/chute but a 2-commit one-shot with no live URL), and Taipo (35, complete niche loop with multi-year releases). T-Rex Runner sits with that tier: it beats Beachy Beachy Ball (25, single roll-to-star mechanic with minimal art and no cultural validation) and TypeScript-Blackjack (28, faithful single-table rules but flat DOM) on execution polish, shipped maturity, and validation (Chrome offline easter egg played by billions; repo holds 2186 stars and 1286 forks), but trails Turbo Kart Rally (40, complete 3D racer with AI field, items, HUD, menus) and neverquest (45, deepest catalog systems scope) badly on gameplay depth, scope, and technical ambition. Evidence gaps: judged from repository metadata, README, index.html, and API-read index.js evidence plus one inspected animation frame without cloning and without playing a verified session, so playability, frame rate, difficulty balance, and audio quality are unverified; source and stills do not prove them.

**Screenshot score:** 30/100. Scored only from the inspected first frame of the repo's own gameplay GIF without inferring motion. The frame shows the game's authentic monochrome pixel output: small standing T-Rex sprite on a ground line against a blank white void. Against catalog baselines (Kart Royale 70, Turbo Kart Rally 70 with detailed tracks, HUDs, and crowds; 2048 at 45 with a polished flat UI; Beachy Beachy Ball 35 with a 3D ball, shadows, and obstacles) this has coherent iconic pixel styling but almost no scene detail, composition, or environment in the inspected frame. It sits near neverquest (30, text UI only) and above curiositY (18, near-zero presentation), clearly below 2048 and Beachy on visible polish. Later animation frames (obstacles, night cycle, score) were not extracted, so the score reflects only what was actually inspected.

## Screenshots

![Inspected first frame of the repo's own animated gameplay GIF: tiny dark pixel T-Rex standing at far left on a short horizontal ground line, vast empty white background, no obstacles, score, or night elements visible in this frame. Clearly the game's own runtime output, matching the Chrome offline runner art style.](https://raw.githubusercontent.com/wayou/t-rex-runner/gh-pages/assets/screenshot.gif)

Inspected first frame of the repo's own animated gameplay GIF: tiny dark pixel T-Rex standing at far left on a short horizontal ground line, vast empty white background, no obstacles, score, or night elements visible in this frame. Clearly the game's own runtime output, matching the Chrome offline runner art style.

## Play

- Open https://wayou.github.io/t-rex-runner/ and press Space (or tap / click) to start the run.
- Press Space, Up arrow, tap, or click to jump over cacti and pterodactyls; hold jump input for a higher arc.
- Press Down arrow to duck under high pterodactyls and to drop faster from a jump.
- Survive as speed ramps up through day and night; the run ends on the first collision.
- After crashing, press Space, tap, or click the canvas to restart and chase the saved HI score.

## Mechanics

- Auto-running endless side-scroller with steadily increasing speed
- Jump with variable arc plus mid-air fast drop via duck
- Ducking to pass under airborne pterodactyl obstacles
- Procedurally spawned ground cacti clusters and flying pterodactyls
- Day/night palette cycle with clouds, moon, and stars at higher scores
- Collision-triggered game over with restart and persisted HI score
- Jump, score-milestone, and hit sound effects

## Tags

- endless-runner
- arcade
- pixel-art
- browser-game
- single-player
- reflex
- chrome-easter-egg

## Controls

- Mobile controls: Supported
- Motion controls: Not established
- Gamepad: Not established
- Keyboard/mouse: Supported

## Player modes

- Human players: 1
- Modes: single-player

## Reconstructed prompt

Extract the Chrome offline error-page T-Rex runner into a standalone dependency-free browser game: a pixel dino auto-runs across a white desert, jump with Space/Up/tap/click and duck with Down, dodge procedurally spawned cacti and pterodactyls as speed ramps through a day/night cycle, crash to game over with a persisted HI score, full-screen touch controller plus keyboard and mouse support, and jump/score/hit sound effects.

## Source evidence

- GitHub API identifies wayou/t-rex-runner as public, JavaScript, 2186 stars, 1286 forks, topics chrome/easter-egg/google/javascript/t-rex-runner, default branch gh-pages, description 'the t-rex runner game extracted from chromium', homepage https://chromedino.com. ([source](https://api.github.com/repos/wayou/t-rex-runner))
- Repo page states the game is 'the trex runner game extracted from chrome offline err page' with a Chromium source link, a 'go and enjoy' play link, and the gameplay screenshot GIF; it also lists fork variants (Kumamon, KuGou, bot) with their own GIFs and play links. ([source](https://github.com/wayou/t-rex-runner))
- Raw README confirms the same description, the Chromium extraction claim, and the play link http://wayou.github.io/t-rex-runner/. ([source](https://raw.githubusercontent.com/wayou/t-rex-runner/gh-pages/README.md))
- API file listing (gh-pages branch) shows a tiny static game: index.html, index.js (~90KB), index.css, LICENSE, README.md, and an assets/ folder with sprite PNGs and gameplay GIFs. ([source](https://api.github.com/repos/wayou/t-rex-runner/contents/?ref=gh-pages))
- Playable index.html is titled 'chrome easter egg: t-rex runner', shows a 'Press Space to start' heading, includes a mobile viewport (user-scalable=no), sprite images, embedded jump/score/hit audio, and an onkeydown handler that hides the start message on Space (keyCode 32). ([source](https://github.com/wayou/t-rex-runner/blob/gh-pages/index.html))
- The live GitHub Pages build opens the playable game page ('Press Space to start' with offline sprites) and returned HTTP 200, verifying it is a playable URL and not just a repo or promo page. ([source](https://wayou.github.io/t-rex-runner/))
- index.js binds keyboard (KEYDOWN/KEYUP with JUMP and RESTART keycodes), mouse (MOUSEDOWN/MOUSEUP with left-click-on-canvas restart), and touch (full-screen touch-controller div, TOUCHSTART/TOUCHEND, IS\_TOUCH\_ENABLED/IS\_MOBILE handling); jump is triggered by JUMP keys or TOUCHSTART. ([source](https://github.com/wayou/t-rex-runner/blob/gh-pages/index.js))
- index.js contains zero matches for multiplayer, socket/websocket, peer, second player, gamepad, joystick, gyroscope, accelerometer, or device-orientation/motion terms, supporting a single-player, keyboard/mouse/touch-only reading; no AI creation models are attributed anywhere in the project sources (a 2014 Chromium extraction). ([source](https://github.com/wayou/t-rex-runner/blob/gh-pages/index.js))
- No catalog game matched this project: the local catalog index and all 20 linked game READMEs were read, and a search for t-rex/trex/wayou across games/ found no prior entry, so no existing slug is reused. ([source](https://github.com/agents-dev/Astra-Top-Games))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 85/100: \[Fictional review\] One-more-try perfection: I kept tapping through the night cycle chasing my hi-score and every cactus felt fair. The purest two-button reflex loop ever shipped in a browser tab.
- 55/100: \[Fictional review\] Made-up casual note: fun for a few minutes and it runs anywhere, but it is one dino jumping over cacti on a blank white strip with no levels, rivals, or progression. I saw everything in the first run.
- 100/100: \[Fictional review\] Invented minimalist take: extracted from a browser error page and played by billions, this is the most validated endless runner in history. Doing this much with pixels, a speed ramp, and day-night shading is absurd efficiency.

## Links

- [Source repository](https://github.com/wayou/t-rex-runner)
- [Play the game](https://wayou.github.io/t-rex-runner/)
