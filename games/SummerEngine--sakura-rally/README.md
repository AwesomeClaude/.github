# Sakura Rally

[View source](https://github.com/SummerEngine/sakura-rally)

| Overall rating | Screenshot score |
| :---: | :---: |
| **56/100** | **68/100** |

<details>
<summary>Read the scoring rationale</summary>

### Overall rating

Deep indie rally package: two stages plus a connected seasonal open world, campaign, time attack, free roam, garage, replays, custom physics, and synthesized audio with documented verification. Above Turbo Kart Rally (40) and Kart Royale (50) on scope, systems depth, and technical execution, near Ashlands (55) but below moorestech (64) with no web play, no human multiplayer, single-player only, and unverified playability, performance, and balance from stills and docs alone.

### Screenshot score

Best inspected frame is a ground-level start-gantry view with coherent anime styling, painted clouds, blossom trees, buildings, and dense branded dressing; aerials show large seasonal worlds with roads, rivers, and forests. Composition and stylization are strong, but frames lack visible car action and HUD, and model-viewer captures are discounted. Below Kart Royale (70) and Turbo Kart Rally (70) on gameplay detail, above OSRS Tower Defense (65) on art coherence, near scumm-game territory; stills alone prove nothing about motion or feel.

</details>

## At a glance

| Detail | Value |
| --- | --- |
| Repository created | 26 Sep 2026 · 15:24 UTC |
| Added to catalog | 27 Sep 2026 · 06:20 UTC |
| Last updated | 27 Sep 2026 · 06:20 UTC |
| Documented creation models | [Claude Opus 5.5](https://github.com/SummerEngine/sakura-rally), [elevenlabs/music/v2.5](https://github.com/SummerEngine/sakura-rally/blob/main/docs/AUDIO.md), [fal-ai/elevenlabs/sound-effects/v2](https://github.com/SummerEngine/sakura-rally/blob/main/docs/AUDIO.md) |

## Screenshots

![Inspected 1600x900 in-engine view under a pink SAKURA RALLY start gantry: straight tarmac road ahead, branded barriers, pennant string, blossom trees, houses, torii gate, spectators, painted clouds and mountains. No car or HUD visible; game's own runtime output.](https://raw.githubusercontent.com/SummerEngine/sakura-rally/main/docs/renders/hanami_tour_00.jpg)

Inspected 1600x900 in-engine view under a pink SAKURA RALLY start gantry: straight tarmac road ahead, branded barriers, pennant string, blossom trees, houses, torii gate, spectators, painted clouds and mountains. No car or HUD visible; game's own runtime output.

![Inspected 1600x900 aerial render of Hanami Pass: spring green valley with winding tarmac, river, bridge, buildings, pink sakura clusters, cedar stands, haze and painted clouds. Top-down world overview, no car or HUD.](https://raw.githubusercontent.com/SummerEngine/sakura-rally/main/docs/renders/hanami_aerial.jpg)

Inspected 1600x900 aerial render of Hanami Pass: spring green valley with winding tarmac, river, bridge, buildings, pink sakura clusters, cedar stands, haze and painted clouds. Top-down world overview, no car or HUD.

![Inspected 1600x900 aerial render of Momiji Valley: autumn golden-hour hills with winding road, river, houses, red-orange maples, dark cedars, haze and painted clouds. Top-down world overview, no car or HUD.](https://raw.githubusercontent.com/SummerEngine/sakura-rally/main/docs/renders/momiji_aerial.jpg)

Inspected 1600x900 aerial render of Momiji Valley: autumn golden-hour hills with winding road, river, houses, red-orange maples, dark cedars, haze and painted clouds. Top-down world overview, no car or HUD.

![Inspected 1600x900 aerial render of the liaison road: green summer valley with long straight road, river, rocks, cedar and sakura transition zones, haze and painted clouds. Top-down world overview, no car or HUD.](https://raw.githubusercontent.com/SummerEngine/sakura-rally/main/docs/renders/liaison_aerial.jpg)

Inspected 1600x900 aerial render of the liaison road: green summer valley with long straight road, river, rocks, cedar and sakura transition zones, haze and painted clouds. Top-down world overview, no car or HUD.

![Inspected 1600x900 model-viewer render of the white/pink Sakura rally car with number 07, gold wheels, roof intake and rear wing on a plain grey background. Vehicle showcase, not active gameplay.](https://raw.githubusercontent.com/SummerEngine/sakura-rally/main/docs/renders/car_godot_front34.png)

Inspected 1600x900 model-viewer render of the white/pink Sakura rally car with number 07, gold wheels, roof intake and rear wing on a plain grey background. Vehicle showcase, not active gameplay.

## Play

- Install Summer Engine or stock Godot 4.7, open the project folder, and press Play (macOS can use Play Sakura Rally.command).
- From the title hub choose Campaign for the connected Seasons Rally, or Time Attack for Time Trial and Free Roam cards.
- Launch with held throttle for launch control at 4600 rpm, then release into first at GO.
- Drive with W/Up throttle, S/Down brake and reverse, A/D steering, Space handbrake, E/Q manual gears, C camera, R reset, Esc/P pause, H horn, F1 hide UI.
- Follow yellow diamond warnings and chevrons, stay off soft roadside dressing where possible, and finish stages to earn medals and records.
- In Campaign, continue past the Hanami finish onto the open liaison road, then start SS2 at the Momiji grid for the final classification.

## Mechanics

- Cel-shaded rally driving with custom raycast car physics, suspension, combined-slip tyres, gearbox, turbo, and arcade crash forgiveness
- Two timed stages plus a 2 km untimed liaison road joined into one world with no loading between legs
- Campaign with results, continue/resume legs, arrival card, and classification against six rivals
- Time Trial with splits, medals, and saved records; Free Roam with open barriers and nearest-road reset
- Two cars with distinct drivetrains plus five liveries switched in a roadside workshop garage
- Soft roadside dressing that breaks with speed cost, billowing checkpoint gates, tumbling spectators, guardrails, and corner warning signs
- Four cameras including slope-aware chase, plus title flyover, garage orbit, and gate/finale cinematics
- Input-and-state replay recording for every drive with an offline review and rendering tool

## Tags

- rally
- racing
- single-player
- time-trial
- low-poly
- cel-shaded
- 3d
- godot
- desktop

## Controls

- Mobile controls: Not established
- Motion controls: Not established
- Gamepad: Supported
- Keyboard/mouse: Supported

## Player modes

- Human players: 1
- Modes: single-player

## Technologies

- **Godot 4.7** — engine ([evidence](https://github.com/SummerEngine/sakura-rally/blob/main/project.godot))
- **Summer Engine** — engine ([evidence](https://github.com/SummerEngine/sakura-rally))
- **GDScript** — language ([evidence](https://github.com/SummerEngine/sakura-rally/blob/main/docs/CONTRACTS.md))
- **Jolt Physics** — physics ([evidence](https://github.com/SummerEngine/sakura-rally/blob/main/project.godot))
- **Forward Plus** — rendering ([evidence](https://github.com/SummerEngine/sakura-rally/blob/main/project.godot))
- **FSR** — rendering ([evidence](https://github.com/SummerEngine/sakura-rally))
- **Python** — language ([evidence](https://github.com/SummerEngine/sakura-rally))
- **Blender** — build ([evidence](https://github.com/SummerEngine/sakura-rally))

## Reconstructed prompt

Build Sakura Rally, a cel-shaded low-poly Godot rally game through spring and autumn Japan with two stages joined by a drivable seasonal liaison road, custom arcade car physics, two cars and liveries, campaign plus time attack and free roam, soft breakable roadside, spectators, replays, synthesized engine audio and Japanese city-pop music.

## Source evidence

- Repository page titles it Sakura Rally as a cel-shaded low-poly rally game for Summer Engine and Godot 4.7 with two maps, custom car physics, and synthesised engine audio, built by Claude Opus 5.5 from one prompt. ([source](https://github.com/SummerEngine/sakura-rally))
- README documents Campaign as one continuous drive with no loading, Time Trial with medals and records, Free Roam with open barriers, two cars and five liveries, settings, replays, and verification results. ([source](https://github.com/SummerEngine/sakura-rally))
- Play section requires opening the project in Summer Engine or stock Godot 4.7 or the macOS command file; no browser play URL is offered. ([source](https://github.com/SummerEngine/sakura-rally))
- Controls table maps throttle, brake/reverse, steering, handbrake, manual gears, camera, reset, pause, horn, and UI-hide to keyboard keys and gamepad inputs; no touch or motion controls are documented. ([source](https://github.com/SummerEngine/sakura-rally))
- project.godot sets Godot 4.7 Forward Plus features, Jolt physics at 120 Hz, 1920x1080 viewport, car/world/prop/trigger layers, and Game/Sound/Replays autoloads. ([source](https://github.com/SummerEngine/sakura-rally/blob/main/project.godot))
- Shared contracts specify GDScript only, Forward+, Jolt, pure-GDScript compatibility with Summer and official Godot builds, plus Python mapgen, Blender car/prop scripts, and synthesized audio tooling. ([source](https://github.com/SummerEngine/sakura-rally/blob/main/docs/CONTRACTS.md))
- Audio doc attributes music to ElevenLabs Music v2.5 via fal and ambience beds to ElevenLabs sound-effects v2 via fal, with prompts, loop baking, and licensing notes; engine, world, UI, stingers, and synthesized voices are procedural. ([source](https://github.com/SummerEngine/sakura-rally/blob/main/docs/AUDIO.md))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 85/100: The spring-to-autumn liaison drive is lovely and the cel shading holds together beautifully at road level.
- 62/100: Handling feels forgiving and the corner signs help, but I wanted real rivals on track and a browser build.
- 100/100: A perfect cozy rally diorama to photograph with the UI hidden.

## Links

- [Source repository](https://github.com/SummerEngine/sakura-rally)
