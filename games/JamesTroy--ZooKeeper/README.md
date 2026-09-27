# Zoo Keeper

[Open the game source](https://github.com/JamesTroy/ZooKeeper)
**Repository created:** 2026-02-16T10:43:38Z
**Added to catalog:** 2026-09-27T04:44:37.584145+00:00
**Updated in catalog:** 2026-09-27T04:44:37.584145+00:00

**Overall rating:** 42/100. Closest comparators: Ashlands (55, catalog top on broad unverified 3D-engine scope with no inspectable screenshots), THORNMERE (46, real inspected combat screenshots at 60) and neverquest (45, deepest prior systems scope with a playable build), Wilderness (44, fellow ambitious 3D world project) and SpaceHo2 (42). ZooKeeper's documented paper scope is among the broadest in the catalog (behavior-tree animal AI with needs and breeding, enclosures, economy, visitors, staff, research, weather, time, rating, milestones, random events, save/load, full UMG suite, ~465KB of C++ across ~150 files). But like Ashlands it offers zero inspectable screenshots and no playable artifact (no Pages site, no releases, no homepage; a native UE 5.7 C++ build is required), its 12 commits all landed in a single day at version 0.1.0, and the runtime level is assembled from tinted engine basic-shape meshes, so visual polish and technical execution are unverifiable. It therefore sits below Ashlands (55), which claims a custom engine plus verification harness, and below screenshot-backed games such as THORNMERE and neverquest, roughly alongside SpaceHo2/Wilderness-tier ambitious-but-unverifiable 3D projects. Source and commit messages alone do not prove playability, performance, or balance.

**Screenshot score:** not scored. No inspectable gameplay screenshot.

## Play

- No public playable build exists, so the game cannot be played in a browser; playing requires building from source.
- Clone https://github.com/JamesTroy/ZooKeeper and open ZooKeeper.uproject with Unreal Engine 5.7 (the EngineAssociation in the project file).
- Build the ZooKeeper game module and press Play: you spawn as a first-person zoo keeper in a procedurally assembled zoo map.
- Move with W/A/S/D, look with the mouse, jump with Space, sprint with Left Shift, interact with E, and toggle build mode with B.
- Scroll or press number keys 1-5 to cycle tools (Hand, Food Bucket, Build Tool, Binoculars, Tranquilizer); use Tab for management screens and Escape to pause.

## Mechanics

- First-person zoo keeper character with Enhanced Input movement, sprint, jump, camera look, interaction traces, and an equippable five-tool kit
- Animal simulation with needs components (hunger, thirst, sleep, social), behavior-tree AI tasks (eat, sleep, socialize, wander), needs services/decorators, and a breeding component
- Enclosure system with enclosure actors and volume components, zoo buildings, feeders, enrichment items, and a building placement component
- Economy subsystem with funds, transactions, daily expenses (staff salaries, feed, maintenance), daily finance reports, and starting-funds configuration
- Visitor AI characters with a visitor subsystem and staff characters with AI controllers and a staff subsystem
- Progression systems: research subsystem with categories (animals, buildings, economy, veterinary, conservation), milestones, zoo rating/reputation, and random events
- World simulation: day/time subsystem with pause, weather subsystem, day/night cycle and date tracking in the replicated game state
- Persistence via a save-game class and save subsystem with quicksave/quickload hooks in the player controller
- Full programmatic C++ UMG interface: main menu, pause menu, HUD, build menu, animal info, finance panel, research tree, staff roster, tutorial, overview, and save/load widgets
- Procedurally assembled zoo level (entrance, avenues, plazas, ponds, enclosure rows for lions, elephants, penguins, monkeys, bears, giraffes, tigers, reptiles) built at runtime from basic-shape meshes

## Tags

- simulation
- management
- zoo
- first-person
- 3d
- singleplayer
- unreal-engine
- tycoon
- strategy

## Controls

- Mobile controls: Not established
- Motion controls: Not established
- Gamepad: Not established
- Keyboard/mouse: Supported

## Player modes

- Human players: 1
- Modes: single-player

## Technologies

- **Unreal Engine 5.7** — engine ([evidence](https://github.com/JamesTroy/ZooKeeper/blob/main/ZooKeeper.uproject))
- **C++** — language ([evidence](https://api.github.com/repos/JamesTroy/ZooKeeper/languages))
- **Enhanced Input** — framework ([evidence](https://github.com/JamesTroy/ZooKeeper/blob/main/ZooKeeper.uproject))
- **UMG** — framework ([evidence](https://github.com/JamesTroy/ZooKeeper/blob/main/ZooKeeper.uproject))
- **Lumen** — rendering ([evidence](https://raw.githubusercontent.com/JamesTroy/ZooKeeper/main/Config/DefaultEngine.ini))
- **Niagara** — framework ([evidence](https://github.com/JamesTroy/ZooKeeper/blob/main/ZooKeeper.uproject))
- **Unreal Build Tool** — build ([evidence](https://github.com/JamesTroy/ZooKeeper/blob/main/Source/ZooKeeper/ZooKeeper.Build.cs))

## Reconstructed prompt

Create Zoo Keeper, a first-person zoo management game in Unreal Engine 5.7 with C++. Include a first-person keeper character (WASD + mouse, sprint, jump, E to interact, B for build mode, five switchable tools), behavior-tree animal AI with hunger/thirst/sleep/social needs plus breeding, enclosures/buildings/feeders/enrichment with placement, an economy with daily expenses and reports, visitor and staff AI, research/milestone/rating/reputation/random-event progression, day-night-time and weather simulation, save/load with quicksave, and a full programmatic UMG UI (main menu, HUD, build menu, animal info, finance, research tree, staff roster, tutorial). Assemble the zoo level procedurally at runtime (entrance, avenues, plazas, ponds, themed enclosure rows).

## Source evidence

- Repository JamesTroy/ZooKeeper exists, is public, not a fork, created 2026-02-16, default branch main, primary language C++, 0 stars, 0 forks, no description, no homepage, Pages disabled. ([source](https://api.github.com/repos/JamesTroy/ZooKeeper))
- Project file describes 'A first-person zoo keeper management game', EngineAssociation 5.7, a Runtime ZooKeeper module depending on Engine, CoreUObject, AIModule, NavigationSystem and UMG, with EnhancedInput, Water, Niagara and CommonUI plugins enabled. ([source](https://github.com/JamesTroy/ZooKeeper/blob/main/ZooKeeper.uproject))
- Project settings name the game 'Zoo Keeper' version 0.1.0 with the same first-person management description, and set MaxPlayers=1, establishing single-player with one human player. ([source](https://raw.githubusercontent.com/JamesTroy/ZooKeeper/main/Config/DefaultGame.ini))
- Input bindings establish keyboard/mouse controls: WASD movement axes, MouseX/MouseY look axes, SpaceBar jump, E interact, LeftShift sprint, B build-mode toggle; input runs through Enhanced Input with UMG/Slate UI. ([source](https://raw.githubusercontent.com/JamesTroy/ZooKeeper/main/Config/DefaultInput.ini))
- Tool component handles tool switching via scroll wheel and number keys 1-5 across Hand, Food Bucket, Build Tool, Binoculars and Tranquilizer; the player controller adds Escape pause and Tab management keys, all keyboard/mouse driven. ([source](https://raw.githubusercontent.com/JamesTroy/ZooKeeper/main/Source/ZooKeeper/Player/ToolComponent.h))
- No touch, on-screen joystick, accelerometer/gyroscope, or gamepad bindings are documented anywhere in the inspected input configuration or controller code; support is therefore unestablished rather than ruled out. ([source](https://raw.githubusercontent.com/JamesTroy/ZooKeeper/main/Source/ZooKeeper/Core/ZooPlayerController.cpp))
- Codebase spans ~150 files (~465KB C++): animal AI/behavior-tree tasks, needs and breeding components; enclosures, buildings, feeders, enrichment; core game mode/state/character/controller; economy, interaction, tools, save/load, staff, 12 world subsystems, 11 UI widgets, and visitor AI. ([source](https://api.github.com/repos/JamesTroy/ZooKeeper/git/trees/main?recursive=1))
- Data model defines animal species rows (identity, food/social/size/danger classification, mesh/anim/icon visuals, audio cues, biome habitat, walk/run speeds, needs decay), research categories, biomes, and economy/transaction types. ([source](https://raw.githubusercontent.com/JamesTroy/ZooKeeper/main/Source/ZooKeeper/Data/ZooDataTypes.h))
- Runtime zoo layout is assembled procedurally from engine basic-shape meshes (cube, cylinder, sphere, plane) with tinted materials: entrance, avenues, plazas, ponds, trees, benches, signs, and themed enclosure rows (lions, elephants, penguins, monkeys, bears, giraffes, tigers, reptiles). ([source](https://raw.githubusercontent.com/JamesTroy/ZooKeeper/main/Source/ZooKeeper/Core/ZooLevelBuilder.cpp))
- Commit history shows 12 commits in a single day (2026-02-16) including 'Implement full playable build: Phases 0-8' and several compilation-fix commits; there are no releases, no README, no screenshots or image assets anywhere in the file tree, and the only Content asset is a small Git-LFS map pointer. ([source](https://api.github.com/repos/JamesTroy/ZooKeeper/commits?per_page=20))
- No playable URL is established: no homepage, no GitHub Pages site, no releases or packages, and the game is a native UE5 C++ project requiring an engine build rather than a browser artifact. ([source](https://github.com/JamesTroy/ZooKeeper))
- Repo page shows no description, screenshots, or playable links; the file listing (Config, Content, Source, .gitattributes, .gitignore, .uproject) confirms there are no inspectable gameplay images. ([source](https://github.com/JamesTroy/ZooKeeper))
- No catalog entry matches this game: no existing game references this repository, playable URL, or project, and no prior entry is a zoo management game by this author. ([source](https://github.com/JamesTroy/ZooKeeper))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 75/100: \[Fictional review\] Imagined management-sim fan: the design doc breadth is genuinely exciting — behavior-tree animals with hunger, thirst, sleep and social needs, breeding, staff shifts, visitor AI, research trees and random events, all wired through a first-person keeper. If even half of it runs, this is the zoo sim I have wanted for years.
- 55/100: \[Fictional review\] Made-up UE tinkerer note: twelve commits in a single day, version 0.1.0, no screenshots, no packaged build, and a level built from engine basic-shape cubes with tinted materials. Ambitious scaffold, but nothing here proves it plays, performs, or is balanced yet.
- 90/100: \[Fictional review\] Invented systems-nerd take: a dozen world subsystems (economy, visitors, staff, weather, time, rating, milestones, research, saves) plus a full programmatic UMG suite and BT animal AI in pure C++? Absurd scope for a solo prototype — I want to believe.

## Links

- [Source repository](https://github.com/JamesTroy/ZooKeeper)
- [Unreal project file](https://github.com/JamesTroy/ZooKeeper/blob/main/ZooKeeper.uproject)
