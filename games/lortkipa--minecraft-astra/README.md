# Wilderness

[View source](https://github.com/lortkipa/minecraft-astra)

| Overall rating | Screenshot score |
| :---: | :---: |
| **44/100** | **Not scored** |

<details>
<summary>Read the scoring rationale</summary>

### Overall rating

AAA proximity judged from source via web API plus README because the game could not be played: no inspectable gameplay screenshots exist and the listed preview returned 404. Closest comparators are Kart Royale (50, ~60k-line 3D kart tech demo with proven polished screenshots and full race loop), neverquest (45, deepest catalog systems scope but text-only), and Turbo Kart Rally (40, complete single-track 3D racer with menus, AI, and items). Wilderness sits between Turbo Kart Rally and Kart Royale at 44: its scope exceeds Turbo Kart (open 192x192 voxel survival world with mining, 8-recipe crafting, hunger, XP, animals, night enemies, quests, map, and persistence versus one circuit) and matches Kart Royale on technical ambition (chunked voxels, raycasts, AO, shadows, water shader, viewmodel), but trails Kart Royale on proven polish (no gameplay frames to inspect, dead demo, 2 same-day commits from a single prompt with no balancing, QA, multiplayer, or live-ops evidence) and trails neverquest on long-tail progression depth and multi-year iteration. Clearly above Taipo (35, single-map 2D typing TD), TypeScript-Blackjack (28, flat single-table card game), Beachy Beachy Ball (25, minimal ball roller), and curiositY (18, static riddle pages) on 3D engine complexity and survival-loop breadth. Evidence gaps: source and docs alone do not prove playability, frame rate, balance, or late-game depth.

### Screenshot score

No inspectable gameplay screenshot.

</details>

## At a glance

| Detail | Value |
| --- | --- |
| Documented creation models | Not established |

## Play

- Install and run locally with \`npm install\` then \`npm run dev\`, and open the URL shown in the terminal (the listed Netlify preview returned 404 when checked).
- Click Enter the wilderness to capture the mouse and start, then move with W/A/S/D, look with the mouse, jump or swim up with Space, and sprint with Shift.
- Hold left click to mine blocks and attack animals or night creatures; right-click to place the selected block or eat food.
- Press 1-9 or use the mouse wheel to select one of the 9 hotbar slots.
- Press E, C, or Tab to open inventory and crafting: turn logs into planks and sticks, build a crafting table, place it nearby to unlock stone tools, torches, and the stone sword.
- Press F to eat apples or meat when hunger drops; gather apples from oak leaves and meat from passive animals.
- Press M for the world map, H for the field guide, and Esc to pause; follow the First Chapter quest chain (wood, crafting, shelter, exploration).
- Survive the day-night cycle (a full day lasts about 15 minutes), build shelter and torches before night creatures spawn, and manage health and hunger to avoid the death screen.

## Mechanics

- First-person voxel survival in a 192x192x72 procedurally generated world with hills, river, trees, water, and day-night cycle
- Amanatides-Woo voxel raycast mining and block placement with tool-gated durations and mining progress ring
- Block, tool, material, and food item system with 9-slot hotbar, 24-slot backpack, and equip reassignment
- 8-recipe crafting chain (planks, sticks, table, wooden and stone pickaxes, axe, sword, torches) with nearby-table gating
- Health, hunger, XP levels, fall damage, drowning and void checks, and hunger-gated sprint and regeneration
- Passive animals (sheep and pigs) that wander, panic when hit, and drop meat; hostile night creatures that spawn after dark and despawn at dawn
- Melee combat with range and facing checks, tool-based damage, knockback-style panic, and block or coal drops
- Full HUD: quest chain tracker, compass, minimap plus full 192x192 map, clock and day counter, vitals icons, coordinates, XP bar, toasts, and damage vignette
- Modal loop: inventory and crafting, field guide, settings (sensitivity, FOV, quality, shadows, volume), pause, large map, death and respawn, and seeded new-world creation
- Browser persistence via localStorage saves with autosave, plus synthesized Web Audio effects and procedural Three.js visuals (chunk meshing, AO, shadows, water shader, clouds, grass, torches)

## Tags

- voxel
- survival
- sandbox
- crafting
- exploration
- 3d
- threejs
- browser-game
- procedural-generation
- single-player

## Reconstructed prompt

Vibe-code Wilderness, a Minecraft-style voxel survival browser game with Three.js and Vite in a single pass: a 192x192 procedurally generated voxel world with terrain, river, trees, water shader, clouds, grass, and day-night cycle; first-person mine and place with raycasts, tools, and craftingtable-gated recipes; health, hunger, XP, passive animals and night enemies; quest tracker, compass, minimap, inventory, field guide, settings, pause, map, death, and seeded-new-world modals with localStorage saves and synthesized audio.

## Source evidence

- Game title is Wilderness, described as a Minecraft-style browser game vibe-coded with a single prompt using GPT-6 Astra. ([source](https://github.com/lortkipa/minecraft-astra/blob/main/README.md))
- Listed preview https://endearing-taffy-1374d7.netlify.app/ returned 404 when fetched, so no playable build could be verified. ([source](https://endearing-taffy-1374d7.netlify.app/))
- Repo is public JavaScript (47418 bytes JS, 583 bytes HTML), 0 stars, 0 forks, default branch main, created and last pushed 2026-09-05 with only 2 commits (first commit, readme update). ([source](https://api.github.com/repos/lortkipa/minecraft-astra))
- File tree has no screenshots or docs images: only README, index.html, package files, public/favicon.svg, and 6 source files (core.js, game.js, main.js, style.css, ui.js, world.js). ([source](https://api.github.com/repos/lortkipa/minecraft-astra/git/trees/main?recursive=1))
- Stack is Three.js 0.180 plus lucide icons with Vite 7, with scripts for dev, build, preview, and node tests, though no tests directory is present in the tree. ([source](https://github.com/lortkipa/minecraft-astra/blob/main/package.json))
- Voxel engine defines 12 block types plus stick, tools, and food items, 8 crafting recipes, and procedural terrain with value noise, peaks, river carving, coal veins, caves, and tree placement. ([source](https://github.com/lortkipa/minecraft-astra/blob/main/src/core.js))
- World renderer builds 16x16 chunks with face culling, canvas texture atlas, per-vertex AO and shading, torch point lights, instanced grass, flowers, shader water, blocky clouds, and stars. ([source](https://github.com/lortkipa/minecraft-astra/blob/main/src/world.js))
- Game loop implements pointer-lock FPS movement with sprint, swim, and step-up, Amanatides-Woo raycast targeting with outline, tool-gated mining, placement collision checks, melee mob combat, 19 passive animals plus 7 night spawns, particles, day-night sky, HUD ticks, autosave, and settings. ([source](https://github.com/lortkipa/minecraft-astra/blob/main/src/game.js))
- UI shell provides quest chain, compass, minimap and large map, vitals, hotbar, toasts, and modals for inventory and crafting, guide, settings, pause, map, death, and seeded new worlds. ([source](https://github.com/lortkipa/minecraft-astra/blob/main/src/ui.js))
- README controls table documents WASD move, mouse look, Space jump/swim, Shift sprint, hold-click mine, click attack, right-click place/eat, 1-9 and wheel hotbar, E/C/Tab inventory, F eat, M map, H guide, Esc pause. ([source](https://github.com/lortkipa/minecraft-astra/blob/main/README.md))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 75/100: \[Fictional review\] Imagined survival fan: I punched trees until I could build a plank shelter, strung torches around it, and barely survived the first night ambush. For a browser voxel toy the day-night mood and map are great; I just wish the preview link still worked so I could show a friend.
- 55/100: \[Fictional review\] Made-up casual player note: lots of Minecraft-shaped systems — mining, crafting tables, hunger, hotbar — but with zero screenshots and a dead demo I had to take the code on faith. Fun on paper, unproven in the hand.
- 100/100: \[Fictional review\] Invented engine-nerd take: a 192x192 chunked voxel world with Amanatides-Woo raycasts, per-face AO, water shaders, and a full HUD from a single prompt? As a vibe-coded technical sketch this is absurdly ambitious, even if it is nowhere near AAA.

## Links

- [Source repository](https://github.com/lortkipa/minecraft-astra)
- [Related link](https://github.com/lortkipa/minecraft-astra/blob/main/README.md)
- [Related link](https://github.com/lortkipa/minecraft-astra/blob/main/package.json)
- [Related link](https://github.com/lortkipa/minecraft-astra/blob/main/src/core.js)
- [Related link](https://github.com/lortkipa/minecraft-astra/blob/main/src/world.js)
- [Related link](https://github.com/lortkipa/minecraft-astra/blob/main/src/game.js)
- [Related link](https://github.com/lortkipa/minecraft-astra/blob/main/src/ui.js)
- [Related link](https://endearing-taffy-1374d7.netlify.app/)
