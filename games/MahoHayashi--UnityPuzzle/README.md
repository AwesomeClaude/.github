# UnityPuzzle

[View source](https://github.com/MahoHayashi/UnityPuzzle) · [Previous report](https://github.com/AwesomeClaude/.github/blob/796938a221f7bc9b20f657c7cbf9cdb31cd783fe/games/MahoHayashi--UnityPuzzle/README.md)

| Overall rating | Screenshot score |
| :---: | :---: |
| **15/100** | **Not scored** |

<details>
<summary>Read the scoring rationale</summary>

### Overall rating

Far from AAA production quality and below every cataloged game on available evidence. Kart Royale (50) and Turbo Kart Rally (40) are complete 3D racers with AI fields, HUDs, and stylized worlds; 2048 (38) and T-Rex Runner (35) are finished, instantly playable browser loops; even curiositY (18), the lowest-rated catalog entry, ships a complete 15-level riddle trail with a live site. UnityPuzzle is a single-commit Unity prototype with one scene, five small CSV maps, arrow-key teleport movement, and placeholder sprites (plain beige square Wall, Unity-cube Block, multicolor Goal shard — three sprites visually inspected), and no README, no playable WebGL/Pages build, no releases, and no evidenced win, collision, or block-pushing rules in the inspected GameManager/StageManager sources. It earns points for a coherent Sokoban-like structure (tile types, 5 stages, directional sprites) but cannot be played without the Unity Editor, so scope, polish, and technical execution are all unverified beyond static project files. Evidence gaps: no gameplay screenshots, video, builds, or docs; gh CLI was unavailable so evidence came via public api.github.com and raw file fetches instead; source-file findings cannot prove playability, performance, or balance.

### Screenshot score

No inspectable gameplay screenshot.

</details>

## At a glance

| Detail | Value |
| --- | --- |
| Repository created | 10 Jul 2026 · 07:28 UTC |
| Added to catalog | 27 Sep 2026 · 03:49 UTC |
| Last updated | 27 Sep 2026 · 04:05 UTC |
| Documented creation models | [Claude Opus 4.8](https://github.com/MahoHayashi/UnityPuzzle/commit/44dcdea5b61c678f968b78f4a09f1c995758ffe2) |

## Play

- No public playable build exists, so the Unity Editor is required: clone https://github.com/MahoHayashi/UnityPuzzle and open it as a Unity project (ProjectVersion.txt specifies 2022.3.62f2)
- Open Assets/Scenes/Main.unity and press Play
- Move the player one tile per press with the Up, Down, Left, and Right arrow keys
- Explore the five CSV maps under Assets/StageTexts (stage0.txt through stage4.txt); win, collision, and block-pushing rules are not documented or evidenced in the inspected sources

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

## Technologies

- **Unity 2022.3.62f2** — engine ([evidence](https://raw.githubusercontent.com/MahoHayashi/UnityPuzzle/main/ProjectSettings/ProjectVersion.txt))
- **C#** — language ([evidence](https://api.github.com/repos/MahoHayashi/UnityPuzzle/languages))

## Reconstructed prompt

Create a small Unity 2D Sokoban-style puzzle: a Main scene bootstrapped by GameManager, StageManager, and PlayerManager scripts; load 5 small CSV grid maps from text files (walls, ground, blocks, block-goals, player starts); instantiate one prefab per tile with plain 2D sprites including directional player keys; move the player one tile per arrow-key press.

## Source evidence

- Repository is MahoHayashi/UnityPuzzle: public, C#, single main branch, 1 commit, 0 stars, 0 forks, no description, no homepage, no topics, has\_pages false ([source](https://api.github.com/repos/MahoHayashi/UnityPuzzle))
- Only commit is 'Initial commit: Unity puzzle game' dated 2026-07-10, co-authored by Claude Opus 4.8 \<noreply@anthropic.com\> ([source](https://github.com/MahoHayashi/UnityPuzzle/commit/44dcdea5b61c678f968b78f4a09f1c995758ffe2))
- Repo root has no README and only Assets, Packages, ProjectSettings plus .gitignore; it is a Unity project, not a web build ([source](https://api.github.com/repos/MahoHayashi/UnityPuzzle/contents/))
- GameManager.cs moves the player one tile per arrow-key press via Input.GetKeyDown(KeyCode.UpArrow/DownArrow/LeftArrow/RightArrow) with no touch, motion, or gamepad input evidenced; establishes keyboard support ([source](https://raw.githubusercontent.com/MahoHayashi/UnityPuzzle/main/Assets/GameManager.cs))
- StageManager.cs loads a CSV TextAsset into WALL/GROUND/BLOCK\_POINT/BLOCK/PLAYER enums and instantiates one prefab per tile plus a ground layer, using SpriteRenderer bounds for tile sizing; only PLAYER and BLOCK positions are tracked, with no win/collision logic evidenced ([source](https://raw.githubusercontent.com/MahoHayashi/UnityPuzzle/main/Assets/StageManager.cs))
- PlayerManager.cs exposes only a Move(Vector3) transform setter with empty Start/Update; single-player token movement only, no multiplayer evidence ([source](https://raw.githubusercontent.com/MahoHayashi/UnityPuzzle/main/Assets/PlayerManager.cs))
- Five stage maps stage0.txt through stage4.txt exist (each 125 bytes); stage0 is a 7x9 CSV grid of tile ids 0-4 forming a walled room with goal/block/player markers ([source](https://raw.githubusercontent.com/MahoHayashi/UnityPuzzle/main/Assets/StageTexts/stage0.txt))
- Single scene Assets/Scenes/Main.unity exists ([source](https://api.github.com/repos/MahoHayashi/UnityPuzzle/contents/Assets/Scenes?ref=main))
- Nine gameplay prefabs exist (Block, BlockPoint, Goal, Ground, Wall, Up/Down/Left/RightImage) ([source](https://api.github.com/repos/MahoHayashi/UnityPuzzle/contents/Assets/Prefabs?ref=main))
- Asset art is 9 individual placeholder sprites (3-7 KB each): Wall, Ground, Block, BlockPoint, Goal, Up/Down/Left/RightImage; three (Wall beige square, Block Unity-cube, Goal multicolor shard) downloaded and visually inspected — single tiles only, no composited gameplay screenshot exists in the repo ([source](https://api.github.com/repos/MahoHayashi/UnityPuzzle/contents/Assets/Images?ref=main))
- No releases, no GitHub Pages site, and null homepage: no publicly reachable playable URL is established ([source](https://api.github.com/repos/MahoHayashi/UnityPuzzle/releases))
- ProjectVersion.txt pins Unity editor 2022.3.62f2 ([source](https://raw.githubusercontent.com/MahoHayashi/UnityPuzzle/main/ProjectSettings/ProjectVersion.txt))
- Languages endpoint reports C# only, matching the three inspected .cs scripts ([source](https://api.github.com/repos/MahoHayashi/UnityPuzzle/languages))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 55/100: Fictional take: a neat little Sokoban sketch — five tiny maps, chunky tiles, and arrow-key shuffling that feels like a first-week Unity exercise. Charming as a starting point.
- 30/100: Fictional take: I pushed around the test map for a minute and ran out of things to discover. No win fanfare, no push rules I could verify, placeholder art everywhere.
- 70/100: Fictional take: as a prototype it has bones — CSV levels, clean prefab-per-tile structure, directional sprites. Give it collision, goals, and a WebGL build and it could be a real coffee-break puzzler.

## Links

- [Source repository](https://github.com/MahoHayashi/UnityPuzzle)
