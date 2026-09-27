# Lille

[View source](https://github.com/leynos/lille)

| Overall rating | Screenshot score |
| :---: | :---: |
| **28/100** | **Not scored** |

<details>
<summary>Read the scoring rationale</summary>

### Overall rating

Far from AAA: Phase 1 RTS prototype with no campaign, win or loss loop, multiplayer, audio, cinematics or live-ops scale, no public playable URL, no releases or Pages, and no inspectable gameplay frame, so playability, performance and balance are unverified. Most relevant comparators: UnityPuzzle (15, single-commit engine prototype with placeholder sprites and no build) is the floor Lille clearly exceeds on codebase scale, docs and test discipline across 341 tracked paths; curiosity (18, complete 15-level riddle trail with a live site) ships a finished loop Lille lacks; Beachy Beachy Ball (25, complete minimal live loop) and TypeScript-Blackjack (28, complete single-table rules) are the shipped-tiny-game tier Lille roughly matches on AAA proximity for opposite reasons; Neural Sight (30), chess rot (30) and Find Panda (30) all pair narrow scope with either inspectable visuals or a complete loop, which Lille cannot match; SpaceHo2 (42), neverquest (45), Kart Royale (50) and Ashlands (55) vastly exceed it on finished gameplay depth and proven execution. Ranked at 28: above the prototype floor on technical ambition, below every complete loop with verified play.

### Screenshot score

No inspectable gameplay screenshot.

</details>

## At a glance

| Detail | Value |
| --- | --- |
| Repository created | 17 Jan 2025 · 23:11 UTC |
| Added to catalog | 27 Sep 2026 · 04:41 UTC |
| Last updated | 27 Sep 2026 · 04:41 UTC |
| Documented creation models | Not established |

## Play

- Install the pinned Rust nightly toolchain (rust-toolchain.toml pins nightly-2025-09-14) with rustfmt and clippy components
- Run the desktop game with cargo run -p lille --features render (rendering is gated behind the render feature)
- Optionally enable text rendering with cargo run -p lille --features text, which implies render
- Pan the single presentation camera with W/A/S/D or arrow keys at the configured pan speed
- The map plugin loads assets/maps/primary-isometric.tmx at startup and spawns the player and actors on map readiness; there is no browser or public playable build

## Mechanics

- Bevy ECS as state container with a DBSP dataflow circuit as the declarative logic engine, stepped once per tick
- ECS-to-DBSP input sync plus DBSP-to-ECS output sync for positions, velocities, health and behaviour decisions
- Single primary isometric Tiled map loaded at startup via LilleMapPlugin, defaulting to maps/primary-isometric.tmx
- Tiled custom properties translated into engine state such as collidable blocks, slopes, player spawns and spawn points
- Declarative physics streams for kinematics, floor heights, forces, friction and applied acceleration
- Reactive agent behaviour streams including fear, targeting, movement decisions and health and damage pipelines
- Single presentation camera with keyboard panning and planned isometric Y-sorting of sprites
- Fractured-city RTS setting with corporate militias, syndicates, data cults and faction squads described as lore rather than an evidenced win or loss loop

## Tags

- rts
- real-time-strategy
- strategy
- isometric
- prototype
- bevy
- rust
- dataflow
- tiled
- single-player

## Controls

- Mobile controls: Not established
- Motion controls: Not established
- Gamepad: Not established
- Keyboard/mouse: Supported

## Player modes

- Human players: 1
- Modes: single-player

## Technologies

- **Rust** — language ([evidence](https://raw.githubusercontent.com/leynos/lille/main/rust-toolchain.toml))
- **Bevy 0.18.1** — engine ([evidence](https://raw.githubusercontent.com/leynos/lille/main/Cargo.toml))
- **bevy\_ecs\_tiled 0.12.0** — framework ([evidence](https://raw.githubusercontent.com/leynos/lille/main/Cargo.toml))
- **DBSP 0.98** — framework ([evidence](https://raw.githubusercontent.com/leynos/lille/main/Cargo.toml))
- **glam 0.33** — framework ([evidence](https://raw.githubusercontent.com/leynos/lille/main/Cargo.toml))

## Reconstructed prompt

Build Lille, an overengineered isometric real-time strategy prototype in Rust with Bevy 0.18: a single Bevy app where ECS holds world state and a DBSP incremental dataflow circuit holds all physics, geometry and reactive behaviour logic; load one primary Tiled isometric map with custom properties into ECS and physics; spawn a player plus actors on map readiness; render static entities with a keyboard-pannable presentation camera; document architecture, map pipeline and user configuration; verify with rstest, rspec-style, BDD and contract tests behind cargo features.

## Source evidence

- Repository leynos/lille is public, described as Overengineered RTS, primary language Rust, created 2025-01-17, pushed 2026-09-25, 0 stars, 0 forks, ISC license, default branch main, homepage empty, has\_pages false ([source](https://api.github.com/repos/leynos/lille))
- Language breakdown is Rust-dominated with small Makefile and Shell shares, matching a Rust Bevy workspace ([source](https://api.github.com/repos/leynos/lille/languages))
- README titles the project Lille and calls it a simple real-time strategy prototype with an optional-Bevy-subsystem dataflow game loop, currently Phase 1 synchronizing legacy GameWorld state into Bevy and rendering static entities ([source](https://github.com/leynos/lille/blob/main/README.md))
- Cargo manifest describes the package as A realtime strategy game, edition 2021, with a lille binary gated on render and map features ([source](https://github.com/leynos/lille/blob/main/Cargo.toml))
- The game is run locally with cargo run -p lille --features render, with text rendering layered via cargo run -p lille --features text; rendering tests use cargo test -p lille --features render ([source](https://github.com/leynos/lille/blob/main/README.md))
- Entry point launches a single local Bevy App with DbspPlugin, PresentationPlugin and LilleMapPlugin; no multiplayer, networking, server or client mode is documented or wired ([source](https://github.com/leynos/lille/blob/main/src/main.rs))
- Camera system reads WASD and arrow keys for panning with configurable pan speed and clamped delta time, establishing keyboard support ([source](https://github.com/leynos/lille/blob/main/src/presentation.rs))
- Presentation design says keyboard plus mouse inputs were planned for camera control, but the inspected implementation only evidences keyboard panning, so mouse support beyond windowed desktop play is unestablished ([source](https://github.com/leynos/lille/blob/main/docs/lille-presentational-layer.md))
- No touch, on-screen joystick, accelerometer, gyroscope or gamepad handling was found in the inspected presentation, map, components or run paths; the project targets desktop cargo run with Linux x11, so those statuses remain unknown rather than ruled out ([source](https://github.com/leynos/lille/blob/main/src/presentation.rs))
- Map pipeline loads a single primary Tiled map by default from maps/primary-isometric.tmx, validates the asset path, spawns the player and actors on map readiness, and enforces a single-active-map lifecycle ([source](https://github.com/leynos/lille/blob/main/docs/users-guide.md))
- Recursive main-branch tree has 341 paths and exactly one image file, assets/maps/tiles/iso-tile.png; no docs, screenshots or gameplay captures exist in-repo ([source](https://api.github.com/repos/leynos/lille/git/trees/main?recursive=1))
- The sole image asset was downloaded and visually inspected: a 64x32 single green isometric diamond tile texture, not a gameplay frame, so no graphics score can be given ([source](https://raw.githubusercontent.com/leynos/lille/main/assets/maps/tiles/iso-tile.png))
- No releases exist, the Pages API returns 404, the repo contents show no web build output, and the documented play path is local cargo run, so no publicly reachable playable URL is established ([source](https://api.github.com/repos/leynos/lille/releases))
- Active stack is documented as Bevy 0.18.1 with bevy\_ecs\_tiled map loading, DBSP dataflow logic, glam math and a nightly-2025-09-14 Rust toolchain ([source](https://github.com/leynos/lille/blob/main/docs/developers-guide.md))
- No prior catalog game references leynos, lille or Overengineered RTS, so no existing slug is reused ([source](https://github.com/leynos/lille))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 70/100: Fictional illustrative review one: panned across the isometric map with WASD and watched static entities tick through the DBSP loop — as an overengineered RTS sketch the separation of Bevy state and dataflow logic is genuinely interesting.
- 45/100: Fictional illustrative review two: made-up player note — interesting architecture docs and a real map asset, but I never saw a gameplay frame, there is no playable link, and Phase 1 is mostly camera plus static entities, so there is no game to judge yet.
- 95/100: Fictional illustrative review three: invented engine-nerd take — a declarative DBSP physics and behaviour circuit synced into Bevy ECS with Tiled isometric maps and hundreds of tests? As a prototype codebase this is the most rigorous tech demo in its tier.

## Links

- [Source repository](https://github.com/leynos/lille)
- [Source README](https://github.com/leynos/lille/blob/main/README.md)
- [Source Cargo manifest](https://github.com/leynos/lille/blob/main/Cargo.toml)
