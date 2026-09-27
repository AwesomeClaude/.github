# Ballz

[Open the game source](https://github.com/kurtmc/ball-game)
**Repository created:** 2026-04-05T22:46:08Z
**Added to catalog:** 2026-09-27T04:42:43.868463+00:00
**Updated in catalog:** 2026-09-27T04:42:43.868463+00:00

**Overall rating:** 40/100. Far from AAA: one 2D puzzle loop with no 3D scene, narrative, multiplayer, or live-ops scale. Calibrated against all catalog games. Closest comparators are Turbo Kart Rally (40, complete racer with AI field, items, HUD, menus), 2048 (38, flawless single-mechanic viral classic with mass validation), T-Rex Runner (35, single-reflex loop with shipped maturity), and Beachy Beachy Ball (25, single ball-rolling mechanic with minimal art). Ballz sits at the Turbo Kart Rally tier: deeper systems than 2048/T-Rex/Beachy with custom raycast physics, trajectory preview, mutations, Chaos Zone modifiers, drafting, particles, procedural audio, and multi-platform CI (Windows, AppImage, Android APK, .love), but narrower scope and unproven polish versus neverquest (45, deepest catalog systems), THORNMERE (46), OSRS Tower Defense (52), and catalog-top Ashlands (55). Evidence gaps: no inspectable screenshots or video, no browser-playable build so no live playthrough, and code plus spec alone do not prove playability, performance with 100+ balls, or difficulty balance.

**Screenshot score:** not scored. No inspectable gameplay screenshot.

## Play

- Download a desktop build (Windows setup/zip, Linux AppImage) or the Android APK from the releases page, or run ballz.love with the LOVE runtime; there is no browser-playable URL
- Drag upward from the launch point with mouse (desktop) or touch (mobile) to set an angle using the dotted trajectory preview; drag back below the launch line to cancel
- Release to launch balls sequentially at the chosen angle and let them ricochet off walls, ceiling, and numbered blocks, each block hit dealing 1 damage
- Wait for all balls to land; the next launch point moves to where the first ball landed, all blocks descend one row, and a new row plus pickups spawns at the top
- Route balls through ball pickups to grow the ball count for the next turn and chase higher levels without letting any block reach the bottom row
- After level 50 use Chaos Zone mutagens and per-turn draft choices; press space or tap during flight to cycle ball speed, Esc to quit, and any key to restart after game over

## Mechanics

- Drag-to-aim volley launch with dotted first-bounce trajectory preview and near-horizontal angle clamping
- Sequential multi-ball firing with constant speed and elastic wall, ceiling, and block-face reflection
- Numbered HP blocks with level-scaled HP, heat-color difficulty read, destruction pop, particles, and screen shake
- Row descent plus procedural new-row generation each turn with game over when a block reaches the bottom row
- Launch point follows first landed ball with floor collection and stuck-ball auto-return
- Ball pickups that permanently grow ball count plus optional ring currency and grid mutagen pickups
- Chaos Zone after level 50 with per-turn modifiers (gravity, portal walls, big balls, sniper, earthquake, jackpot, triple threat)
- Six stackable ball mutations (heavy, splitter, ghost, kaboom, drunk, magnet) with draft selection
- Flight speed-up toggle, level/score display, restart flow, and local high-score persistence

## Tags

- brick-breaker
- ballz-clone
- turn-based
- puzzle
- arcade
- single-player
- 2d
- love2d
- lua
- procedural-audio
- roguelike-modifiers

## Controls

- Mobile controls: Supported
- Motion controls: Not established
- Gamepad: Not established
- Keyboard/mouse: Supported

## Player modes

- Human players: 1
- Modes: single-player

## Technologies

- **LÖVE 11.4** — engine ([evidence](https://raw.githubusercontent.com/kurtmc/ball-game/master/conf.lua))
- **Lua** — language ([evidence](https://api.github.com/repos/kurtmc/ball-game/languages))
- **love.graphics** — rendering ([evidence](https://raw.githubusercontent.com/kurtmc/ball-game/master/main.lua))
- **Custom 2D physics** — physics ([evidence](https://raw.githubusercontent.com/kurtmc/ball-game/master/physics.lua))
- **love.audio** — audio ([evidence](https://raw.githubusercontent.com/kurtmc/ball-game/master/audio.lua))
- **GitHub Actions** — build ([evidence](https://raw.githubusercontent.com/kurtmc/ball-game/master/.github/workflows/release.yml))
- **Inno Setup** — build ([evidence](https://raw.githubusercontent.com/kurtmc/ball-game/master/installer.iss))

## Reconstructed prompt

Build Ballz, a LOVE2D turn-based brick-breaker in Lua: drag to aim with a dotted first-bounce preview, launch balls sequentially upward into a 7-column grid of numbered HP blocks, reflect off walls/ceiling/blocks with custom 2D physics, collect balls at the floor with launch point following the first landing, spawn a new descending row plus ball pickups each turn, end when a block reaches the bottom row. Add level-scaled HP colors, particles, screen shake, procedural love.audio sounds, ball trails, speed-up toggle, Chaos Zone modifiers and ball mutations after level 50, portrait thumb layout, high-score persistence, and CI builds for Windows installer, Linux AppImage, Android APK, and .love.

## Source evidence

- GitHub API identifies kurtmc/ball-game as a public Lua repository created 2026-04-05, default language Lua, no homepage, no GitHub Pages, 0 stars, 0 forks ([source](https://api.github.com/repos/kurtmc/ball-game))
- Repository page confirms the project is the Ballz brick-breaker game source with Lua files, spec doc, and CI release workflow ([source](https://github.com/kurtmc/ball-game))
- Languages endpoint reports the codebase is overwhelmingly Lua with a small Inno Setup installer script ([source](https://api.github.com/repos/kurtmc/ball-game/languages))
- Game specification defines Ballz as a turn-based brick-breaker: aim, launch ball volley, ricochet damage, collect at floor, advance rows, game over when a block reaches the bottom row ([source](https://raw.githubusercontent.com/kurtmc/ball-game/master/ballz-game-spec.md))
- Spec defines 7-column grid, HP-scaled numbered blocks, ball pickups that grow ball count, dotted trajectory preview with angle clamping, and custom 2D reflection physics ([source](https://raw.githubusercontent.com/kurtmc/ball-game/master/ballz-game-spec.md))
- Spec states input is touch drag on mobile and mouse drag on desktop with direct-aim upward drag and cancel below the launch point ([source](https://raw.githubusercontent.com/kurtmc/ball-game/master/ballz-game-spec.md))
- conf.lua sets the window title to Ballz and targets LOVE version 11.4 with an 800x800 resizable window ([source](https://raw.githubusercontent.com/kurtmc/ball-game/master/conf.lua))
- main.lua implements love.load/update/draw with mouse press/move/release aiming, touch press for ball speed-up, keyboard resize and state keys, and letterboxed scaling with screen shake ([source](https://raw.githubusercontent.com/kurtmc/ball-game/master/main.lua))
- aiming.lua implements mouse-driven aim with minimum-angle clamping, cancellation zone, and dotted raycast trajectory preview including gravity and portal-wall variants ([source](https://raw.githubusercontent.com/kurtmc/ball-game/master/aiming.lua))
- states.lua implements aiming, launching, resolving, collecting, advancing, drafting, and game-over states; spacebar cycles ball speed, number keys draft mutations, escape quits, any other key restarts after game over ([source](https://raw.githubusercontent.com/kurtmc/ball-game/master/states.lua))
- physics.lua implements custom raycast collision against walls and blocks with face detection, ball radius handling, and no ball-ball collision ([source](https://raw.githubusercontent.com/kurtmc/ball-game/master/physics.lua))
- audio.lua generates all sound procedurally with love.sound/love.audio: wall tick, rising-pitch block hits, noise pop on destroy, pickup chime ([source](https://raw.githubusercontent.com/kurtmc/ball-game/master/audio.lua))
- grid.lua defines 7 columns, 11 rows, ball speed and pickup radii, plus portrait layout reserving a thumb aim-drag zone below the floor ([source](https://raw.githubusercontent.com/kurtmc/ball-game/master/grid.lua))
- mutations.lua adds six ball mutations (heavy, splitter, ghost, kaboom, drunk, magnet) and chaos.lua adds post-level-50 Chaos Zone modifiers (gravity, portal walls, big balls, sniper, earthquake, jackpot, triple threat) ([source](https://raw.githubusercontent.com/kurtmc/ball-game/master/mutations.lua))
- Chaos Zone modifiers are rolled per turn after level 50 with banner announcements, confirming extended progression systems beyond the MVP loop ([source](https://raw.githubusercontent.com/kurtmc/ball-game/master/chaos.lua))
- Release workflow builds Windows, Linux AppImage, Android APK, and .love artifacts with LOVE 11.5 for Windows, stamping per-commit versions ([source](https://raw.githubusercontent.com/kurtmc/ball-game/master/.github/workflows/release.yml))
- Releases API lists only downloadable artifacts (ballz-android.apk, setup exe, win64 zip, AppImage, ballz.love) with no browser-playable build; repository has\_pages is false and homepage is null ([source](https://api.github.com/repos/kurtmc/ball-game/releases))
- installer.iss packages the Windows build with Inno Setup under the Ballz name linked to the source repository ([source](https://raw.githubusercontent.com/kurtmc/ball-game/master/installer.iss))
- Recursive file tree contains only Lua sources, docs, CI config, and installer script with no PNG, JPG, GIF, or video screenshots to inspect ([source](https://api.github.com/repos/kurtmc/ball-game/git/trees/master?recursive=1))
- No catalog game matched this project: local catalog index and game READMEs were read and a search for kurtmc, ball-game, and ballz across games/ found no prior entry, so no existing slug is reused ([source](https://github.com/kurtmc/ball-game))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 78/100: Fictional illustrative review: the aim-preview plus volley cascade is pure one-more-turn juice, and my first Chaos Zone gravity turn completely changed my angles.
- 55/100: Fictional illustrative review: solid clone with fun mutations on paper, but flat dark-grid presentation and one loop mean runs blur together fast.
- 100/100: Fictional illustrative review: splitter plus kaboom chain reactions with a hundred balls bouncing is the most satisfying spreadsheet-destruction toy here.

## Links

- [Source repository](https://github.com/kurtmc/ball-game)
- [Game specification](https://github.com/kurtmc/ball-game/blob/master/ballz-game-spec.md)
- [Release downloads](https://github.com/kurtmc/ball-game/releases)
