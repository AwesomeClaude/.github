# 2048

[Play the game](https://play2048.co/) · [View source](https://github.com/gabrielecirulli/2048) · [Previous report](https://github.com/AwesomeClaude/.github/blob/e866255fc5cb8e58c821c089ae8d9381df1f427d/games/gabrielecirulli--2048/README.md)

| Overall rating | Screenshot score |
| :---: | :---: |
| **38/100** | **45/100** |

<details>
<summary>Read the scoring rationale</summary>

### Overall rating

Exact match of catalog game gabrielecirulli--2048, resubmitted via its repository URL. One flawless 4x4 sliding-merge loop shipped on web plus iOS/Android, with ~13.4k stars and ~17.6k forks evidencing mass validation. Excluding the target itself, it sits above flat single-screen casuals such as TypeScript-Blackjack (28), chess rot (30) and Top-10 Tension (32) on tuning and proven appeal, roughly alongside Taipo (35), T-Rex Runner (35) and Wouf Kart (38) as complete but narrow in scope, and trails Turbo Kart Rally (40), THORNMERE (46) and catalog-top moorestech (64) enormously on scope, depth and audiovisual richness. Nowhere near AAA: no 3D scene, audio design, narrative or progression. Evidence gaps: gh CLI had no auth so GitHub evidence was verified via unauthenticated api.github.com endpoints; no live playthrough instrumented, so animations, feel, performance and spawn balance are unmeasured; inspected docs and game\_manager.js confirm the rules but do not prove balance or performance.

### Screenshot score

First image is the game's own full-board output: clean cream board, readable color progression, gold 2048 tile with You win overlay. Coherent and iconic but flat DOM tiles with no scene, lighting or compositional depth. It ranks below richer catalog frames such as Kart Royale and Turbo Kart Rally (70), THORNMERE (60) and Taipo (55), and above plainer flat UIs such as chess rot (40) and Blackjack/Beachy (35). Second image is a curated angled promotional crop, discounted as non-full gameplay reference. Still images only; motion and feel cannot be judged.

</details>

## At a glance

| Detail | Value |
| --- | --- |
| Repository created | 05 Mar 2014 · 16:03 UTC |
| Added to catalog | 27 Sep 2026 · 01:22 UTC |
| Last updated | 28 Sep 2026 · 04:51 UTC |
| Documented creation models | Not established |

## Screenshots

![2048 gameplay](screenshots/2ea0f7b8349639636fdb6ffac8bb1e48f37e8beda89bab25843e0637c9f4495b.png)

Inspected 584x728 PNG of the game's own runtime output: cream page with 2048 masthead, tagline 'Join the numbers and get to the 2048 tile!', score box 12328, full 4x4 board with flat orange/gold numbered tiles (32, 8, 4, 2, 16, highlighted gold 2048 tile) and a 'You win!' overlay across the grid. Flat minimal DOM-tile design; repo author notes the frame is staged.

[Original screenshot](https://cloud.githubusercontent.com/assets/1175750/8614312/280e5dc2-26f1-11e5-9f1f-5891c3ca8b26.png)

![2048 gameplay](screenshots/bd9f3bef2985fc2ecbc88541cf9b8d696a12cae07b85511a853e0322fa4cba72.jpg)

Inspected 1200x630 JPEG promotional crop from play2048.co: angled close-up of beveled tiles showing 8, 64, 4, glowing 256, 2, 16, 32 with soft shadows on a taupe tray. Only a partial board is visible with no score, masthead or full grid; curated reference imagery rather than a full gameplay frame.

[Original screenshot](https://play2048.co/ogImage.jpg)

## Play

- Open the playable game at https://play2048.co/ in a browser with JavaScript enabled
- Slide all tiles at once with arrow keys (or WASD) or swipe on touch screens
- When two tiles with the same number touch they merge into their sum
- A new 2 or 4 tile spawns after each move, so avoid filling the 4x4 grid
- Reach the 2048 tile to win; keep going for a higher score afterward
- The game ends when the grid is full with no merges possible; start a New Game to restart

## Mechanics

- Slide-the-whole-board movement on a 4x4 grid in four directions
- Equal-tile merging with score awarded per merge
- Random 2/4 tile spawn after each valid move
- Win condition on creating the 2048 tile with endless continuation
- Game-over detection when no empty cell and no legal merge exists
- Persistent best-score storage alongside current score

## Tags

- puzzle
- sliding-tile
- merge
- casual
- browser
- single-player
- minimal
- viral-classic

## Controls

- Mobile controls: Supported
- Motion controls: Not established
- Gamepad: Not established
- Keyboard/mouse: Supported

## Player modes

- Human players: 1
- Modes: single-player

## Technologies

- **JavaScript** — language ([evidence](https://api.github.com/repos/gabrielecirulli/2048/languages))
- **HTML** — language ([evidence](https://api.github.com/repos/gabrielecirulli/2048/languages))
- **CSS** — language ([evidence](https://api.github.com/repos/gabrielecirulli/2048/languages))

## Reconstructed prompt

Build a minimal single-page web sliding-tile puzzle on a 4x4 grid: arrow keys and touch swipes move all tiles; equal tiles merge with scoring; spawn a 2 or 4 after each move; detect win at 2048 and game over; persist best score; style with a warm flat palette, beveled tiles, and smooth animations.

## Source evidence

- GitHub API identifies gabrielecirulli/2048 as 'The source code for 2048', primary language JavaScript, MIT license, ~13.4k stars and ~17.6k forks, homepage https://play2048.co, topics 2048/2048-game/game/javascript/online-game/puzzle-game, created 2014-03-05 (verified via unauthenticated api.github.com because gh CLI has no auth in this environment) ([source](https://api.github.com/repos/gabrielecirulli/2048))
- Repo page and raw README describe it as 'a small clone of 1024 based on Saming's 2048', 'Made just for fun. Play it here!', with official Play Store and App Store app links and an embedded screenshot the author notes is staged/fake ('I never reached 2048') ([source](https://github.com/gabrielecirulli/2048))
- Repo file listing shows index.html, style/, meta/, and js/ with game\_manager.js, grid.js, tile.js, html\_actuator.js, keyboard\_input\_manager.js, local\_storage\_manager.js, application.js plus polyfills ([source](https://api.github.com/repos/gabrielecirulli/2048/contents/))
- keyboard\_input\_manager.js maps arrow keys plus WASD and Vim HJKL to moves and R to restart, and implements single-touch swipe detection on the game container with touchstart/touchmove/touchend including MSPointer variants; no gamepad or motion-sensor handling is present ([source](https://raw.githubusercontent.com/gabrielecirulli/2048/master/js/keyboard_input_manager.js))
- index.html sets mobile web-app capable viewport with HandheldFriendly/MobileOptimized tags and apple-touch icons, and the how-to-play text documents arrow-key keyboard play; together with the swipe handler this establishes touch and keyboard support ([source](https://raw.githubusercontent.com/gabrielecirulli/2048/master/index.html))
- game\_manager.js implements the full loop: 2 starting tiles, move/restart/keepPlaying events, setup with saved-state reload, win/game-over termination checks and endless continuation after winning ([source](https://raw.githubusercontent.com/gabrielecirulli/2048/master/js/game_manager.js))
- play2048.co returns HTTP 200 with title '2048 • Play the Free Online Game', meta description 'Join the tiles and reach 2048!', author/creator Gabriele Cirulli; it is the repo homepage and canonical playable shell ([source](https://play2048.co/))
- gabrielecirulli.github.io/2048 returns HTTP 200 with the full game DOM (scores, game-intro 'Join the numbers and get to the 2048 tile!', New Game button, game-container grid), confirming it is the playable mirror ([source](https://gabrielecirulli.github.io/2048/))
- No multiplayer, turn-passing, or networking is mentioned in the repo README, playable pages, or API topics; scoring is solo score plus best-score storage, establishing single-player with one human player ([source](https://github.com/gabrielecirulli/2048))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 90/100: Still the perfect coffee-break puzzle. One more merge turns into twenty minutes and that gold 2048 tile never gets old.
- 65/100: Brilliant and brutally minimal, but it is one 4x4 board with one idea. Great for a week, then you have seen everything.
- 100/100: A flawless little artifact: four directions, endless tension, instantly readable. The clone that became the cultural landmark.

## Links

- [Source repository](https://github.com/gabrielecirulli/2048)
- [Play game](https://gabrielecirulli.github.io/2048/)
- [Related link](https://play2048.co)
- [Play Store app](https://play.google.com/store/apps/details?id=com.gabrielecirulli.app2048)
- [App Store app](https://itunes.apple.com/us/app/2048-by-gabriele-cirulli/id868076805)
- [Original submission](https://play2048.co/)
