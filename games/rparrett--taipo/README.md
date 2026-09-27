# Taipo

[Open the game source](https://github.com/rparrett/taipo)

**Overall rating:** 35/100. Closest comparators are Turbo Kart Rally (40) and Kart Royale (50): both are complete single-track 3D arcade loops with AI fields, items, physics, HUD/menus and procedural tech. Neural Sight (30) is a 24-hour photographic prototype with no real game loop. Taipo sits between Turbo Kart and Neural Sight at 35: it has a genuinely complete and distinctive loop (typing-only TD economy, three tower roles, Tiled waves, four word lists, Bevy desktop plus web builds, multi-year releases, 4.7/5 from 9 itch ratings), which beats Neural Sight's tech demo scope, but its scope is narrower than either kart game (one small tilemap, a handful of reused/BrowserQuest-adjacent sprites, acknowledged TODO gaps in sound, art, levels, and word lists) and its 2D pixel presentation is flatter and sparser. Evidence gaps: judged from source via gh api plus two still screenshots and the itch page; no live playthrough, no video, no performance, balance, or late-wave depth verified, so playability and tuning are not proven.

**Screenshot score:** 55/100. The inspected English-mode gameplay frame shows coherent readable pixel art (winding road, towers, skeletons, yen and timer HUD, typing buffer) with a charming station-house map, but large flat empty water expanses, sparse decoration, and simple small sprites put it below all three catalog 70s: Kart Royale and Turbo Kart Rally show denser 3D scenes with lighting, crowds, scenery and full race HUDs, and Neural Sight shows photographic captured detail. The second inspected image is a word-list menu overlay, discounted as non-gameplay. Judged from stills only; no motion, feel, or performance inferred.

## Screenshots

![Inspected 1438x954 gameplay frame (English mode): top-down pixel-art TD board with winding gray road, red-roofed towers, skeleton/crab/snake enemies marching the dashed path, BOSS vending machine and station house decor, HUD with 20 yen coin and 0.0 timer, side action-panel prompts (engineer, solar, taut) with enemy labels (gigantic, papal, incomplete, asinine, mourner, hoglet), green range ring around a selected tower, and bottom typing buffer '\> engi'. Clearly the game's own runtime output.](https://img.itch.zone/aW1hZ2UvOTg5MTU0LzU2NjU2MDAucG5n/original/MnHlHT.png)

Inspected 1438x954 gameplay frame (English mode): top-down pixel-art TD board with winding gray road, red-roofed towers, skeleton/crab/snake enemies marching the dashed path, BOSS vending machine and station house decor, HUD with 20 yen coin and 0.0 timer, side action-panel prompts (engineer, solar, taut) with enemy labels (gigantic, papal, incomplete, asinine, mourner, hoglet), green range ring around a selected tower, and bottom typing buffer '\> engi'. Clearly the game's own runtime output.

![Inspected 1440x960 menu overlay frame: same pixel map dimmed behind a centered word-list select modal with Kana, Kana + N5, Kana + N5 + Yamanote, and English buttons. Menu/title selection, not active gameplay; discounted for graphics scoring.](https://img.itch.zone/aW1hZ2UvOTg5MTU0LzU2NjU2MTcucG5n/original/MPZWHj.png)

Inspected 1440x960 menu overlay frame: same pixel map dimmed behind a centered word-list select modal with Kana, Kana + N5, Kana + N5 + Yamanote, and English buttons. Menu/title selection, not active gameplay; discounted for graphics scoring.

## Play

- Open the itch.io page and launch the web build, or download the Windows/macOS/Linux build, or run locally with \`cargo run --release\`.
- On the main menu, pick word lists (Kana, N5 Kanji, Yamanote stops, English) and press Start Game.
- Type the romanized form of a word or phrase shown in the action panel, as in macOS IME (e.g. nn for ん), and press Enter to submit it.
- Type a tower slot label to select it, then type the build prompt to spend 20 yen on a Shuriken (damage), Pupper (buff nearby), or Coffee (boss-armor debuff) tower.
- Type economy and management prompts: plain words earn 1 yen each, upgrade costs 10 yen, selling refunds half, and typing 'help' shows romaji readings.
- Hold the winding road against timed waves of skeletons, crabs, snakes and bosses; do not let enemies reach the goal, and use taunt to force the next wave early.

## Mechanics

- Typing-only control: every action (build, upgrade, sell, select, earn yen, help mode) is triggered by typing a prompt and pressing Enter
- Romaji-to-Japanese parser with chunked prompts, per-glyph tinting, help mode showing readings, and a disambiguating prompt pool
- Tower defense economy in yen: earn 1 per typed word, build for 20, upgrade for 10 (range bonus), sell for half refund
- Three tower roles: single-target damage (Shuriken), nearby damage buff (Pupper), single-target armor-debuff (Coffee) plus boss towers
- Tiled-map wave system with paths, enemy type, count, HP, armor, speed, spawn interval and inter-wave delay per wave
- Enemy roster with animated sprites, health bars, armor and status effects (damage buff / armor shred indicators)
- Range indicator, tower targeting loop, projectiles (shuriken, boss bullets), and tower appearance updates on change events
- Word-list system with Kana, N5 kanji, Yamanote station, and English lists plus selectable menu checkboxes and persisted prefs
- Main menu, playing, and game-over states with currency and wave-timer HUD, action panel, reticle, and volume/mute settings

## Tags

- tower-defense
- typing-game
- educational
- japanese-learning
- 2d
- pixel-art
- bevy
- rust
- browser-game
- singleplayer

## Reconstructed prompt

Build Taipo, a 2D typing tower defense in Rust with Bevy: all control is typing romanized Japanese or English prompts plus Enter. One Tiled winding-road map with timed enemy waves, a yen economy (type words to earn, build/upgrade/sell towers), three tower types (damage, support buff, armor debuff), animated pixel enemies with HP bars, range indicators, four selectable word lists, main menu and game-over flow, and desktop plus WebGL2 web builds.

## Source evidence

- Taipo is a typing tower defense for learning Japanese (plus an English mode), built with Bevy; web build hosted on itch.io. ([source](https://github.com/rparrett/taipo/blob/main/README.md))
- Repo is Rust (~152k lines per gh api languages) with Bevy 0.16, bevy\_ecs\_tilemap, Tiled maps, chumsky parser, and ron word-list data; 21 source files covering typing, towers, enemies, waves, map, UI. ([source](https://github.com/rparrett/taipo/blob/main/Cargo.toml))
- All control is typing prompts: tower selection/build/upgrade/sell, yen generation, language help toggle, and taunt are handled as completed-prompt Actions in main.rs. ([source](https://github.com/rparrett/taipo/blob/main/src/main.rs))
- Typing system uses PromptChunks with displayed vs typed forms, a disambiguating PromptPool, help mode events, and submit-on-Enter matching. ([source](https://github.com/rparrett/taipo/blob/main/src/typing.rs))
- Towers cost 20 yen, upgrades 10 (range +32), sell refunds half; three kinds (Basic damage, Support buff, Debuff armor shred) with range indicators and status-effect sprites. ([source](https://github.com/rparrett/taipo/blob/main/src/tower.rs))
- Waves are Tiled-object driven with enemy type, count, HP, armor, speed, interval and delay; spawners march atlas-animated enemies along paths with health bars. ([source](https://github.com/rparrett/taipo/blob/main/src/wave.rs))
- Word lists shipped: kana.jp.txt, n5.jp.txt, yamanote.jp.txt, english.txt, selectable from the main menu and persisted via prefs. ([source](https://github.com/rparrett/taipo/blob/main/assets/data/game.ron))
- README TODO openly lists gaps: missing sounds (wave/enemy/economy cues), placeholder art (enemies, decorations, tileset, shuriken tower), more levels and words, custom word lists. ([source](https://github.com/rparrett/taipo/blob/main/README.md))
- itch.io page: 2D typing tower defense, type romanized words plus Enter, three towers (Shuriken 1 dmg, Pupper +1 buff, Coffee -2 boss armor), rated 4.7/5 from 9 ratings, HTML5 plus Windows/macOS/Linux builds at v0.7.1. ([source](https://euclidean-whale.itch.io/taipo))
- Project history spans 2020-12 to 2025-05 with releases through v0.7.1; open issues note asset-pack replacement, IME improvements, and help-mode clipping. ([source](https://github.com/rparrett/taipo/issues))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 75/100: \[Fictional review\] Imagined study-session player: typing real Yamanote station names to fund my shuriken towers is weirdly addictive, and the romaji-to-kana snap when a prompt clears feels great. Runs out of surprises after a few waves, but as a Japanese drill disguised as tower defense it totally works.
- 50/100: \[Fictional review\] Made-up casual typist note: cute pixel map and the pupper buff tower made me laugh, but long stretches are just grinding one yen per word while skeletons march, and the flat empty water makes the board feel sparse next to a real TD.
- 100/100: \[Fictional review\] Invented Bevy-fan take: a typing-only tower defense in Rust with a hand-rolled kana parser, Tiled waves, and five years of engine upgrades? Niche, scrappy, and completely charming — I forgive the placeholder art.

## Links

- [Related link](https://euclidean-whale.itch.io/taipo)
- [Source repository](https://github.com/rparrett/taipo)
- [Related link](https://github.com/rparrett/taipo/blob/main/README.md)
