# curiositY

[Open the game source](https://github.com/sharkdp/curiosity)

**Overall rating:** 18/100. Far below all three catalog games on AAA proximity. Kart Royale (50) and Turbo Kart Rally (40) are complete 3D kart racers with physics, AI fields, items, HUDs and stylized 3D worlds; Neural Sight (30) is a WebGPU Gaussian-splat FPS prototype with photographic scenes. Curiosity has a complete 15-level riddle loop and genuinely clever multi-discipline puzzle design (view-source, console, terminal, CSV, unicode, geography), which beats a bare demo on gameplay depth per unit of code, but its scope is ~200 tiny static files, its visual presentation is near-zero (unstyled text pages under one banner, single decorative font), and its technical execution is static hosting plus small scripts rather than an engine. It earns points for a finished, hand-tuned loop with log-driven dead ends, yet sits clearly beneath Neural Sight's rendering tech and the kart racers' systems depth. Evidence gaps: judged from repository content via gh api plus the live landing page only; no full playthrough of all 15 levels, no solution verification, no traffic or completion data, and no audio, animation, persistence, or accessibility evidence. Static pages alone cannot prove pacing, difficulty balance, or hint sufficiency.

**Screenshot score:** not scored. No inspectable gameplay screenshot.

## Screenshots

![Inspected 709x120 PNG: striped art-deco style CURIOSITY wordmark logo on white, letter Y partly faded. Title branding asset, not gameplay; no game scene, HUD, character, or level content visible.](https://raw.githubusercontent.com/sharkdp/curiosity/master/assets/curiosity.png)

Inspected 709x120 PNG: striped art-deco style CURIOSITY wordmark logo on white, letter Y partly faded. Title branding asset, not gameplay; no game scene, HUD, character, or level content visible.

## Play

- Open the live site at https://shark.fish/curiosity in a desktop browser; it redirects to the first level.
- Read each minimal level page carefully: the riddle is often in the page text, the link URLs, or the filename itself.
- Try editing the URL directly: many levels are solved by guessing the next filename, and wrong guesses land on hand-written dead-end pages.
- Use View Source and the browser developer console on levels about HTML tags, JavaScript, and hidden code.
- Work through all 15 levels in order (URL guessing, HTML source, JS console, fake terminal, SVG layers, Hitchhiker trivia, binary, CSV point cloud, pi digits, git tricks, unicode rainbows, debug puzzles, geography) to reach the finish page.
- If stuck, note the author added hints to some levels over time (e.g. levels 13 and 15); there is no in-game hint button.

## Mechanics

- URL-guessing navigation: progress by replacing filenames in the address bar across 15 numbered level folders
- Hand-authored dead-end pages for wrong guesses, expanded from real 404s found by parsing Apache access logs
- View-source riddles: clues hidden in HTML tags, filenames, stylesheets, and page source
- Browser-console and JavaScript puzzles, including an obfuscated fake terminal level built on jQuery Terminal
- SVG layer inspection puzzle with hidden text in vector paths
- Encoding and trivia puzzles: binary/hex filenames, Hitchhiker's Guide 42 references, pi digits
- CSV point-cloud puzzle solvable with a provided Python sampling script (5000-point torus)
- Git-themed and unicode-themed levels (emoji/rainbow codepoints, ISO 10646)
- Geography finale: compass/antarctica/south-pole themed pages
- Custom 404 page as a game mechanic that sends the player back instead of ending the run

## Tags

- puzzle
- riddle
- browser-game
- text
- web-riddle
- point-and-click
- single-player
- static-site

## Reconstructed prompt

Build curiositY, a minimalist browser riddle trail in pure static HTML/CSS/JS: 15 handcrafted levels plus a finish page, each a tiny themed puzzle (URL guessing, view-source HTML, JS console, fake terminal, SVG layers, 42 trivia, binary, CSV point cloud, pi, git, unicode rainbows, debug tricks, geography). Wrong guesses land on witty dead-end pages; add a custom 404 that sends players back. Style it with one decorative banner font and muted pastel CSS, no engine, no build step, no accounts.

## Source evidence

- Repo is sharkdp/curiosity, described as 'How far does your curiosity take you?', tagged browser-game/math/puzzle, ~390 KB, ~202 files, mostly HTML/CSS with small JS/Python, 127 stars. ([source](https://github.com/sharkdp/curiosity))
- Root README contains only the title and a play link to the live site; the game itself is the levels/ directory. ([source](https://github.com/sharkdp/curiosity/blob/master/README.md))
- Levels directory holds 15 numbered levels (level001-level015) plus a finish folder and a spoiler warning, confirming the full scope. ([source](https://github.com/sharkdp/curiosity/tree/master/levels))
- Level 1 is URL-guessing: an index page of colored box links (no/middle/yes/curiosity/win etc.) teaching players to probe filenames. ([source](https://github.com/sharkdp/curiosity/blob/master/levels/level001/index.html))
- Level 5 centers on a fake in-browser terminal (jQuery Terminal, obfuscated terminal.js built from terminal.original.js via jsobfuscate). ([source](https://github.com/sharkdp/curiosity/blob/master/levels/level005/terminal.html))
- Level 6 is an SVG inspection puzzle with hidden layers and text inside vector paths. ([source](https://github.com/sharkdp/curiosity/blob/master/levels/level006/blob.svg))
- Level 7 is Hitchhiker's Guide trivia (42/adams/douglas/hitchhiker/fortytwo filenames); level 8 is binary/hex filename encodings. ([source](https://github.com/sharkdp/curiosity/tree/master/levels/level007))
- Level 9 is a 3D-shape CSV puzzle with a Python script sampling 5000 points on a torus (RADIUS 10, INNER\_RADIUS 3, seed 1). ([source](https://github.com/sharkdp/curiosity/blob/master/levels/level009/sample_points.py))
- Level 11 is git/wordplay themed with hashed filenames; level 13 is unicode rainbow/emoji codepoints (1F308, 4CCF, ISO10646). ([source](https://github.com/sharkdp/curiosity/tree/master/levels/level013))
- Level 14 ends with a JS trick page leading to level 15's geography pages (compass/antarctica/southpole/ocean), then a finish page with only a congratulations note and GitHub watch button. ([source](https://github.com/sharkdp/curiosity/blob/master/levels/finish/eof.html))
- Dead ends are a designed mechanic: misc/parse.py mines Apache access logs for 404 requests to add more wrong-guess pages per level. ([source](https://github.com/sharkdp/curiosity/blob/master/misc/parse.py))
- Presentation is minimal: one shared stylesheet (Monoton/Raleway/Source Code Pro fonts, pastel palette) and a custom 404 page reading 'Hmm... no. Go back'. ([source](https://github.com/sharkdp/curiosity/blob/master/assets/main.css))
- Only raster image in the repo is the curiosity.png wordmark logo (709x120, inspected: striped CURIOSITY lettering, no gameplay); the only other image is the level-6 puzzle SVG, not art. ([source](https://github.com/sharkdp/curiosity/blob/master/assets/curiosity.png))
- Commit history shows sporadic hint additions (e.g. 'Add hint for almost completing level 15', extra level-13 hints), indicating hand-tuned difficulty with no hint system. ([source](https://github.com/sharkdp/curiosity/commits/master))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 65/100: \[Fictional review\] Imagined puzzle fan: level 5's fake terminal got me good, and the dead-end pages made every wrong guess feel like the author was watching. Wish it looked like more than a stylesheet, though.
- 40/100: \[Fictional review\] Made-up casual player note: clever riddles, but plain text pages with no art, sound, or hints system wore me out by level 9. I brute-forced the CSV one and felt nothing.
- 85/100: \[Fictional review\] Invented web-dev take: a masterclass in doing a lot with static files — view-source puzzles, console tricks, and a 404 page as a game mechanic. Short, sharp, and free.

## Links

- [Source repository](https://github.com/sharkdp/curiosity)
- [Related link](https://shark.fish/curiosity)
