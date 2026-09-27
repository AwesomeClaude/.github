# hypeJumper

[Open the game source](https://github.com/parkjongbin0520-spec/hypeJumper)
**Repository created:** 2026-06-01T02:23:07Z
**Added to catalog:** 2026-09-27T04:41:33.536018+00:00
**Updated in catalog:** 2026-09-27T04:41:33.536018+00:00
**Built with:** [Opus 4.8](https://raw.githubusercontent.com/parkjongbin0520-spec/hypeJumper/main/CLAUDE.md)

**Overall rating:** 36/100. Far from AAA: small prototype scope with no browser play, no verified gameplay visuals, no multiplayer, narrative, or live-ops scale. Most relevant comparators: Flip Runner Racing (33, ten-level hill-climb with fuel/flips/chute but a one-shot with no live URL), Taipo (35, complete typing-TD loop with multi-year releases and itch ratings), T-Rex Runner (35, single flawless reflex loop with massive validation), 2048 (38, mass-validated flawless merge loop), and Turbo Kart Rally (40, complete 3D kart loop with AI field, items, and menus). hypeJumper sits just above Flip Runner and around Taipo/T-Rex: its Celeste-grade movement tech (coyote, buffers, 8-way dash, super/hyper/wallbounce, grab puzzles), six text-map stages, dual Python plus frame-parity C#/MonoGame implementations with 21 passing tests, and two shipped Windows releases beat Flip Runner on technical depth, but it trails 2048 on proven tuning and validation and trails Turbo Kart Rally badly on scope, opponents, and rendered world richness. Catalog top Ashlands (55) is far ahead on world scale. Evidence gaps: no browser-playable build, no inspectable gameplay screenshots, and no live playthrough, so playability, performance, balance, and audio quality are unverified and source files do not prove them.

**Screenshot score:** not scored. No inspectable gameplay screenshot.

## Screenshots

![Inspected 545x340 PNG: crude level-design sketch, not runtime gameplay output. White background with chunky black block terrain steps, two small flat orange platforms joined by a double-headed orange arrow, and a thin orange vertical line at the right edge. No player, enemies, HUD, lighting, or rendered game scene; documents intended moving-platform spacing rather than the shipped visual presentation.](https://raw.githubusercontent.com/parkjongbin0520-spec/hypeJumper/main/exampleMap.png)

Inspected 545x340 PNG: crude level-design sketch, not runtime gameplay output. White background with chunky black block terrain steps, two small flat orange platforms joined by a double-headed orange arrow, and a thin orange vertical line at the right edge. No player, enemies, HUD, lighting, or rendered game scene; documents intended moving-platform spacing rather than the shipped visual presentation.

## Play

- Download a Windows build from the Releases page (v0.1.0 HypeJumper.exe or v0.2.0 HypeJumper-csharp-win-x64.zip) or run python main.py with pygame-ce installed.
- On the title screen press any key to start; press ESC to open the pause menu (resume or quit).
- Move with Left/Right arrows or A/D; hold C for higher variable jumps and use coyote time and jump buffering on edges.
- Press X to dash in 8 directions, chain super, hyper, and wallbounce jumps, and wall-slide or wall-jump on walls.
- Press Z to grab puzzle targets, S or Down to duck or fast-fall, R to reset the room, and touch the goal to advance through stages 1-5; avoid spikes and enemies.

## Mechanics

- Celeste-style Approach acceleration with ground and air control multipliers
- Variable-height jump with 3-stage gravity plus coyote time and jump buffering
- 8-direction dash with end-dash speed retention
- Super, hyper, and wallbounce momentum jumps
- Wall slide and wall jump with forced-move timers
- Grab-based puzzle mechanic with aim window and slow motion
- Armored and basic enemies plus rope NTT objects
- Moving platforms with rider carry and push resolution
- Jump pads and wall springs
- Spikes and hazard death with checkpoint respawn
- Six text tilemap stages with goal-triggered progression
- Title, playing, and paused game states with debug HUD

## Tags

- 2d-platformer
- precision-platformer
- celeste-like
- puzzle-platformer
- pixel-art
- single-player

## Controls

- Mobile controls: Not established
- Motion controls: Not established
- Gamepad: Not established
- Keyboard/mouse: Supported

## Player modes

- Human players: 1
- Modes: single-player

## Technologies

- **Python** — language ([evidence](https://raw.githubusercontent.com/parkjongbin0520-spec/hypeJumper/main/CLAUDE.md))
- **pygame-ce 2.5.7** — framework ([evidence](https://raw.githubusercontent.com/parkjongbin0520-spec/hypeJumper/main/requirements.txt))
- **C#** — language ([evidence](https://raw.githubusercontent.com/parkjongbin0520-spec/hypeJumper/main/csharp/HypeJumper/Game1.cs))
- **.NET 10.0** — framework ([evidence](https://raw.githubusercontent.com/parkjongbin0520-spec/hypeJumper/main/csharp/HypeJumper/HypeJumper.csproj))
- **MonoGame.Framework.DesktopGL 3.8.\*** — framework ([evidence](https://raw.githubusercontent.com/parkjongbin0520-spec/hypeJumper/main/csharp/HypeJumper/HypeJumper.csproj))
- **FontStashSharp.MonoGame 1.5.6** — framework ([evidence](https://raw.githubusercontent.com/parkjongbin0520-spec/hypeJumper/main/csharp/HypeJumper/HypeJumper.csproj))
- **PyInstaller** — build ([evidence](https://raw.githubusercontent.com/parkjongbin0520-spec/hypeJumper/main/hypejumper.spec))

## Reconstructed prompt

Create hypeJumper, a Celeste-inspired 2D precision platformer prototype in Python with Pygame (plus a frame-parity C# MonoGame port): Approach-based run physics, variable jump with coyote time and buffering, 8-way dash, super/hyper/wallbounce tech, wall slide and wall jump, grab puzzles, enemies, springs, moving platforms, spikes, checkpoints, six text-map stages, title and pause screens, jade bio-cyberpunk palette with parallax bamboo and fireflies, and Windows exe releases.

## Source evidence

- GitHub API identifies the repo as parkjongbin0520-spec/hypeJumper on branch main, created 2026-06-01, language C#, no description, no homepage, GitHub Pages disabled, 0 stars and 0 forks. ([source](https://api.github.com/repos/parkjongbin0520-spec/hypeJumper))
- Project docs define the game as a 2D platformer hyper-move jump puzzle referencing Celeste movement (coyote time, jump buffer, dash), built in Python with Pygame as a polished prototype. ([source](https://raw.githubusercontent.com/parkjongbin0520-spec/hypeJumper/main/CLAUDE.md))
- Architecture doc scopes Celeste movement (Approach accel, variable jump, 8-way dash, super/hyper/wallbounce, wall slide and wall jump, coyote time, buffers) with grab logic reserved for Phase 3 puzzles. ([source](https://raw.githubusercontent.com/parkjongbin0520-spec/hypeJumper/main/PLANNING.md))
- requirements.txt pins the Python runtime dependency to pygame-ce==2.5.7. ([source](https://raw.githubusercontent.com/parkjongbin0520-spec/hypeJumper/main/requirements.txt))
- C# port targets net10.0 with MonoGame.Framework.DesktopGL 3.8.\*, MonoGame.Content.Builder.Task 3.8.\*, and FontStashSharp.MonoGame 1.5.6. ([source](https://raw.githubusercontent.com/parkjongbin0520-spec/hypeJumper/main/csharp/HypeJumper/HypeJumper.csproj))
- Python entry point implements keyboard controls: C jump edge and hold, X dash edge, Z grab edge and hold, R reset, ESC pause, arrows or WASD movement, Enter confirm. ([source](https://raw.githubusercontent.com/parkjongbin0520-spec/hypeJumper/main/main.py))
- C# port mirrors keyboard-only input via MonoGame Keyboard state: C jump, X dash, Z grab, R reset, arrows/WASD movement, Escape and Enter menus; InputReader tracks keyboard down and edge states only. ([source](https://raw.githubusercontent.com/parkjongbin0520-spec/hypeJumper/main/csharp/HypeJumper/Game1.cs))
- Scene implements single-player room progression: level index, goal rectangles that trigger next-level loading, checkpoints, respawn, and one tracked player with no network or multiplayer code. ([source](https://raw.githubusercontent.com/parkjongbin0520-spec/hypeJumper/main/src/scene.py))
- Settings define a 960x540 window with a 480x272 internal room target and a LEVEL\_FILES stage 1-5 sequence. ([source](https://raw.githubusercontent.com/parkjongbin0520-spec/hypeJumper/main/settings.py))
- Releases ship Windows-only downloads, not browser play: v0.1.0 single HypeJumper.exe and v0.2.0 HypeJumper-csharp-win-x64.zip folder build with SDL2 and assets; bodies document A/D move, C jump, X dash, Z grab, S duck, R reset, ESC menu. ([source](https://github.com/parkjongbin0520-spec/hypeJumper/releases/tag/v0.2.0))
- Asset docs list 26 player PNGs, bamboo parallax backgrounds, tile, spike, SFX jump/land/dash/death/goal, one stage BGM, and six text tilemaps with missing-asset color-rectangle and mute fallbacks. ([source](https://raw.githubusercontent.com/parkjongbin0520-spec/hypeJumper/main/ASSETS.md))
- The only root-level image is a crude black-and-white block sketch with orange platform markers, inspected as a design sketch rather than gameplay runtime output; no gameplay screenshots, videos, or playable web URLs were found. ([source](https://raw.githubusercontent.com/parkjongbin0520-spec/hypeJumper/main/exampleMap.png))
- No catalog\_slug match: no existing catalog game references this repository, playable URL, or project, so this is a new entry. ([source](https://github.com/parkjongbin0520-spec/hypeJumper))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 78/100: Fictional illustrative review: the dash chains feel fantastic once they click — coyote time and buffers forgive my sloppy jumps, and hyper-tech shortcuts make old rooms worth replaying.
- 55/100: Fictional illustrative review: clever Celeste-style movement trapped in a bare prototype — I like the tech, but with sketch-level visuals and Windows-only downloads I bounced off after a few rooms.
- 100/100: Fictional illustrative review: a perfect hyper-movement sandbox — frame-parity Python and C# builds, six text-map stages, and buttery wallbounces make this the tightest indie precision platformer I have played.

## Links

- [Source repository](https://github.com/parkjongbin0520-spec/hypeJumper)
- [Release v0.2.0 (C# MonoGame Windows build)](https://github.com/parkjongbin0520-spec/hypeJumper/releases/tag/v0.2.0)
- [Release v0.1.0 (Python Windows build)](https://github.com/parkjongbin0520-spec/hypeJumper/releases/tag/v0.1.0)
