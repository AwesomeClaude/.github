# 2048

[Open the game source](https://github.com/gabrielecirulli/2048)
[Play the game](https://gabrielecirulli.github.io/2048/)

**Overall rating:** 38/100. 2048 is the original viral sliding-merge puzzler: one flawless 4x4 loop, officially shipped on web plus iOS/Android, with 13.4k stars and 17.6k forks evidencing mass validation. Against the catalog it sits above flat single-screen casuals (TypeScript-Blackjack 28, chess rot 30, Top-10 Tension 32) on execution polish, tuning, and proven appeal, and roughly alongside Taipo (35) and Wouf Kart (38), which are also complete but narrow in scope; it trails Turbo Kart Rally (40), THORNMERE (46), and the kart/3D tier on scope, depth, and audiovisual richness, and trails catalog-top Ashlands (55) enormously on ambition. It is nowhere near AAA (no 3D, audio design, narrative, or progression systems). Evidence gaps: animations/feel and spawn balance were not playtested, performance unmeasured, so playability and balance claims rest on reputation and code inspection, not verification.

**Screenshot score:** 45/100. The inspected repo screenshot shows the game's own 4x4 board with the gold 2048 tile and a 'You win!' overlay: impeccably clean, instantly readable, iconic color progression. But it is flat DOM tiles with no scene, lighting, texture, or compositional depth, so it ranks below richer catalog frames (Turbo Kart Rally and Kart Royale at 70, THORNMERE at 60, Taipo at 55) and above plainer flat UIs (chess rot 40, Blackjack/Beachy 35) for coherence and cultural polish. Still image only; motion smoothness and feel cannot be judged from it.

## Screenshots

![Inspected 584x728 PNG: the game's own 4x4 board on cream background, orange/gold numbered tiles (32, 8, 4, 2, 16, highlighted gold 2048 tile), '2048' masthead, score box 12328, and a 'You win!' overlay across the grid. Clean flat minimal design; author notes in the README the frame is staged ('That screenshot is fake... I never reached 2048').](https://cloud.githubusercontent.com/assets/1175750/8614312/280e5dc2-26f1-11e5-9f1f-5891c3ca8b26.png)

Inspected 584x728 PNG: the game's own 4x4 board on cream background, orange/gold numbered tiles (32, 8, 4, 2, 16, highlighted gold 2048 tile), '2048' masthead, score box 12328, and a 'You win!' overlay across the grid. Clean flat minimal design; author notes in the README the frame is staged ('That screenshot is fake... I never reached 2048').

## Play

- Open the playable page (https://gabrielecirulli.github.io/2048/) in a browser
- Slide all tiles at once with arrow keys, WASD/HJKL keys, or a swipe on touch screens
- When two tiles with the same number collide they merge into one tile with their sum
- A new tile (2 or 4) spawns after every move, so keep the board from filling up
- Reach the 2048 tile to win; you can keep playing for a higher score afterward
- The game ends when the grid is full and no merges are possible; press New Game or R to restart

## Mechanics

- Slide-the-whole-board movement on a 4x4 grid in four directions
- Equal-tile merging with score awarded per merge
- Random 2/4 tile spawn after each valid move
- Win condition on creating the 2048 tile with optional endless continuation
- Game-over detection when no empty cell and no legal merge exists
- Persistent best-score storage alongside the current score

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

Build a minimal single-page web sliding-tile puzzle on a 4x4 grid: arrow keys, WASD/HJKL, and touch swipes move all tiles; equal tiles merge with scoring; spawn a 2 or 4 after each move; detect win at 2048 and game over; persist best score; style with a warm flat palette and smooth tile animations.

## Source evidence

- Repo page titles it 'The source code for 2048', describes it as a small clone of 1024 based on Saming's 2048 and inspired by Threes, links 'Play it here!' and official Play Store / App Store apps, and shows 13.4k stars and 17.6k forks; About section lists play2048.co ([source](https://github.com/gabrielecirulli/2048))
- Playable page loads the actual game: score/best display, 4x4 grid, New Game button, tagline 'Join the numbers and get to the 2048 tile!', how-to-play text, and iOS/Android app links ([source](https://gabrielecirulli.github.io/2048/))
- How-to-play states movement with arrow keys and merging of equal tiles; repo credits contributors for swipe handling on mobile, Windows Phone swipes, and Android 2.3 support ([source](https://github.com/gabrielecirulli/2048))
- keyboard\_input\_manager.js maps arrow keys, WASD, Vim HJKL, and R-restart, and implements single-touch swipe detection on the game container with touchstart/touchmove/touchend (including MSPointer variants); it contains no gamepad or motion-sensor handling ([source](https://raw.githubusercontent.com/gabrielecirulli/2048/master/js/keyboard_input_manager.js))
- No multiplayer, turn-passing, or networking is mentioned anywhere; scoring is solo score plus best-score storage, establishing single-player ([source](https://github.com/gabrielecirulli/2048))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 95/100: Absurdly moreish. I told myself one more slide and suddenly an hour was gone and I finally saw the 2048 tile glowing gold. Flawless little loop.
- 70/100: Elegant and brutally simple, but it is really just one 4x4 grid. Brilliant for a week, then you have seen everything it will ever do.
- 100/100: A perfect casual artifact: four directions, one idea, infinite tension. The rare clone that outgrew its inspirations and became a cultural landmark.

## Links

- [https://github.com/gabrielecirulli/2048](https://github.com/gabrielecirulli/2048)
- [https://gabrielecirulli.github.io/2048/](https://gabrielecirulli.github.io/2048/)
- [https://play2048.co](https://play2048.co)
- [https://play.google.com/store/apps/details?id=com.gabrielecirulli.app2048](https://play.google.com/store/apps/details?id=com.gabrielecirulli.app2048)
- [https://itunes.apple.com/us/app/2048-by-gabriele-cirulli/id868076805](https://itunes.apple.com/us/app/2048-by-gabriele-cirulli/id868076805)
