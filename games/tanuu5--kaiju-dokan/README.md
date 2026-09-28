# 怪獣ドカン！ KAIJU DOKAN!

[Play the game](https://tanuu5.github.io/kaiju-dokan/) · [View source](https://github.com/tanuu5/kaiju-dokan)

| Overall rating | Screenshot score |
| :---: | :---: |
| **54/100** | **68/100** |

<details>
<summary>Read the scoring rationale</summary>

### Overall rating

Excluding the target itself, closest comparators are Kart Royale (50 overall / 70 screenshots: complete polished 3D loop but single-track racer), OSRS Tower Defense (52/65: deep wave/tower systems with dense HUD), Ashlands (55/no scorable screenshots: broadest systems scope but no inspectable visuals), Turbo Kart Rally (40/70: polished 3D racer, thinner evidenced systems), and moorestech (64/76: far broader factory/sim scope with denser UI). Kaiju Dokan shows a complete verified playable loop (destruction physics, combos, energy/breath, AI waves, HP/regen, ranks, minimap, settings, headless balance sim) plus three coherent stylized 3D screenshots and three verified input schemes, placing it above the single-loop kart racers and near OSRS/Ashlands, but below moorestech on scope and proven depth. Capped well below AAA: single stage (stage 2 pending), no verified performance/balance data, and stills cannot prove feel, difficulty, or long-term variety.

### Screenshot score

Two inspected gameplay frames show coherent stylized sunset-city 3D with dense lit-window blocks, kaiju model with glowing plates, debris/dust/breath effects, manga impact typography, and a full destruction-focused HUD. Slightly above OSRS Tower Defense (65) and scumm-game (62) on 3D scene density and effects, just below Kart Royale/Turbo Kart Rally/Neural Sight (70) on crispness and composition (dark crushed night blocks, HUD-less breath shot). Stills cannot prove motion, performance, or balance; title card discounted.

</details>

## At a glance

| Detail | Value |
| --- | --- |
| Repository created | 26 Sep 2026 · 09:20 UTC |
| Added to catalog | 27 Sep 2026 · 06:24 UTC |
| Last updated | 27 Sep 2026 · 06:24 UTC |
| Documented creation models | [Claude Opus 5.5](https://github.com/tanuu5/kaiju-dokan) |

## Screenshots

![Inspected 1280x720 gameplay frame: third-person view of dark kaiju silhouette stomping through a dense sunset city of lit-window blocks, manga impact text and +1,470 score popup, full HUD (Dokagon HP/energy bars, 3:36 timer, 4% destruction vs 40% goal, score 17,753, 14 toppled buildings, 26 combo x3.5, minimap, WASD/gamepad control hints). Clearly the game's own runtime output; densest gameplay evidence.](https://raw.githubusercontent.com/tanuu5/kaiju-dokan/main/docs/images/gameplay.jpg)

Inspected 1280x720 gameplay frame: third-person view of dark kaiju silhouette stomping through a dense sunset city of lit-window blocks, manga impact text and +1,470 score popup, full HUD (Dokagon HP/energy bars, 3:36 timer, 4% destruction vs 40% goal, score 17,753, 14 toppled buildings, 26 combo x3.5, minimap, WASD/gamepad control hints). Clearly the game's own runtime output; densest gameplay evidence.

![Inspected 1280x720 gameplay close-up: kaiju firing a bright magma breath beam into city blocks with flying debris cubes, dust, glowing dorsal plates, sunset skyline and lit windows behind, score popups (+849/+1,440/+200). No HUD visible but clearly the game's own runtime output; shows breath attack and destruction effects.](https://raw.githubusercontent.com/tanuu5/kaiju-dokan/main/docs/images/breath.jpg)

Inspected 1280x720 gameplay close-up: kaiju firing a bright magma breath beam into city blocks with flying debris cubes, dust, glowing dorsal plates, sunset skyline and lit windows behind, score popups (+849/+1,440/+200). No HUD visible but clearly the game's own runtime output; shows breath attack and destruction effects.

![Inspected 1280x720 title card: KAIJU DOKAN! logo and Stage 1 bayside-city text over the same sunset procedural city, orange game-start button, mission text (40% destruction goal, defense-force warning) and control summary. Menu/title presentation of the game's own output, discounted as non-gameplay.](https://raw.githubusercontent.com/tanuu5/kaiju-dokan/main/docs/images/title.jpg)

Inspected 1280x720 title card: KAIJU DOKAN! logo and Stage 1 bayside-city text over the same sunset procedural city, orange game-start button, mission text (40% destruction goal, defense-force warning) and control summary. Menu/title presentation of the game's own output, discounted as non-gameplay.

## Play

- Open https://tanuu5.github.io/kaiju-dokan/ in a WebGL2 browser (landscape recommended on phones).
- Reach the destruction-rate goal within the 4-minute limit to clear the stage, then keep rampaging or press Enter / pause-menu finish to see results.
- Move with WASD and Shift to dash (left stick / LB on gamepad; left-side touch drag, push to edge to dash); camera with mouse, arrow keys, right stick, or right-side touch drag.
- Attack with punch (left click / J / X), tail spin (E / K / B), jump stomp (Space / A), hold magma breath when charged (right click / F / L / RT), and roar (Q / I / Y).
- Chain destruction to raise the combo multiplier up to x5, charge energy to fire breath (glowing dorsal plates signal full charge), and smash tanks and helicopters while watching HP.
- On touch devices use the lower-right punch/jump/tail/breath/roar buttons and the top-left pause button; adjust quality, shake, sensitivity, and volumes in settings if the game is heavy.

## Mechanics

- Block-by-block building destruction with support-connectivity falling and tall-building sideways toppling with chain collisions
- Timed destruction-rate goal stage with score, ranks, toppled-building count, and post-clear score attack
- Destruction combo multiplier up to x5
- Energy meter charged by destruction enabling magma breath, with full-charge dorsal-glow signal
- AI defense forces (tanks, attack helicopters) escalating over time, vulnerable to all attacks plus roar stagger
- HP with damage-regen delay and heal-on-topple, game over at 0 HP
- Punch 3-hit slam, tail spin, jump stomp, charged breath, roar that scatters cars
- HUD with HP/energy/cooldowns, timer, destruction bar with goal marker, score, combo, and minimap
- Procedural city/sky/sea/shader visuals with sunset lighting, bloom, and stencil kaiju silhouette; synthesized Web Audio SFX and BGM
- Quality/shake/sensitivity/invert/volume/FPS settings with low-quality default on mobile

## Tags

- kaiju
- city-destruction
- 3d
- threejs
- webgl
- browser-game
- procedural-generation
- action
- single-player
- stylized

## Controls

- Mobile controls: Supported
- Motion controls: Not established
- Gamepad: Supported
- Keyboard/mouse: Supported

## Player modes

- Human players: 1
- Modes: single-player

## Technologies

- **Three.js ^0.186.1** — engine ([evidence](https://api.github.com/repos/tanuu5/kaiju-dokan/contents/package.json?ref=main))
- **TypeScript ^7.0.2** — language ([evidence](https://api.github.com/repos/tanuu5/kaiju-dokan/contents/package.json?ref=main))
- **Vite ^8.3.1** — build ([evidence](https://raw.githubusercontent.com/tanuu5/kaiju-dokan/main/vite.config.ts))
- **Vitest ^4.1.11** — build ([evidence](https://api.github.com/repos/tanuu5/kaiju-dokan/contents/package.json?ref=main))
- **WebGL2** — rendering ([evidence](https://github.com/tanuu5/kaiju-dokan))
- **Web Audio API** — audio ([evidence](https://github.com/tanuu5/kaiju-dokan))

## Reconstructed prompt

Build KAIJU DOKAN, a 3D browser kaiju-destruction game in Three.js + TypeScript: play a giant monster smashing a procedural sunset bayside city with block-by-block building damage, support-collapse toppling with chain collisions, punch/tail/stomp/breath/roar attacks, combo multiplier, energy-charged magma breath, tanks and attack helicopters with HP/regen rules, 4-minute timed destruction-goal stage with score and ranks, minimap and full HUD, keyboard+mouse plus keyboard-only plus gamepad plus touch virtual-stick controls, quality/shake/sensitivity/volume settings, all graphics and Web Audio SFX/BGM generated in code, Vite+Vitest build with headless balance-simulation tests, deployable to GitHub Pages.

## Source evidence

- Repository is an actual game: description (via API) is a 3D browser game where you control a giant kaiju to smash a city, built with Three.js + TypeScript; public repo, language TypeScript, homepage set to the GitHub Pages build, has\_pages true. ([source](https://api.github.com/repos/tanuu5/kaiju-dokan))
- README identifies the game as controlling giant kaiju Dokagon to destroy a sunset bayside city, with all graphics, sound effects, and BGM generated in code and no external image/audio files. ([source](https://github.com/tanuu5/kaiju-dokan))
- README documents the win/lose loop: 4-minute limit, reach 40% destruction (live build shows 50% goal text) to clear the stage, keep rampaging for score after clearing, combo multiplier up to x5, energy charges magma breath, tanks and attack helicopters attack over time, HP reaches 0 for game over with regen rules. ([source](https://github.com/tanuu5/kaiju-dokan))
- README documents keyboard+mouse controls (WASD, mouse camera, clicks, Space, E, Q, F, etc.), keyboard-only alternatives, and full gamepad mapping including menu navigation; the live index.html confirms the same bindings plus HUD, minimap, pause, settings, and result screens. ([source](https://github.com/tanuu5/kaiju-dokan))
- README documents smartphone/tablet touch controls: left-side drag spawns a virtual stick (push to edge to dash), right-side drag for camera, lower-right buttons for punch/tail/jump/breath/roar, pause button; index.html contains the touch UI layer with the same buttons. ([source](https://github.com/tanuu5/kaiju-dokan))
- No source mentions accelerometer/gyroscope motion controls, so motion support is unknown rather than ruled out. ([source](https://github.com/tanuu5/kaiju-dokan))
- No multiplayer is documented; the game describes one player as the kaiju against AI defense forces (tanks, helicopters), so single-player with 1 human player. ([source](https://github.com/tanuu5/kaiju-dokan))
- Live URL opens the actual playable game (title screen, HUD with HP/energy/timer/destruction/score/combo/minimap, touch buttons, pause, settings, stage-clear result), not just a repo or promo page. ([source](https://tanuu5.github.io/kaiju-dokan/))
- README attributes development to AI coding tool Claude Code with model Claude Opus 5.5. ([source](https://github.com/tanuu5/kaiju-dokan))
- package.json declares three ^0.186.1 dependency with TypeScript ^7.0.2, vite ^8.3.1, vitest ^4.1.11 dev dependencies; vite.config.ts confirms a Vite build targeting es2022 with relative base for GitHub Pages. ([source](https://api.github.com/repos/tanuu5/kaiju-dokan/contents/package.json?ref=main))
- Languages endpoint is TypeScript-dominant with CSS and HTML, matching a TypeScript browser game with custom CSS UI. ([source](https://api.github.com/repos/tanuu5/kaiju-dokan/languages))
- README technical section documents InstancedMesh block-based buildings with CPU destruction/support/toppling simulation, procedural shader windows/roads/sky/sea, sunset lighting with bloom, stencil see-through kaiju silhouette, and Web Audio synthesized footsteps/explosions/roars/drum-and-bass BGM loop. ([source](https://github.com/tanuu5/kaiju-dokan))
- No existing catalog entry matches this repository or playable URL; grep over games/ and README.md found no kaiju-dokan or tanuu5 reference, so no slug is reused. ([source](https://github.com/tanuu5/kaiju-dokan))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 85/100: Fictional illustrative review: stomping a tower's foundation and watching it keel into the next block while the combo ticks up is pure joy, and the sunset city looks great for code-only art.
- 60/100: Fictional illustrative review: fun four-minute rampage with a lot of buttons to learn; I spent my first run fumbling breath charges while helicopters chipped my HP away.
- 100/100: Fictional illustrative review: procedural everything, touch stick plus gamepad plus keyboard, manga impact text over a burning skyline — the most complete giant-monster toy in this catalog.

## Links

- [Source repository](https://github.com/tanuu5/kaiju-dokan)
- [Play the game](https://tanuu5.github.io/kaiju-dokan/)
