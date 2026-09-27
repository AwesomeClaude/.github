# moorestech

[View source](https://github.com/moorestech/moorestech)

| Overall rating | Screenshot score |
| :---: | :---: |
| **64/100** | **76/100** |

<details>
<summary>Read the scoring rationale</summary>

### Overall rating

Catalog comparison: most relevant comparators are Ashlands (55, current top), Wilderness (44, blocky exploration crafter), Kart Royale (50) and Neural Sight (30/70 screenshots, polished 3D but narrower scope). moorestech shows broader systems (gear power, belts, tech eras, story, tutorial, co-op server, mod tools), 15,000+ commits, and more polished stylized 3D than any catalog game, placing it above Ashlands. Capped well below AAA because the game is unreleased, with no playable build to verify performance, balance, or netcode, and evidence gaps on audio and gamepad/touch support.

### Screenshot score

Visible gameplay frames show coherent anime-stylized 3D with dense grass, soft shadows, detailed machines, and full HUDs, exceeding catalog mid-tier gameplay shots such as OSRS Tower Defense (65) and matching or passing the sharpest kart-racer frames (Kart Royale/Turbo Kart Rally 70) on scene detail, though still frames cannot prove motion, performance, or balance.

</details>

## At a glance

| Detail | Value |
| --- | --- |
| Repository created | 31 Mar 2021 · 04:00 UTC |
| Added to catalog | 27 Sep 2026 · 04:44 UTC |
| Last updated | 27 Sep 2026 · 04:44 UTC |
| Documented creation models | Not established |

## Screenshots

![Inspected: top-down 3D factory yard with conveyors carrying ore, brick furnaces with fire, pipes, anime protagonist in pink/white outfit, and 9-slot hotbar with item counts. Densest gameplay UI and clearest factory-building evidence; game's own runtime output.](https://moores.tech/assets/game-screenshot-1-DJ3aSHbO.webp)

Inspected: top-down 3D factory yard with conveyors carrying ore, brick furnaces with fire, pipes, anime protagonist in pink/white outfit, and 9-slot hotbar with item counts. Densest gameplay UI and clearest factory-building evidence; game's own runtime output.

![Inspected: desert factory with Metal Processing Equipment panel, inventory grid with gears/ingots counts, conveyors with metal rolls, character from behind, bottom hotbar. Full machine/inventory UI; game's own runtime output.](https://moores.tech/assets/game-screenshot-2-Bdgb5b21.webp)

Inspected: desert factory with Metal Processing Equipment panel, inventory grid with gears/ingots counts, conveyors with metal rolls, character from behind, bottom hotbar. Full machine/inventory UI; game's own runtime output.

![Inspected: grassy meadow with translucent building placement ghost, anime character placing a structure, waterfall/rocks/trees behind, bottom hotbar. Shows build-preview gameplay state; game's own runtime output.](https://moores.tech/assets/game-feature-tutorial-BuGQjo7s.webp)

Inspected: grassy meadow with translucent building placement ghost, anime character placing a structure, waterfall/rocks/trees behind, bottom hotbar. Shows build-preview gameplay state; game's own runtime output.

![Inspected: anime character running across a vast green open world with cliffs, forests, lake, and mountains, hotbar visible at bottom. Shows exploration scale; game's own runtime output.](https://moores.tech/assets/game-feature-openworld-DViLb0zE.webp)

Inspected: anime character running across a vast green open world with cliffs, forests, lake, and mountains, hotbar visible at bottom. Shows exploration scale; game's own runtime output.

## Play

- Move with W/A/S/D and jump with Space.
- Hold Left Click to mine and collect resources.
- Press B to open the build menu and Tab for inventory.
- Place with Left Click, rotate with R, demolish with G, undo with Ctrl+Z.
- Follow the Current Challenges panel for the next objective.
- Expand gear power, conveyors, and machines from waterwheels toward electricity and fusion, and ultimately build a rocket.

## Mechanics

- Gear and shaft power network with rotation speed and torque
- Conveyor-belt production lines with slopes and junctions
- Block placement, rotation, demolition, and undo with build costs
- Mining, smelting, processing, and assembly automation
- Technology progression from waterwheel to steam, electricity, and fusion
- Inventory, hotbar, and machine recipe interfaces
- Story campaign with anime companions and tutorial challenges
- Online co-op multiplayer via dedicated server
- Mod support with open-source code and editor tools

## Tags

- factory-automation
- simulation
- open-world
- anime
- rpg
- story
- crafting
- building
- 3d
- online-co-op
- moddable

## Controls

- Mobile controls: Not established
- Motion controls: Not established
- Gamepad: Not established
- Keyboard/mouse: Supported

## Player modes

- Human players: Not established
- Modes: single-player, online multiplayer

## Technologies

- **Unity 6000.3.8f1** — engine ([evidence](https://raw.githubusercontent.com/moorestech/moorestech/master/moorestech_client/ProjectSettings/ProjectVersion.txt))
- **C#** — language ([evidence](https://api.github.com/repos/moorestech/moorestech/languages))
- **Universal Render Pipeline 17.3.0** — rendering ([evidence](https://github.com/moorestech/moorestech/blob/master/moorestech_client/Packages/manifest.json))
- **Unity Input System 1.18.0** — framework ([evidence](https://github.com/moorestech/moorestech/blob/master/moorestech_client/Packages/manifest.json))

## Reconstructed prompt

Create an anime-style 3D open-world factory automation game in Unity: third-person character, gear/torque power networks, conveyor production lines, mining/smelting/assembly machines, inventory and 9-slot hotbar building, tech progression from waterwheels to fusion, story campaign about an exiled princess, tutorial challenge guidance, single-player plus online co-op via a dedicated server, and mod support with open-source code.

## Source evidence

- Repository is an actual game: description 'Animated open world automated factory game' with C# primary language and topics including game, game-development, unity, unity3d-game, realtime-server. ([source](https://github.com/moorestech/moorestech))
- Repo metadata via API: C# dominant language, topics csharp/dotnet/unity, 83 stars, default branch master, no homepage; releases dev-v1.0.0 through dev-v1.2.0 exist with no downloadable game builds. ([source](https://api.github.com/repos/moorestech/moorestech))
- README states this is the Unity server and client of factory game moorestech and instructs opening moorestech\_client in Unity and playing the MainGame scene. ([source](https://raw.githubusercontent.com/moorestech/moorestech/master/README.md))
- CONTEXT.md defines the game as a factory-building sandbox where the player places blocks, mines resources, and assembles production lines, with hotbar slots 1-9, build costs, belts, and power wiring. ([source](https://raw.githubusercontent.com/moorestech/moorestech/master/CONTEXT.md))
- Steam page lists Features as Single-player and Online Co-op, release 'To be announced' / 'not yet available', system requirements Windows/macOS/Linux, and full source code on GitHub with planned Workshop mod support. ([source](https://store.steampowered.com/app/1958160/moorestech/))
- Official site describes gear-driven factory construction, anime open world, tech progression from waterwheel to fusion, story of exiled princess Yori, tutorial, and Summer 2026 Steam release target. ([source](https://moores.tech/home.html))
- Gamescom play guide lists keyboard+mouse controls: WASD move, Space jump, hold Left Click mine/collect, Tab inventory, B build menu, Left Click place, R rotate, G demolish, Ctrl+Z undo, plus a Current Challenges objective panel. ([source](https://raw.githubusercontent.com/moorestech/moorestech/master/docs/gamescom/a4-play-guide-en.html))
- Unity editor version pinned at 6000.3.8f1 in client ProjectSettings. ([source](https://raw.githubusercontent.com/moorestech/moorestech/master/moorestech_client/ProjectSettings/ProjectVersion.txt))
- Client package manifest includes Universal Render Pipeline 17.3.0 and Input System 1.18.0 among Unity dependencies. ([source](https://github.com/moorestech/moorestech/blob/master/moorestech_client/Packages/manifest.json))
- No public playable browser build found: Steam is an unreleased store listing, the repository requires opening the Unity project locally, and moorestech\_web is an in-game WebUI frontend, not a hosted playable game. ([source](https://raw.githubusercontent.com/moorestech/moorestech/master/moorestech_web/README.md))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 85/100: A factory sim with real personality: routing belts around a meadow while my little princess engineer supervises just feels good. The gear-power idea makes every upgrade tangible.
- 62/100: Ambitious and charming, but clearly still in development. The building and automation loop reads well; I want to see how the late-game tech tree and co-op hold up.
- 100/100: Waterwheels to fusion with anime storybook heart. The day my first fully automated line lit up, I knew this was something special.

## Links

- [Source repository](https://github.com/moorestech/moorestech)
- [Steam store page](https://store.steampowered.com/app/1958160/moorestech/)
- [Official site](https://moores.tech/home.html)
