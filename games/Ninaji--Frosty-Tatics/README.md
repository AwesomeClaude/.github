# Frosty Tactics — A Lamina Runica · The Runic Blade

[Open the game source](https://github.com/Ninaji/Frosty-Tatics)

**Overall rating:** 48/100. Closest comparators: neverquest (45 overall, deepest catalog systems scope but monochrome text UI only) and Kart Royale (50, ~60k-line 3D procedural tech demo with one 1.6km track) / Turbo Kart Rally (40, complete single-track 3D racer). Frosty Tactics exceeds neverquest on scope-plus-rendering (50-battle campaign plus endless mode, 115 enemies x 279 adjectives, D&D 5e rule layer, 13 actives + 10 passives, Three.js isometric scenes, procedural bosses, 10-track music engine, bilingual UI, sim-validated balance) and exceeds both kart racers and Taipo (35, single-map typing TD), Neural Sight (30, 4-scene shooter prototype), TypeScript-Blackjack (28, single-table card rules), Beachy Beachy Ball (25, single roll-to-star mechanic), and curiositY (18, static riddle pages) on gameplay depth and content volume. It ranks just below Kart Royale because visual polish, composition, and scene detail are unverified: the repo ships zero gameplay screenshots (only shields.io badges, discounted), the live canvas app exposes no static frames to inspect, and with 0 stars, 11 commits, and no playtest, playability, performance, and balance are unproven from source alone despite the sim harness.

**Screenshot score:** not scored. No inspectable gameplay screenshot.

## Play

- Open https://ninaji.github.io/Frosty-Tatics/ in a desktop browser (or run locally with npm install then npm run dev at http://localhost:5173).
- On first visit pick a language (Portuguese/English); force it later with ?lang=en or ?lang=pt.
- Click tiles to move Frosty on the isometric grid; click enemies to attack with the Everfrost blade.
- Press 1-9 to aim abilities (Winged Leap, Frost Strike, Action Surge, Avatar of Frost); press T to end turn, Q/E to rotate camera, mouse wheel to zoom, Esc to cancel targeting, H for help.
- Clear 5 zones x 10 battles (boss every 10th) plus final boss Vorthrax, then continue into Endless mode; collect victory gold, buy potions and 5 permanent upgrades, distribute attribute increases, and autosave persists in localStorage.
- Optional URL params: ?demo for spectator mode, ?auto to auto-advance battles/shop/attributes, ?speed=4 for animation speed, ?seed=123 for a fixed campaign.

## Mechanics

- Isometric turn-based grid tactics: click-to-move, weapon attacks, attacks of opportunity, elevated-terrain +2 hit bonus, hazards (lava, poison, thorns)
- D&D 5e-inspired d20 combat: d20 + bonus vs AC, advantage/disadvantage, natural-20 crits with doubled dice, saving throws, 12 damage types with resistance/immunity/vulnerability, 16 conditions
- 115 base enemies in 17 families x 279 mechanically-meaningful adjectives (32,085 single-adjective variants); enemy specials include smites, blasts, heals, buffs, debuffs, summons
- 50-battle campaign (5 zones x 10, boss every 10th) plus final boss Vorthrax plus scaling Endless mode with seeded encounter generation
- Hero progression levels 1-30+: 13 unlockable active abilities and 10 passives, attribute increases at 8 ASI levels, shop with potions and 5 permanent upgrades
- Enemy AI with behaviors (aggressive, shooter, coward, ambusher, guardian, lazy) plus multiattack, pack tactics, regen, lifesteal, thorns, auras, death explosions/splits
- Headless simulation and validation harness: full campaign sim across seeds with level/defeat/round-length assertions plus data-integrity checks, run in CI before Pages deploy
- Procedural Three.js presentation: isometric tile maps per zone palette, procedural Frosty/enemy/boss meshes, particle FX and damage numbers, event-driven battle renderer with demo/autoplay and speed control
- Bilingual PT-BR/EN localization of enemies, adjectives, abilities, and combat log with CI completeness check; bestiary tracking, localStorage autosave, procedural WebAudio SFX plus 10-track procedural soundtrack with jukebox

## Tags

- tactics
- turn-based
- tactical-rpg
- isometric
- 3d
- threejs
- dnd
- fantasy
- procedural-generation
- browser-game
- single-player
- bilingual

## Reconstructed prompt

Build Frosty Tactics (A Lamina Runica / The Runic Blade), a bilingual PT-BR/EN isometric 3D turn-based tactics browser game in Three.js + Vite in the spirit of Final Fantasy Tactics with D&D 5e rules: winged-tiefling heroine Frosty with runic bastard sword Everfrost; 50-battle campaign across 5 themed zones plus final boss Vorthrax plus endless mode; 115 data-driven enemies in 17 families x 279 mechanical adjectives; d20-vs-AC combat with advantage, crits, saves, 12 damage types, 16 conditions, opportunity attacks, high ground and hazards; 13 active + 10 passive abilities, ASI levels, shop with potions and 5 upgrades, bestiary, localStorage saves; fully procedural characters, tiles, FX, WebAudio SFX and 10-track soundtrack with jukebox; pure-rules core decoupled from Three.js so the whole campaign simulates headless in Node with validate + sim scripts enforced in CI before GitHub Pages deploy; support ?demo/?auto/?speed/?seed/?lang params.

## Source evidence

- Repo is Ninaji/Frosty-Tatics, described as 'Tatics game made with Fable 5'; README titles it Frosty Tactics, an isometric 3D turn-based tactics browser game in the spirit of Final Fantasy Tactics with D&D 5e rules, starring winged tiefling Frosty with runic sword Everfrost. ([source](https://github.com/Ninaji/Frosty-Tatics/blob/main/README.md))
- Campaign scope: 5 zones x 10 battles (boss every 10th) plus final boss Vorthrax the Void Dragon, then scaling Endless mode; zone table defines families, bosses, minions, palettes, and intro text per tier. ([source](https://github.com/Ninaji/Frosty-Tatics/blob/main/src/data/campaign.js))
- Content volume: 115 base enemies in 17 families x 279 adjectives with real mechanical effects (32,085 single-adjective variants); enemy file defines D&D stats, HP dice, AC, attacks, traits, specials, resistances, behaviors, and procedural visual descriptors. ([source](https://github.com/Ninaji/Frosty-Tatics/blob/main/src/data/enemies.js))
- Hero progression: 13 active abilities by level (Defensive Posture, Winged Leap, Frost Strike, Action Surge, Avatar of Frost) plus 10 level-gated passives, ASI levels, and abilitiesForLevel/passivesForLevel selectors. ([source](https://github.com/Ninaji/Frosty-Tatics/blob/main/src/data/abilities.js))
- Architecture decouples pure D&D rules core from Three.js: core/ has dice/combat/conditions, game/ has battle engine/AI/encounters/campaign/save, render/ has isometric scene/tiles/procedural characters/bosses/FX/event player, plus ui/, audio/, and sim/ validation. ([source](https://github.com/Ninaji/Frosty-Tatics/blob/main/README.md))
- Entry point wires SceneManager, TileMap, FX, BattleRenderer, procedural Frosty/enemy meshes, Sfx/MusicEngine with 10 data-driven loopable tracks, HUD/screens, save/load, autoplay/demo modes, tile-only FFT-style picking, and camera/zoom controls. ([source](https://github.com/Ninaji/Frosty-Tatics/blob/main/src/main.js))
- Validation story: npm run validate checks data integrity (\>=100 enemies, \>=200 adjectives); sim/run-sim.js simulates the full campaign headless across seeds with level-18-34 and battle-length assertions; CI validates, sims, builds, and deploys to GitHub Pages on every main push. ([source](https://github.com/Ninaji/Frosty-Tatics/blob/main/README.md))
- Commit history shows 11 commits with detailed boss meshes, procedural soundtrack/jukebox, full PT-BR/EN i18n with language picker, and Pages deploy; repo file tree lists only src/, sim/, index.html, package.json, vite.config.js (Three.js + Vite) with no docs/, screenshots/, or image assets. ([source](https://github.com/Ninaji/Frosty-Tatics/commits/main))
- No inspectable gameplay screenshots exist: README carries only shields.io badges, image-path probes (docs/, screenshots/, public/, assets/) all return 404, and the live Pages build is a canvas app returning no static frame; screenshots therefore unscored. ([source](https://github.com/Ninaji/Frosty-Tatics/blob/main/README.md))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 85/100: \[Fictional review\] Fifty battles in and my winged tiefling just unlocked Avatar da Geada — freezing a whole pack of Burning Goblins at once felt like the FFT payoff I have wanted in a browser tab for years.
- 62/100: \[Fictional review\] Made-up tactics fan note: the D&D math, opportunity attacks, and adjective combos are genuinely deep, but with no screenshots to preview the arenas I went in blind, and the procedural figures look plain next to the kart racers' sunset tracks.
- 100/100: \[Fictional review\] Invented systems-nerd take: a headless sim that validates all 50 battles across seeds, 32,085 enemy variants, full PT/EN localization, and a 10-track procedural jukebox? As an engineering artifact this is the most ambitious catalog entry yet.

## Links

- [Source repository](https://github.com/Ninaji/Frosty-Tatics)
- [Related link](https://ninaji.github.io/Frosty-Tatics/)
- [Related link](https://github.com/Ninaji/Frosty-Tatics/blob/main/README.md)
