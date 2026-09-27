# UnityPuzzle

[Open the game source](https://github.com/MahoHayashi/UnityPuzzle)
**Repository created:** 2026-07-10T07:28:29Z
**Added to catalog:** 2026-09-27T03:49:50.928883+00:00
**Updated in catalog:** 2026-09-27T03:49:50.928883+00:00
**Built with:** [Claude Opus 4.8](https://github.com/MahoHayashi/UnityPuzzle/commit/44dcdea5b61c678f968b78f4a09f1c995758ffe2)

**Overall rating:** 15/100. Far from AAA production quality and below every cataloged game on available evidence. Kart Royale (50) and Turbo Kart Rally (40) are complete 3D racers with AI fields, HUDs, and stylized worlds; 2048 (38) and T-Rex Runner (35) are finished, instantly playable browser loops; even curiositY (18), the lowest-rated catalog entry, ships a complete 15-level riddle trail with a live site. UnityPuzzle is a single-commit Unity prototype with one scene, five small CSV maps, arrow-key teleport movement, and placeholder sprites (plain beige/brown squares, a Unity-cube block, keyboard-key player icons) — and no README, no playable WebGL/pages build, no releases, and no evidenced win, collision, or block-pushing rules in the inspected GameManager/StageManager sources. It earns points for a coherent Sokoban-like structure (tile types, 5 stages, directional sprites) but cannot be played without the Unity Editor, so scope, polish, and technical execution are all unverified beyond static project files. Evidence gaps: no gameplay video, screenshots, builds, or docs; source-file findings limited to API-served file content, which cannot prove playability, performance, or balance.

**Screenshot score:** not scored. No inspectable gameplay screenshot.

## Play

- No public playable build exists, so Unity Editor is required: clone https://github.com/MahoHayashi/UnityPuzzle and open it as a Unity project
- Open Assets/Scenes/Main.unity and press Play
- Move the player one tile per press with the Up, Down, Left, and Right arrow keys
- Explore the five CSV maps under Assets/StageTexts (stage0.txt through stage4.txt); win, push, and goal rules are not documented or evidenced in the verified sources

## Mechanics

- Arrow-key grid movement of a single player token (one tile per key press)
- CSV text-defined stages loaded at runtime (five maps: stage0.txt through stage4.txt)
- Prefab-per-tile stage construction (Wall, Ground, Block, BlockPoint, Goal, directional player sprites)
- Tile-coordinate to screen-position mapping with centered grid layout
- Single Main.unity scene bootstrapped by GameManager plus StageManager

## Tags

- puzzle
- sokoban
- grid
- 2d
- unity

## Controls

- Mobile controls: Not established
- Motion controls: Not established
- Gamepad: Not established
- Keyboard/mouse: Supported

## Player modes

- Human players: 1
- Modes: single-player

## Reconstructed prompt

Create a small Unity 2D Sokoban-style puzzle: a Main scene bootstrapped by GameManager, StageManager, and PlayerManager scripts; load 5 small CSV grid maps from text files (walls, ground, blocks, block-goals, player starts); instantiate one prefab per tile with plain 2D sprites including directional player keys; move the player one tile per arrow-key press.

## Source evidence

- Repository is MahoHayashi/UnityPuzzle: public, C#, single main branch, 1 commit, 0 stars, 0 forks, no description, no homepage, no topics, has\_pages false ([source](https://api.github.com/repos/MahoHayashi/UnityPuzzle))
- Only commit is 'Initial commit: Unity puzzle game' dated 2026-07-10, co-authored by Claude Opus 4.8 \<noreply@anthropic.com\> ([source](https://github.com/MahoHayashi/UnityPuzzle/commit/44dcdea5b61c678f968b78f4a09f1c995758ffe2))
- Repo root has no README and only Assets, Packages, ProjectSettings plus .gitignore; it is a Unity project, not a web build ([source](https://api.github.com/repos/MahoHayashi/UnityPuzzle/contents/))
- GameManager.cs moves the player one tile per arrow-key press via Input.GetKeyDown(KeyCode.UpArrow/DownArrow/LeftArrow/RightArrow) with no touch, motion, or gamepad input evidenced ([source](https://github.com/MahoHayashi/UnityPuzzle/blob/main/Assets/GameManager.cs))
- StageManager.cs loads a CSV TextAsset into WALL/GROUND/BLOCK\_POINT/BLOCK/PLAYER enums and instantiates one prefab per tile plus a ground layer; only PLAYER and BLOCK positions are tracked, with no win/collision logic evidenced ([source](https://github.com/MahoHayashi/UnityPuzzle/blob/main/Assets/StageManager.cs))
- PlayerManager.cs exposes only a Move(Vector3) transform setter with empty Start/Update; single-player token movement only, no multiplayer evidence ([source](https://github.com/MahoHayashi/UnityPuzzle/blob/main/Assets/PlayerManager.cs))
- Five stage maps stage0.txt through stage4.txt exist (each ~125 bytes, 7x9 CSV grids of tile ids 0-4); e.g. stage0 is a walled room with goal/block/player markers ([source](https://raw.githubusercontent.com/MahoHayashi/UnityPuzzle/main/Assets/StageTexts/stage0.txt))
- Single scene Assets/Scenes/Main.unity plus 9 tile prefabs (Block, BlockPoint, Goal, Ground, Wall, Up/Down/Left/RightImage) ([source](https://api.github.com/repos/MahoHayashi/UnityPuzzle/contents/Assets/Scenes?ref=main))
- Asset art is 9 tiny placeholder sprites (3-7 KB each, inspected locally): plain beige Wall and pale-green Ground squares, Unity-logo cube Block, multicolor Goal shard, honeycomb BlockPoint, yellow keyboard-key directional player icons; no composited gameplay screenshot exists in the repo ([source](https://github.com/MahoHayashi/UnityPuzzle/tree/main/Assets/Images))
- No releases, no GitHub Pages site, and null homepage: no publicly reachable playable URL is established ([source](https://api.github.com/repos/MahoHayashi/UnityPuzzle/releases))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 55/100: Fictional take: a neat little Sokoban sketch — five tiny maps, chunky tiles, and arrow-key shuffling that feels like a first-week Unity exercise. Charming as a starting point.
- 30/100: Fictional take: I pushed around the test map for a minute and ran out of things to discover. No win fanfare, no push rules I could verify, placeholder art everywhere.
- 70/100: Fictional take: as a prototype it has bones — CSV levels, clean prefab-per-tile structure, directional sprites. Give it collision, goals, and a WebGL build and it could be a real coffee-break puzzler.

## Links

- [Source repository](https://github.com/MahoHayashi/UnityPuzzle)
