# 2048

[Open the game source](https://github.com/gabrielecirulli/2048)
[Play the game](https://play2048.co/)
[Previous report](https://github.com/agents-dev/Astra-Top-Games/blob/f74936bf945284f98485556c55b8c7b477b69177/games/gabrielecirulli--2048/README.md)
**Repository created:** 2014-03-05T16:03:26Z
**Added to catalog:** 2026-09-27T01:22:14Z
**Updated in catalog:** 2026-09-27T03:34:34.296548+00:00

**Overall rating:** 38/100. Same game as catalog gabrielecirulli--2048 (38/100), resubmitted via its official homepage play2048.co. One flawless 4x4 sliding-merge loop, shipped on web plus iOS/Android with 13.4k stars and 17.6k forks evidencing mass validation. Against the catalog it sits above flat single-screen casuals such as TypeScript-Blackjack (28), chess rot (30), and Top-10 Tension (32) on tuning and proven appeal, roughly alongside Taipo (35) and Wouf Kart (38) as complete but narrow in scope, and trails Turbo Kart Rally (40), THORNMERE (46), and catalog-top Ashlands (55) enormously on scope, depth, and audiovisual richness. Nowhere near AAA: no 3D scene, audio design, narrative, or progression. Evidence gaps: play2048.co requires JavaScript so gameplay was verified from page scaffolding plus the mirrored playable DOM and repo files, not a live playthrough; animations, feel, performance, and spawn balance unmeasured.

**Screenshot score:** 45/100. First image is the game's own full-board output: clean cream board, readable color progression, gold 2048 tile with You win overlay. Coherent and iconic but flat DOM tiles with no scene, lighting, or compositional depth. It ranks below richer catalog frames such as Kart Royale and Turbo Kart Rally (70), THORNMERE (60), and Taipo (55), and above plainer flat UIs such as chess rot (40) and Blackjack/Beachy (35). Second image is a curated angled promotional crop with beveled tiles, discounted as non-full gameplay reference. Still images only; motion and feel cannot be judged.

## Screenshots

![Inspected 584x728 PNG of the game's own runtime output: full 4x4 board on cream background with orange/gold numbered tiles (32, 8, 4, 2, 16, highlighted gold 2048 tile), 2048 masthead, score box 12328, and You win overlay across the grid. Flat minimal DOM-tile design; repo author notes the frame is staged.](https://cloud.githubusercontent.com/assets/1175750/8614312/280e5dc2-26f1-11e5-9f1f-5891c3ca8b26.png)

Inspected 584x728 PNG of the game's own runtime output: full 4x4 board on cream background with orange/gold numbered tiles (32, 8, 4, 2, 16, highlighted gold 2048 tile), 2048 masthead, score box 12328, and You win overlay across the grid. Flat minimal DOM-tile design; repo author notes the frame is staged.

![Inspected 1200x630 promotional crop from play2048.co: angled close-up of beveled tiles showing 8, 64, 4, 256, 2, 16, 32 with soft shadows and glow on the 256 tile. Only a partial board is visible, no score, masthead, or full grid; curated reference imagery rather than a full gameplay frame.](https://play2048.co/ogImage.jpg)

Inspected 1200x630 promotional crop from play2048.co: angled close-up of beveled tiles showing 8, 64, 4, 256, 2, 16, 32 with soft shadows and glow on the 256 tile. Only a partial board is visible, no score, masthead, or full grid; curated reference imagery rather than a full gameplay frame.

## Play

- Open the playable game at https://play2048.co/ in a browser with JavaScript enabled
- Slide all tiles at once with arrow keys or swipe on touch screens
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

## Reconstructed prompt

Build a minimal single-page web sliding-tile puzzle on a 4x4 grid: arrow keys and touch swipes move all tiles; equal tiles merge with scoring; spawn a 2 or 4 after each move; detect win at 2048 and game over; persist best score; style with a warm flat palette, beveled tiles, and smooth animations.

## Source evidence

- play2048.co page title is '2048 - Play the Free Online Game' with meta description 'Join the tiles and reach 2048! ... loved by millions' and author/creator Gabriele Cirulli; body contains a JS-mounted \<div id="app"\> plus game bundles, with noscript confirming it is the playable game shell ([source](https://play2048.co/))
- GitHub API identifies gabrielecirulli/2048 as 'The source code for 2048', JavaScript, MIT licensed, 13413 stars and 17581 forks, with homepage https://play2048.co (gh CLI unauthenticated in this environment, so verified via public api.github.com instead) ([source](https://api.github.com/repos/gabrielecirulli/2048))
- Repo About section links play2048.co and the README titles it a small clone of 1024 based on Saming's 2048, shows 13.4k stars and 17.6k forks, and links Play it here plus official Play Store and App Store apps ([source](https://github.com/gabrielecirulli/2048))
- Mirrored playable page loads the actual game DOM: 2048 masthead, score/best display, 4x4 grid containers, New Game button, tagline 'Join the numbers and get to the 2048 tile!', arrow-key how-to-play text, and official-version note ([source](https://gabrielecirulli.github.io/2048/))
- keyboard\_input\_manager.js maps arrow keys plus WASD and Vim HJKL to moves, R to restart, and implements single-touch swipe detection on the game container with touchstart/touchmove/touchend including MSPointer variants; no gamepad or motion-sensor handling is present ([source](https://raw.githubusercontent.com/gabrielecirulli/2048/master/js/keyboard_input_manager.js))
- index.html sets mobile web-app capable viewport with HandheldFriendly/MobileOptimized tags and apple-touch icons, supporting the touch-playable finding; how-to-play text establishes arrow-key keyboard play ([source](https://raw.githubusercontent.com/gabrielecirulli/2048/master/index.html))
- No multiplayer, turn-passing, or networking is mentioned in the repo README, playable pages, or API topics; scoring is solo score plus best-score storage, establishing single-player with one human player ([source](https://github.com/gabrielecirulli/2048))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 90/100: Still the perfect coffee-break puzzle. One more merge turns into twenty minutes and that gold 2048 tile never gets old.
- 65/100: Brilliant and brutally minimal, but it is one 4x4 board with one idea. Great for a week, then you have seen it all.
- 100/100: A flawless little artifact: four directions, endless tension, instantly readable. The clone that became the cultural landmark.

## Links

- [Source repository](https://github.com/gabrielecirulli/2048)
- [Play game](https://gabrielecirulli.github.io/2048/)
- [Related link](https://play2048.co)
- [Play Store app](https://play.google.com/store/apps/details?id=com.gabrielecirulli.app2048)
- [App Store app](https://itunes.apple.com/us/app/2048-by-gabriele-cirulli/id868076805)
- [Original submission](https://play2048.co/)
