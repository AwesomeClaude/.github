# PirateSeas

[Open the game source](https://github.com/AndreiBesliu/PirateSeas)
**Repository created:** 2026-09-14T07:56:53Z
**Added to catalog:** 2026-09-27T04:44:55.352967+00:00
**Updated in catalog:** 2026-09-27T04:44:55.352967+00:00

**Overall rating:** 50/100. Deepest naval simulation in the catalog: physical buoyancy, wind/sail model, ballistic gunnery with measured verification, AI squadrons, convoy campaign layer, islands and synthesized audio across ~590KB of C++ and ~485KB of Python. That technical depth exceeds THORNMERE (46) and rivals top-ranked Ashlands (55). But no gameplay screenshot could be inspected, there is no publicly downloadable or browser-playable build (Windows-only packaged exe, excluded from git), and docs are Romanian-only, so polish, performance and playability are unverified. Ranked just below Ashlands and OSRS Tower Defense (52) and above THORNMERE.

**Screenshot score:** not scored. No inspectable gameplay screenshot.

## Play

- Open the Unreal project with PirateSeas.uproject in Unreal Engine 5.7 and press Play to start on the open ocean.
- Or on Windows, package a standalone build with RunUAT BuildCookRun and launch it from Packaged\\Windows\\PirateSeas.exe, optionally via the double-click launchers in the Joaca folder.
- Sail with W/S to raise and lower sail and A/D or arrow keys for the rudder; speed comes from sail, wind strength and wind angle, and the rudder only bites with way on.
- Fire port broadsides with Q and starboard with E; aim guns with the mouse, set barrel elevation with the wheel, hold Left Shift to aim at rigging, press X to lock guns abeam, R to shift crew to repairs, T to order hull planking.
- Win fights by sinking or dismasting enemy warships, or play convoy scenarios: intercept merchants until enough strike their colors, or escort them to the roadstead and into port.

## Mechanics

- Wind-powered square-rig sailing model with sail state, wind strength and point of sail determining speed
- Buoyancy-based floating hull with physical cannonballs, gravity, muzzle velocity and ship-velocity inheritance plus target lead
- Broadside gunnery with four separately reloading guns per side, per-gun traverse limits, elevation control and manual or automatic laying
- Location-based damage: hull integrity, rigging/sail degradation, rudder damage and individual gun knockouts through gunports
- Enemy AI captain with tactics, range keeping, tacking/gybing, squadron line-ahead formation keeping, friendly-fire checks and grounding recovery
- Convoy and escort scenarios with fleeing merchants that strike colors, a roadstead sanctuary, a ship ledger, hull planking purchases and port economy hooks
- Islands with beaches and sandbanks that push ships back offshore and block shots, plus muzzle flash, gun smoke, splinters, shot trails and hull impact marks
- Synthesized positional sound effects for cannon, hull hits, rigging hits and splashes

## Tags

- naval-combat
- pirate
- sailing-simulator
- unreal-engine
- single-player
- prototype
- action
- strategy

## Controls

- Mobile controls: Not established
- Motion controls: Not established
- Gamepad: Supported
- Keyboard/mouse: Supported

## Player modes

- Human players: 1
- Modes: single-player

## Technologies

- **Unreal Engine 5.7** — engine ([evidence](https://raw.githubusercontent.com/AndreiBesliu/PirateSeas/main/PirateSeas.uproject))
- **C++** — language ([evidence](https://api.github.com/repos/AndreiBesliu/PirateSeas/languages))
- **Python** — language ([evidence](https://github.com/AndreiBesliu/PirateSeas/blob/main/Scripts/ship.py))
- **Unreal Physics** — physics ([evidence](https://raw.githubusercontent.com/AndreiBesliu/PirateSeas/main/Source/PirateSeas/PirateSeas.Build.cs))

## Reconstructed prompt

Create an Unreal Engine 5.7 C++ pirate naval combat prototype: a procedurally modeled square-rigged warship sailing on open ocean with buoyancy physics and a wind model, broadside cannons with real ballistic shells, zoned damage (hull, rigging, rudder, guns), an AI enemy captain with squadron tactics, islands with grounding sandbanks, convoy interception and escort scenarios with surrendering merchants, synthesized sound effects, keyboard/mouse plus gamepad controls, and a scripted build plus automated measurement suite verifying every system.

## Source evidence

- Repository AndreiBesliu/PirateSeas is a public non-fork C++ project created 2026-09-14, default branch main, with Unreal Engine 5.7 pirate-ship sailing and naval combat prototype content. ([source](https://api.github.com/repos/AndreiBesliu/PirateSeas))
- README describes sailing a pirate ship with sails on open ocean and fighting an AI-driven enemy ship, with physical floating, wind, ballistic cannons and hull integrity, all in C++ with no Blueprint nodes. ([source](https://github.com/AndreiBesliu/PirateSeas/blob/main/README.md))
- README documents keyboard and mouse controls: W/S sail, A/D and arrows rudder, Q/E broadsides, Shift aim at rigging, R repairs, mouse aims camera and guns, wheel sets elevation, X locks guns, T orders planking. ([source](https://github.com/AndreiBesliu/PirateSeas/blob/main/README.md))
- README documents gamepad binding T as gamepad B/circle for planking orders, and DefaultInput.ini maps Fire/Aim/Repair/LayAbeam/Tackle plus sticks and triggers to gamepad keys. ([source](https://raw.githubusercontent.com/AndreiBesliu/PirateSeas/main/Config/DefaultInput.ini))
- DefaultInput.ini maps W/S/arrows, Q/E/R/X/T, mouse axes, wheel elevation and matching gamepad actions, establishing keyboard/mouse and gamepad support. ([source](https://raw.githubusercontent.com/AndreiBesliu/PirateSeas/main/Config/DefaultInput.ini))
- No touch interface is enabled by default (bAlwaysShowTouchInterface=False, bUseMouseForTouch=False) and no accelerometer/gyroscope gameplay mapping is documented, so mobile and motion support are unestablished. ([source](https://raw.githubusercontent.com/AndreiBesliu/PirateSeas/main/Config/DefaultInput.ini))
- Game is single-player versus AI: the player commands one ship against AI captains, enemy squadrons of up to 8, and merchant convoys; no local or online multiplayer is documented. ([source](https://github.com/AndreiBesliu/PirateSeas/blob/main/README.md))
- The only play path is a Windows standalone exe built with RunUAT into Packaged/, which is gitignored, launched via .bat files in the Joaca folder; no web build, store page, release download, or GitHub Pages site exists. ([source](https://github.com/AndreiBesliu/PirateSeas/tree/main/Joaca))
- Releases list is empty and the repo has no homepage or Pages site, so no publicly reachable playable URL is established. ([source](https://api.github.com/repos/AndreiBesliu/PirateSeas/releases))
- Full file tree contains Unreal maps, materials, meshes, sounds and C++/Python sources but the only PNG (Scripts/ship\_preview.png) is a Blender hull render on a gradient background, not a gameplay screenshot; the README embeds no gameplay images. ([source](https://api.github.com/repos/AndreiBesliu/PirateSeas/git/trees/main?recursive=1))
- Inspected Scripts/ship\_preview.png shows only an untextured Blender ship model on a gradient backdrop with no water, HUD, enemies or game scene, so it is a modeling preview rather than evidence of in-game visuals. ([source](https://raw.githubusercontent.com/AndreiBesliu/PirateSeas/main/Scripts/ship_preview.png))
- PirateSeas.uproject declares EngineAssociation 5.7 with Water, Buoyancy, EnhancedInput and PythonScriptPlugin modules, establishing the engine and version. ([source](https://raw.githubusercontent.com/AndreiBesliu/PirateSeas/main/PirateSeas.uproject))
- Language split is mostly C++ with substantial Python plus small PowerShell/Batch/C# build files, matching the C++ game module and Python asset/build scripts. ([source](https://api.github.com/repos/AndreiBesliu/PirateSeas/languages))
- PirateSeas.Build.cs depends on PhysicsCore among core engine modules, establishing Unreal physics usage by the game. ([source](https://raw.githubusercontent.com/AndreiBesliu/PirateSeas/main/Source/PirateSeas/PirateSeas.Build.cs))
- No AI creation model is attributed in the inspected project sources; the README credits script/procedural generation via Blender and the Unreal Python API, not a named model. ([source](https://github.com/AndreiBesliu/PirateSeas/blob/main/README.md))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 85/100: A demanding age-of-sail sim: wind, sail trim and a 12-gun broadside arc finally make maneuver feel like gunnery.
- 62/100: Fascinating systems and honest measurement logs, but Romanian-only docs and no easy download keep it at dock for most players.
- 100/100: Watching a full squadron wear around while my rigging repair timer ticks down is the most Age-of-Sail thing I have played in years.

## Links

- [Source repository](https://github.com/AndreiBesliu/PirateSeas)
