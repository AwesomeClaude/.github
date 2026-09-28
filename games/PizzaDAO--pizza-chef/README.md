# Pizza Chef

[Play the game](https://pizza-chef-six.vercel.app) · [View source](https://github.com/PizzaDAO/pizza-chef)

| Overall rating | Screenshot score |
| :---: | :---: |
| **44/100** | **Not scored** |

<details>
<summary>Read the scoring rationale</summary>

### Overall rating

Far from AAA (no 3D, voice, cinematics, multiplayer) but a complete real-time arcade loop with unusually broad systems: 4-lane cooking/serving/plate-catching, 8 customer variants, 10 power-ups, bosses, UFO/raids, store economy, workers, death replay and Supabase leaderboard across ~160 tracked files with tests. Most relevant comparators: neverquest (45, deeper RPG systems but text-UI only), Wilderness (44, similar scope tier), SpaceHo2 (42) and Turbo Kart Rally (40, complete indie loop but single-track/simple systems) - Pizza Chef sits with Wilderness just below neverquest/THORNMERE (46) because visual polish is unverified (only empty background, How-to-Play card and icon inspected, no full gameplay frame with entities/HUD), and below catalog-top Ashlands (55) and Kart Royale (50) on technical ambition and proven rendering. Above 2048 (38), Taipo (35) and Blackjack (28) on depth and scope. Evidence gaps: no live playthrough; playability, performance, balance and mobile feel judged from code and docs only, not motion.

### Screenshot score

No inspectable gameplay screenshot.

</details>

## At a glance

| Detail | Value |
| --- | --- |
| Repository created | 09 Jan 2026 · 10:26 UTC |
| Added to catalog | 27 Sep 2026 · 03:49 UTC |
| Last updated | 27 Sep 2026 · 03:49 UTC |
| Documented creation models | Not established |

## Screenshots

![Inspected empty gameplay arena background (2560x1536 WebP): left brick wall with 4 glowing pizza ovens, white marble divider, wooden floor with red velvet ropes marking 3 lanes. Clean coherent cartoon style but no chef, customers, HUD, or effects visible - background plate only, not a full gameplay frame.](https://pizza-chef-assets.pages.dev/backgrounds/pizza-shop-background.webp)

Inspected empty gameplay arena background (2560x1536 WebP): left brick wall with 4 glowing pizza ovens, white marble divider, wooden floor with red velvet ropes marking 3 lanes. Clean coherent cartoon style but no chef, customers, HUD, or effects visible - background plate only, not a full gameplay frame.

![Inspected 1219x765 How to Play menu card: Move chef up/down, Heat pizza in oven and take it out, Serve pizza to customers, with power-up icons (hot honey, sundae, beer, star, doge, nyan cat) and customer faces. Menu/instruction art, not live gameplay; discounted for graphics scoring.](https://pizza-chef-assets.pages.dev/ui/controls.png)

Inspected 1219x765 How to Play menu card: Move chef up/down, Heat pizza in oven and take it out, Serve pizza to customers, with power-up icons (hot honey, sundae, beer, star, doge, nyan cat) and customer faces. Menu/instruction art, not live gameplay; discounted for graphics scoring.

![Inspected 630x630 promotional icon: flat chef emoji with mustache and white hat on solid red background. Title/icon art only, no gameplay scene; discounted for graphics scoring.](https://raw.githubusercontent.com/PizzaDAO/pizza-chef/main/public/og-image.png)

Inspected 630x630 promotional icon: flat chef emoji with mustache and white hat on solid red background. Title/icon art only, no gameplay scene; discounted for graphics scoring.

## Play

- Press Start Game on the splash screen (or Enter) to begin
- Move chef between 4 lanes with Up/Down arrows (desktop) or on-screen arrow buttons / tap above or below chef (mobile)
- Press Left arrow or Space (or tap chef / oven button) to start cooking and take out pizza; take slices before ovens burn and clean burned ovens
- Press Right arrow (or tap right side / pizza button) to serve a slice to the customer in your lane before they reach the counter
- Catch returning empty plates for bonus points; collect falling power-ups (beer, hot honey, sundae, star, doge, nyan) for effects
- Earn score and bank, spend in the Item Store on oven upgrades, speed, power-ups and workers; survive bosses, aliens, health-inspector raids and level-ups; pause with P

## Mechanics

- 4-lane real-time serve-or-lose customer advance
- Oven cooking timing with warning, burn and cleaning states plus speed/capacity upgrades
- 8-slice carry limit and slice inventory management
- Empty-plate catch bonus loop
- 8 customer variants with special behaviors (critic, Bad Luck Brian, Scumbag Steve, health inspector, delivery driver, Pizza Mafia, alien)
- 10 power-ups with timed effects and Nyan sweep
- Boss battles with minions and collision masks
- UFO alien drop/pickup and health-dept raid events
- Level progression, streak multipliers, lives/stars, and skill rating
- Item store economy with bank, upgrades, bribes, workers and Pepe helpers
- Global Supabase high scores, sessions and scorecard images
- Death replay, pause menu, splash, instructions and game-over stats

## Tags

- arcade
- cooking
- time-management
- tower-defense
- boss-battler
- 2d
- single-player

## Controls

- Mobile controls: Supported
- Motion controls: Not established
- Gamepad: Not established
- Keyboard/mouse: Supported

## Player modes

- Human players: 1
- Modes: single-player

## Reconstructed prompt

Build a fast-paced 2D arcade pizza-shop game in React + TypeScript + Vite with 4 lanes: move a chef up/down, cook pizzas in lane ovens with cook/warning/burn/clean states, serve slices to advancing customers, catch empty plates. Include 8 customer variants, 10 power-ups, boss battles, UFO/alien events, item store with oven upgrades and workers, streaks, death replay, portrait and landscape boards with on-screen touch controls, keyboard controls, procedural Web Audio sounds, and Supabase global high scores.

## Source evidence

- Repository PizzaDAO/pizza-chef exists, is public, described as 'Pizza Chef game - refactored version', language TypeScript, homepage https://pizza-chef-six.vercel.app ([source](https://api.github.com/repos/PizzaDAO/pizza-chef))
- Game page for the same repo confirms description and homepage link to playable Vercel build ([source](https://github.com/PizzaDAO/pizza-chef))
- Architecture doc defines fast-paced arcade game: cook pizzas in ovens, serve customers across four lanes, catch empty plates, with upgrade system, power-ups, and global high-score leaderboard; stack React 18 + TypeScript + Vite + Tailwind + Supabase + Web Audio ([source](https://raw.githubusercontent.com/PizzaDAO/pizza-chef/main/architecture.md))
- Deployed Vercel build returns HTTP 200 HTML with title Pizza Chef, meta description 'Serve pizza, get power-ups, and battle big pizza in this fast-paced pizza slinging game!', root div and JS bundle - playable SPA, not just repo or screenshot ([source](https://pizza-chef-six.vercel.app))
- Same deployment HTML served at canonical og:url domain pizzachef.meme, confirming it is the official play domain ([source](https://pizzachef.meme/))
- Keyboard controls documented: Up/Down to move chef, Left or Space to use oven, Right to serve, P to pause; plus Enter/Escape handling and Space/ArrowLeft/Right/Up/Down listeners in App.tsx ([source](https://github.com/PizzaDAO/pizza-chef/blob/main/src/components/InstructionsModal.tsx))
- Mobile touch controls implemented: dedicated MobileGameControls with on-screen up/down, serve-pizza and oven buttons, tap above/below chef to move, tap chef for oven, tap right side to serve; viewport locked with touch-action manipulation and touchstart skip handlers ([source](https://github.com/PizzaDAO/pizza-chef/blob/main/src/components/MobileGameControls.tsx))
- Single-player design: one chefLane, single score/bank/lives state, global leaderboard via Supabase, no multiplayer, co-op or versus code; all opponents are AI customer variants (normal, critic, badLuckBrian, scumbagSteve, healthInspector, deliveryDriver, pizzaMafia, alien) ([source](https://github.com/PizzaDAO/pizza-chef/blob/main/src/types/game.ts))
- No gamepad, accelerometer or gyroscope support found in components, hooks, or constants; only keyboard, mouse-clickable buttons and touch controls are evidenced ([source](https://github.com/PizzaDAO/pizza-chef/blob/main/src/App.tsx))
- Scanned local catalog index and all game directories for pizza/chef matches; no existing pizza-chef entry found, so no slug reuse ([source](https://github.com/AwesomeClaude/.github/blob/main/README.md))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 85/100: Four ovens beeping, plates flying, a critic with a monocle bearing down - brilliant lunch-rush panic with real upgrade strategy.
- 62/100: Fun core loop and wild power-ups, but I want to see a full crowded rush in action before I chase the leaderboard.
- 100/100: Pizza Mafia burst saved my run and the Nyan sweep cleared the screen - instant arcade classic!

## Links

- [Source repository](https://github.com/PizzaDAO/pizza-chef)
- [Play the game](https://pizza-chef-six.vercel.app)
- [Official play domain](https://pizzachef.meme/)
