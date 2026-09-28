# Survive Coders

[Play the game](https://survive-coders.vercel.app/) · [View source](https://github.com/travisstephenfraser/survive-coders)

| Overall rating | Screenshot score |
| :---: | :---: |
| **46/100** | **60/100** |

<details>
<summary>Read the scoring rationale</summary>

### Overall rating

Far from AAA: one level plus one boss, hackathon demo scope, no multiplayer, no automated tests, and no verified performance/balance data. Most relevant comparators: Kart Royale (50, complete 3D kart loop, screenshots 70), HEX DANMAKU (48, 24-stage tactics with editor, screenshots 60), THORNMERE (46, full retro RPG, screenshots 60), neverquest (45, large idle-RPG systems, screenshots 30), and Taipo (35, single-map typing TD, screenshots 55). Survive Coders sits beside THORNMERE/HEX: smaller content volume than Kart Royale and OSRS Tower Defense (52) but a complete themed loop (intro, level, rideable vehicle, multi-phase boss, voice/touch input, original victory song) with coherent CRT pixel art and documented game feel, ahead of neverquest/Taipo on scope and polish. Source and stills do not prove playability, performance, or balance.

### Screenshot score

Inspected gameplay frames show coherent night-pixel-art styling: parallax SF skyline, readable platforms/enemies/pickups, full HUD and CRT scanline finish. Best boss frame is dense and composed, comparable to THORNMERE (60) and HEX DANMAKU (60) and above Taipo (55, sparser flat TD board), but below OSRS Tower Defense (65, denser varied battlefield) and Kart Royale/Turbo Kart Rally (70, 3D lighting and depth). Dark palettes and simple sprites cap it. Title frame discounted as non-gameplay. Stills prove nothing about motion, feel, performance, or balance.

</details>

## At a glance

| Detail | Value |
| --- | --- |
| Repository created | 27 Sep 2026 · 00:43 UTC |
| Added to catalog | 27 Sep 2026 · 06:25 UTC |
| Last updated | 27 Sep 2026 · 06:25 UTC |
| Documented creation models | [Claude Opus 5.5](https://raw.githubusercontent.com/travisstephenfraser/survive-coders/master/README.md) |

## Screenshots

![Inspected 1920x1080 PNG: Anthropic HQ boss arena with three chat-bubble Hydra heads on segmented necks, CONTEXT ROT body, boss HP bar, CONTEXT OVERFLOW meter, 'Context Full! HOLD M, say refactor (or press 3)' tip, Furby-like office creatures, player with laptop, star counter 61. Densest gameplay frame with full boss systems and HUD; the game's own runtime output.](https://raw.githubusercontent.com/travisstephenfraser/survive-coders/master/docs/screenshots/10-boss-context-overflow.png)

Inspected 1920x1080 PNG: Anthropic HQ boss arena with three chat-bubble Hydra heads on segmented necks, CONTEXT ROT body, boss HP bar, CONTEXT OVERFLOW meter, 'Context Full! HOLD M, say refactor (or press 3)' tip, Furby-like office creatures, player with laptop, star counter 61. Densest gameplay frame with full boss systems and HUD; the game's own runtime output.

![Inspected 1920x1080 PNG: player riding a glowing red Powell St cable car over a pit labeled 404, Golden Gate Bridge and Transamerica-style skyline behind, star arcs, Keyboard Goblin and blob enemies, '+1 star' pickup text, full power-bar HUD. Clearly the game's own runtime output.](https://raw.githubusercontent.com/travisstephenfraser/survive-coders/master/docs/screenshots/07-cable-car-ride.png)

Inspected 1920x1080 PNG: player riding a glowing red Powell St cable car over a pit labeled 404, Golden Gate Bridge and Transamerica-style skyline behind, star arcs, Keyboard Goblin and blob enemies, '+1 star' pickup text, full power-bar HUD. Clearly the game's own runtime output.

![Inspected 1920x1080 PNG: night street combat with Painted-Ladies-style houses, Sutro Tower, player firing prompt bolts at a blue Bad Prompt Blob, star pickups, health and star HUD, 'SPACE fires prompts' tip and power bar. The game's own runtime output.](https://raw.githubusercontent.com/travisstephenfraser/survive-coders/master/docs/screenshots/05-street-combat.png)

Inspected 1920x1080 PNG: night street combat with Painted-Ladies-style houses, Sutro Tower, player firing prompt bolts at a blue Bad Prompt Blob, star pickups, health and star HUD, 'SPACE fires prompts' tip and power bar. The game's own runtime output.

![Inspected 1920x1080 PNG: MAX token-stream sequence with '136 tokens' budget meter, scattered character projectiles, CUDA OOM text, Twin Peaks / GPU signage and 404 pit. The game's own runtime output.](https://raw.githubusercontent.com/travisstephenfraser/survive-coders/master/docs/screenshots/06-max-token-stream.png)

Inspected 1920x1080 PNG: MAX token-stream sequence with '136 tokens' budget meter, scattered character projectiles, CUDA OOM text, Twin Peaks / GPU signage and 404 pit. The game's own runtime output.

![Inspected 1688x780 PNG: phone landscape run with touch D-pad bottom-left, fire and jump buttons bottom-right, tappable ship-it/rollback/refactor bar plus talk slot, pause button and star badge. Confirms on-screen touch controls; the game's own runtime output.](https://raw.githubusercontent.com/travisstephenfraser/survive-coders/master/docs/screenshots/13-phone-level.png)

Inspected 1688x780 PNG: phone landscape run with touch D-pad bottom-left, fire and jump buttons bottom-right, tappable ship-it/rollback/refactor bar plus talk slot, pause button and star badge. Confirms on-screen touch controls; the game's own runtime output.

![Inspected 1920x1080 PNG: terminal-style title screen with SURVIVE CODERS masthead, pixel vibe coder and floating laptop key art, keyboard/voice control list and 'Press ENTER to start'. Menu/title card, discounted as non-gameplay.](https://raw.githubusercontent.com/travisstephenfraser/survive-coders/master/docs/screenshots/01-title.png)

Inspected 1920x1080 PNG: terminal-style title screen with SURVIVE CODERS masthead, pixel vibe coder and floating laptop key art, keyboard/voice control list and 'Press ENTER to start'. Menu/title card, discounted as non-gameplay.

## Play

- Open https://survive-coders.vercel.app/ and press Enter (or tap) on the title screen to start.
- Move with arrow keys or A/D; jump with Up, W, or Z (hold for higher jumps).
- Fire prompt bolts with Space, X, or J; after grabbing the MAX chip, hold fire to stream tokens from its budget.
- Fire voice powers by holding M, saying 'ship it', 'rollback', or 'refactor', and releasing; or press 1/2/3.
- On phones/tablets play in landscape: use the on-screen D-pad, fire and jump buttons, tap powers, or hold the talk slot.
- Cross the level to Anthropic HQ, ride the cable car over the 404 pit, then defeat the Context Rot Hydra (refactor when context reads OVERFLOW).

## Mechanics

- Side-scrolling platforming with coyote time, jump buffering, and camera lookahead
- Prompt-bolt projectile combat against three enemy types (splitting blobs, charging goblins, 6-HP H100 GPUs)
- Push-to-talk voice powers with keyboard/tap equivalents and cooldowns
- MAX token-stream power-up with a counted token budget
- Rideable cable car traversal over 404 pits and star-collectible arcs
- Three-headed boss with image-flood telegraphs, control-reversing orb, spawning skulls, context growth/overflow, and enraged last head
- Hit-stop, squash and stretch, boss checkpoint, pause/mute, portrait auto-pause

## Tags

- platformer
- pixel-art
- boss-battle
- voice-controlled
- touch-controls
- single-player
- browser
- hackathon

## Controls

- Mobile controls: Supported
- Motion controls: Not established
- Gamepad: Not established
- Keyboard/mouse: Supported

## Player modes

- Human players: 1
- Modes: single-player

## Technologies

- **Phaser ^3.90.0** — engine ([evidence](https://raw.githubusercontent.com/travisstephenfraser/survive-coders/master/package.json))
- **JavaScript** — language ([evidence](https://api.github.com/repos/travisstephenfraser/survive-coders))
- **Vite ^8.3.1** — build ([evidence](https://raw.githubusercontent.com/travisstephenfraser/survive-coders/master/package.json))
- **Arcade Physics** — physics ([evidence](https://raw.githubusercontent.com/travisstephenfraser/survive-coders/master/src/main.js))
- **WebGL** — rendering ([evidence](https://raw.githubusercontent.com/travisstephenfraser/survive-coders/master/src/main.js))
- **Web Audio** — audio ([evidence](https://raw.githubusercontent.com/travisstephenfraser/survive-coders/master/README.md))
- **Web Speech API** — framework ([evidence](https://raw.githubusercontent.com/travisstephenfraser/survive-coders/master/src/voice.js))

## Reconstructed prompt

Build a 16-bit Phaser 3 browser platformer: a vibe coder runs at night from Daly City to Anthropic HQ across one side-scrolling level with parallax SF landmarks, 3 enemy types, a rideable cable car over 404 pits, star collectibles, push-to-talk voice powers (ship it / rollback / refactor) with keyboard and touch fallbacks, a three-headed Context Rot Hydra boss with context-overflow mechanic, CRT scanlines, touch controls, and an original chiptune win song. Deploy static to Vercel.

## Source evidence

- Repository is a public browser game: 'Survive Coders: a vibe coder's 8-bit platformer run from Daly City to Anthropic HQ (hackathon demo)', language JavaScript, homepage https://survive-coders.vercel.app. ([source](https://api.github.com/repos/travisstephenfraser/survive-coders))
- README describes a playable platformer: robotaxi intro, one side-scrolling level from Daly City to Anthropic HQ, three enemy types (Bad Prompt Blob, Keyboard Goblin, H100 GPU), rideable cable car, and a three-headed Context Rot Hydra boss with distinct head roles. ([source](https://raw.githubusercontent.com/travisstephenfraser/survive-coders/master/README.md))
- Controls table documents keyboard (arrows/AD, Space/X/J fire, M push-to-talk, 1/2/3 powers, P/Esc pause, N mute) and touch (D-pad, fire/jump buttons, tappable powers, hold-to-talk). Touch UI appears on coarse-pointer devices; ?touch flag shows it on desktop where it works with a mouse. ([source](https://raw.githubusercontent.com/travisstephenfraser/survive-coders/master/README.md))
- Touch implementation confirmed in source: DOM buttons over the canvas (D-pad, fire, jump) ORed with keyboard in Player.tick; HUD tap targets for powers, mic and pause. ([source](https://raw.githubusercontent.com/travisstephenfraser/survive-coders/master/src/touch.js))
- Voice powers are push-to-talk (hold M or HUD talk slot, release to fire ship it / rollback / refactor); keys 1/2/3 and taps are fallbacks so voice is never required. ([source](https://raw.githubusercontent.com/travisstephenfraser/survive-coders/master/src/voice.js))
- Single-player structure only: scenes Boot, Title, Level1, BossHQ, HUD, Cine, End with one vibe-coder run; no multiplayer, backend, or network play documented. ([source](https://raw.githubusercontent.com/travisstephenfraser/survive-coders/master/src/main.js))
- Live deployment returns HTTP 200 and serves the game shell (Phaser canvas #game, Survive Coders title/meta, fullscreen touch CSS). ([source](https://survive-coders.vercel.app/))
- No gamepad or device-motion support documented; only keyboard and touch inputs are described. ([source](https://raw.githubusercontent.com/travisstephenfraser/survive-coders/master/README.md))
- Built with Claude Code (Claude Opus 5.5) as a pair programmer; commits carry Co-Authored-By trailers. ([source](https://raw.githubusercontent.com/travisstephenfraser/survive-coders/master/README.md))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 85/100: The cable-car hop over a glowing 404 pit and the refactor-or-rot Hydra finale had our demo-day table shouting commands at the screen. Short, sharp, and full of jokes that land.
- 62/100: A charming one-level run with a genuinely clever push-to-talk hook and a busy boss fight. Great feel for a weekend build, but I wanted a second level and more enemy variety.
- 47/100: Neat concept and readable pixel art, though the night palette gets muddy and voice recognition depends on your browser and room noise. The keyboard fallbacks save it.

## Links

- [Source repository](https://github.com/travisstephenfraser/survive-coders)
- [Play the game](https://survive-coders.vercel.app/)
