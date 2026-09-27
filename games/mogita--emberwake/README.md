# Emberwake

[Play the game](https://emberwake.mogita.rocks) · [View source](https://github.com/mogita/emberwake)

| Overall rating | Screenshot score |
| :---: | :---: |
| **53/100** | **70/100** |

<details>
<summary>Read the scoring rationale</summary>

### Overall rating

A complete, playable single-mode survivors-like with verified deployment, polished HD-2D lighting/bloom screenshots, 12-upgrade draft depth, boss, surges, braziers and synthesized audio. Excluding itself, it outranks Kart Royale (50, polished but single-track racer), HEX DANMAKU (48, flat turn-based board) and Dead Signal (47, unverified visuals, no playable URL) on verified gameplay depth plus presentation, but sits below Ashlands (55, far broader open RPG systems) and moorestech (64, massive factory sim with co-op and mods) because the scope is one 5-minute solo loop with no multiplayer, editor or campaign. Far below AAA on content, cinematics and live-ops scale; source and screenshots do not prove performance or balance.

### Screenshot score

Best frame is the game's own HD-2D runtime output with coherent pixel art, dynamic lantern/brazier lighting, bloom and dense particle projectiles, detailed trees/enemies and a complete HUD. Matches catalog 70s Kart Royale, Turbo Kart Rally and Neural Sight on polished in-engine composition with lighting and UI density, and exceeds THORNMERE and HEX DANMAKU (60) and Taipo (55) on lighting depth and effects density, but sits below moorestech (76) which shows broader multi-scene 3D variety and denser construction UI. Title card discounted as non-gameplay; stills prove nothing about motion, performance or balance.

</details>

## At a glance

| Detail | Value |
| --- | --- |
| Repository created | 25 Sep 2026 · 18:57 UTC |
| Added to catalog | 27 Sep 2026 · 06:09 UTC |
| Last updated | 27 Sep 2026 · 06:09 UTC |
| Documented creation models | Not established |

## Screenshots

![Inspected downloaded copy: active late-night combat at LV 21 with 100/100 HP bar, 9-ability kit row, 0:16 UNTIL DAWN night bar, score 89,807, 38 CHAIN X2 meter, golden projectile swarms, damage numbers 30 and +30, moth enemies, trees and cobblestone path, XP bar and DASH indicator. The game's own runtime output; densest gameplay evidence, put first.](https://raw.githubusercontent.com/mogita/emberwake/main/docs/gameplay.jpg)

Inspected downloaded copy: active late-night combat at LV 21 with 100/100 HP bar, 9-ability kit row, 0:16 UNTIL DAWN night bar, score 89,807, 38 CHAIN X2 meter, golden projectile swarms, damage numbers 30 and +30, moth enemies, trees and cobblestone path, XP bar and DASH indicator. The game's own runtime output; densest gameplay evidence, put first.

![Inspected downloaded copy: THE FLAME GROWS blessing draft at LV 15 with three cards (Bright Lantern NEW, Lodestone, Quick Wick) with star ranks and descriptions, 1 2 3 or click hint, over dimmed live combat background with LV/HP/night/score/chain HUD. The game's own runtime output; menu-over-gameplay overlay, put second.](https://raw.githubusercontent.com/mogita/emberwake/main/docs/levelup.jpg)

Inspected downloaded copy: THE FLAME GROWS blessing draft at LV 15 with three cards (Bright Lantern NEW, Lodestone, Quick Wick) with star ranks and descriptions, 1 2 3 or click hint, over dimmed live combat background with LV/HP/night/score/chain HUD. The game's own runtime output; menu-over-gameplay overlay, put second.

![Inspected downloaded copy: EMBERWAKE pixel title logo with lantern icon over dark cobblestone courtyard at night, lit brazier with radius ring right, ember pickups, BEST 106,598 counter, WASD/SPACE control hints. Title/menu card over game scene, not active combat; discounted for graphics scoring, put last.](https://raw.githubusercontent.com/mogita/emberwake/main/docs/title.jpg)

Inspected downloaded copy: EMBERWAKE pixel title logo with lantern icon over dark cobblestone courtyard at night, lit brazier with radius ring right, ember pickups, BEST 106,598 counter, WASD/SPACE control hints. Title/menu card over game scene, not active combat; discounted for graphics scoring, put last.

## Play

- Open https://emberwake.mogita.rocks in a browser and press any key on the title screen to begin the night.
- Move with WASD or arrow keys and dash with Space; gamepad sticks and buttons also work.
- Your lantern fires on its own — steer into ember drops to gain XP, then pick 1 of 3 blessings with 1/2/3 or click.
- Stand beside unlit braziers to light them; their fire burns the dark.
- Survive the full 5 minutes until dawn; the Moonmoth Matriarch arrives at 3:30. Press Esc to pause, M to mute, R to retry after a run.

## Mechanics

- Top-down auto-combat survival run on a 5-minute night timer with dawn win condition
- Ember pickups, XP levels and 1-of-3 blessing drafts from 12 stackable upgrades
- Lightable braziers whose fire damages nearby darkness
- Dash with cooldown plus move-speed and cooldown upgrades
- Timed surge waves and Moonmoth Matriarch boss at 3:30 with boss HP bar
- Score, kill chain/combo multiplier and persistent local best score
- Full run state: HP, level kit, night progress clock, XP bar, end-of-run stats

## Tags

- roguelike
- survival
- vampire-survivors-like
- pixel-art
- hd-2d
- boss
- single-player
- browser
- threejs

## Controls

- Mobile controls: Not established
- Motion controls: Not established
- Gamepad: Supported
- Keyboard/mouse: Supported

## Player modes

- Human players: 1
- Modes: single-player

## Technologies

- **Three.js ^0.186.0** — engine ([evidence](https://github.com/mogita/emberwake/blob/main/package.json))
- **Three.js ^0.186.0** — rendering ([evidence](https://github.com/mogita/emberwake/blob/main/src/render.js))
- **JavaScript** — language ([evidence](https://github.com/mogita/emberwake/blob/main/src/main.js))
- **Vite ^8.3.0** — build ([evidence](https://github.com/mogita/emberwake/blob/main/package.json))
- **WebAudio** — audio ([evidence](https://github.com/mogita/emberwake/blob/main/src/audio.js))

## Reconstructed prompt

Build a browser pixel-art HD-2D vampire-survivors roguelike called Emberwake with Three.js and Vite: auto-attacking lantern, WASD/arrows movement, Space dash and gamepad support, ember pickups with XP levels and 1-of-3 blessing drafts from 12 stackable upgrades, lightable braziers, a 5-minute night timer with surge waves and a Moonmoth Matriarch boss at 3:30, score/chain combo with persistent best, title/level-up/pause/end screens, bloom-lit night rendering, fully synthesized WebAudio music and SFX, and a deployable static build.

## Source evidence

- Repository page titles the project 'Emberwake' with tagline 'Keep the flame alive until dawn. A pixel-art HD-2D survival game for the browser.' and links Play to https://emberwake.mogita.rocks ([source](https://github.com/mogita/emberwake))
- README documents a roguelike survival loop: auto-fighting lantern, collect embers, level up, pick 1 of 3 blessings, light braziers, survive five minutes until dawn, Moonmoth Matriarch boss arrives at 3:30 ([source](https://github.com/mogita/emberwake/blob/main/README.md))
- README controls establish keyboard support: WASD or arrows to move, Space to dash; level-up overlay supports 1/2/3 or click ([source](https://github.com/mogita/emberwake/blob/main/README.md))
- README explicitly states 'Gamepad works too', establishing gamepad support ([source](https://github.com/mogita/emberwake/blob/main/README.md))
- src/main.js implements keyboard (KeyWASD/arrows, Space/Shift dash, Escape/KeyP pause, KeyM mute, KeyR restart, Digit1-3 selection), pointer/click selection, and gamepad via navigator.getGamepads axes and buttons; no touch joystick or motion controls found ([source](https://github.com/mogita/emberwake/blob/main/src/main.js))
- index.html HUD and screens show single-player survival UI: LV, HP, night countdown to dawn, score, chain combo, kit, XP bar, dash meter, boss bar for MOONMOTH MATRIARCH, title/level-up/pause/end screens with no multiplayer lobby or second-player input ([source](https://github.com/mogita/emberwake/blob/main/index.html))
- Game constants define a 300-second night, boss at 210s, surge waves, and 12 upgrades with levels and stat functions (Ember Bolt, Twin Flame, Cinder Halo, Scatter Sparks, Swift Boots, Hearthstone, Lodestone, Bright Lantern, Storm Chain, Sunburst, Moon Ward, Quick Wick) ([source](https://github.com/mogita/emberwake/blob/main/src/data.js))
- Live play URL opens the actual playable game (title screen with PRESS ANY KEY, WASD/SPACE instructions, HUD with LV/HP/night bar/score), not just a repo or promo page ([source](https://emberwake.mogita.rocks))
- package.json declares three ^0.186.0 and vite ^8.3.0 dependencies with dev/build/preview scripts ([source](https://github.com/mogita/emberwake/blob/main/package.json))
- README states 'Built with Three.js and WebAudio. All art was generated with the Codex CLI and snapped to a pixel grid with tools/pixelize.py. All music and sound effects are synthesized in code.' ([source](https://github.com/mogita/emberwake/blob/main/README.md))
- src/render.js imports three, EffectComposer, RenderPass, UnrealBloomPass, ShaderPass and OutputPass, establishing Three.js post-processed rendering ([source](https://github.com/mogita/emberwake/blob/main/src/render.js))
- src/audio.js header states 'Fully synthesized score and SFX: no audio files to load', establishing code-synthesized WebAudio ([source](https://github.com/mogita/emberwake/blob/main/src/audio.js))
- About field says 'roguelike zero-shot by opus 5.5, claude called codex for assets creation' — informal attribution only; no exact documented creation-model name with version in project files, so creation\_models left unknown. gh api could not be used: no GH\_TOKEN in environment and unauthenticated api.github.com was rate-limited; evidence gathered via page/raw fetches instead ([source](https://github.com/mogita/emberwake))
- No catalog match: local catalog of 35 games contains no mogita/emberwake entry; closest systems comparators are HEX DANMAKU, Dead Signal: Exclusion Zone, neverquest and The Nine Lives of Ash, all different repositories and games ([source](https://github.com/mogita/emberwake))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 88/100: The lantern-build fantasy clicks — I stacked Storm Chain and Cinder Halo, lit two braziers and kited the Matriarch under a golden bullet storm with 16 seconds to dawn. The bloom-lit pixel ruins look gorgeous in motion.
- 64/100: Tight five-minute loop with meaningful drafts and a real boss gate, but one map and one timer means runs blur together. I want more arenas or daily seeds before it joins my nightly rotation.
- 100/100: A zero-shot survivors-like that actually ships: dash feels great, blessings snowball beautifully, the synthesized score swells at nightfall, and dawn breaks feel earned. Best small-scope loop I have played in this catalog.

## Links

- [Source repository](https://github.com/mogita/emberwake)
- [Play the game](https://emberwake.mogita.rocks)
