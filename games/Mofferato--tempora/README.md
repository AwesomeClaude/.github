# Tempora

[Play the game](https://mofferato.github.io/tempora/) · [View source](https://github.com/Mofferato/tempora)

| Overall rating | Screenshot score |
| :---: | :---: |
| **57/100** | **48/100** |

<details>
<summary>Read the scoring rationale</summary>

### Overall rating

Tempora shows the deepest systems scope in the catalog: eleven eras, 22 lands, genetics, settlements, migrations, politics, wars, dynasties, three modes, autoplay and procedural music, verified through README layout tables and the src module list. Against calibration points, it sits above Ashlands (55), OSRS Tower Defense (52) and neverquest (45, the closest text-sim comparator but far narrower) on gameplay depth and scope, and above THORNMERE (46) and The Nine Lives of Ash (47) on simulation breadth. It stays below moorestech (64) because that game pairs deep systems with coherent 3D multiplayer execution, while Tempora is single-player text/DOM UI with no 3D scene, verified screenshots showing only panels and stat bars. Evidence gaps: no independent playtest of balance, performance, or long-run stability; headless sim harness claims exist but were not executed here.

### Screenshot score

Best frame (screenshot.png) is the game's own runtime output: coherent dark UI with character card, five stat bars, wealth readout, era timeline ribbon, tab bar, and dense year-by-year life log with color-coded stat chips. Polished typography and consistent orange/green accents place it above neverquest (30, monochrome dashboard), TypeScript-Blackjack (35, flat felt) and Top-10 Tension (32, flat quiz cards), and near 2048 (45) and The Nine Lives of Ash (50) on UI polish. It stays below Taipo (55, pixel-art scene), THORNMERE (60, textured retro scene with portrait), OSRS Tower Defense (65, dense 2D battlefield) and the catalog 70s (Kart Royale, Turbo Kart Rally, Neural Sight) because there is no rendered environment, lighting, character art beyond a flat avatar, or scene composition — only panels. World, profile and mobile frames confirm the same UI at lower density and are ordered later. Judged from stills only; no motion or feel inferred.

</details>

## At a glance

| Detail | Value |
| --- | --- |
| Repository created | 26 Sep 2026 · 17:57 UTC |
| Added to catalog | 27 Sep 2026 · 06:22 UTC |
| Last updated | 27 Sep 2026 · 06:22 UTC |
| Documented creation models | Not established |

## Screenshots

![Inspected 1280x800 gameplay frame: ancient Egypt life view for Tiye of Buto, age 32, with left character card (avatar, home, status, Chief Blacksmith, five stat bars, deben wealth 1,049), era timeline ribbon on top, tab bar, and dense year-by-year life log for 418-419 BC with family events and green/red stat-change chips; orange Age +1 bar at bottom. Game's own runtime output.](https://raw.githubusercontent.com/Mofferato/tempora/main/assets/screenshot.png)

Inspected 1280x800 gameplay frame: ancient Egypt life view for Tiye of Buto, age 32, with left character card (avatar, home, status, Chief Blacksmith, five stat bars, deben wealth 1,049), era timeline ribbon on top, tab bar, and dense year-by-year life log for 418-419 BC with family events and green/red stat-change chips; orange Age +1 bar at bottom. Game's own runtime output.

![Inspected 1280x800 gameplay frame: World tab showing settlement panel for a village near Memphis with settlement level, living-cost and wage multipliers, best-jobs note, and move buttons for Memphis and Thebes; same character card and Age bar. Game's own runtime output.](https://raw.githubusercontent.com/Mofferato/tempora/main/assets/world.png)

Inspected 1280x800 gameplay frame: World tab showing settlement panel for a village near Memphis with settlement level, living-cost and wage multipliers, best-jobs note, and move buttons for Memphis and Thebes; same character card and Age bar. Game's own runtime output.

![Inspected 1280x800 gameplay frame: character profile modal for Tiye of Buto with Overview/Stats/Personality/Life/Family/Achievements tabs and rows for age, birth, sex, nationality, class, education, occupation, relationship, children, wealth, personality and appearance. Game's own runtime output, partly overlaying the life log.](https://raw.githubusercontent.com/Mofferato/tempora/main/assets/profile.png)

Inspected 1280x800 gameplay frame: character profile modal for Tiye of Buto with Overview/Stats/Personality/Life/Family/Achievements tabs and rows for age, birth, sex, nationality, class, education, occupation, relationship, children, wealth, personality and appearance. Game's own runtime output, partly overlaying the life log.

![Inspected 780x1688 mobile frame: responsive phone layout of the same character card with stacked stat bars, wealth readout, and tab strip plus Age +1 button at bottom. Confirms small-screen layout; discounted toward graphics score as a layout variant rather than new scene detail.](https://raw.githubusercontent.com/Mofferato/tempora/main/assets/mobile.png)

Inspected 780x1688 mobile frame: responsive phone layout of the same character card with stacked stat bars, wealth readout, and tab strip plus Age +1 button at bottom. Confirms small-screen layout; discounted toward graphics score as a layout variant rather than new scene detail.

## Play

- Open https://mofferato.github.io/tempora/ in a browser (or download index.html and open it offline)
- Begin a life in any era from 10,000 BC to the far future and pick actions each year across Life, Relationships, Activities, Places, Occupation, Assets and World tabs
- Press the Age +1 button to advance one year; repeat last year, pin yearly actions, or use Auto-play and the Guide for hands-off play
- When you die, continue as an heir, relative, or someone you knew and build dynasty traits over generations

## Mechanics

- Year-by-year life simulation from 10,000 BC to the far future across eleven eras and 22 lands
- Living world simulation with growing and renamed settlements, migrations, genetics, governments, revolutions and wars
- Character systems with inherited genetics, MBTI type, traits, social class, fame, reputation, pets and family crest
- Careers, schooling, love, marriage, children, places, courts, wills, heirlooms, sports and Olympics, politics and war declarations
- Dynasty continuation as heir, relative, or acquaintance with family tree and dynasty traits
- Narrative, Household and God modes plus repeat-year, pinned actions, autoplay goals and a built-in Guide advisor
- Optional Claude integration for character chat, advice, play-for-me and story prose

## Tags

- life-sim
- simulation
- text-based
- historical
- dynasty
- single-player
- browser
- open-source

## Controls

- Mobile controls: Supported
- Motion controls: Not established
- Gamepad: Not established
- Keyboard/mouse: Supported

## Player modes

- Human players: 1
- Modes: single-player

## Technologies

- **JavaScript** — language ([evidence](https://raw.githubusercontent.com/Mofferato/tempora/main/build.js))
- **HTML5** — rendering ([evidence](https://raw.githubusercontent.com/Mofferato/tempora/main/src/shell.html))
- **CSS** — rendering ([evidence](https://raw.githubusercontent.com/Mofferato/tempora/main/build.js))
- **Web Audio API** — audio ([evidence](https://raw.githubusercontent.com/Mofferato/tempora/main/src/sound.js))
- **Node.js 18** — build ([evidence](https://raw.githubusercontent.com/Mofferato/tempora/main/package.json))

## Reconstructed prompt

Build a free open-source single-file browser life simulator spanning 10,000 BC to the far future with eleven eras, 22 lands, year-by-year ageing, genetics, personalities, careers, relationships, settlements, migrations, wars, politics, dynasties, household and god modes, autoplay, procedural era music, and offline play.

## Source evidence

- Repository title and description present Tempora as a life simulator across twelve thousand years: born 10,000 BC to far future, living one year at a time in a world of dynasties, migrations, wars and politics; free, open source, one HTML file. ([source](https://github.com/Mofferato/tempora))
- Play link points to https://mofferato.github.io/tempora/ with autosave in browser; offline play by downloading index.html; platform server adds accounts and cloud saves. ([source](https://github.com/Mofferato/tempora))
- Features list documents eleven eras across 22 lands, living world, genetics, MBTI, class, fame, pets, school, careers, love, marriage, places, courts, wills, sports, Olympics, politics, era-appropriate communication, stat-change feedback, autoplay, Guide, Claude integration, dynasties, three modes, and procedural era music. ([source](https://github.com/Mofferato/tempora))
- Playable page at mofferato.github.io/tempora/ opens the actual game shell (Tempora header with Age +1 control), not just a repo or promo page. ([source](https://mofferato.github.io/tempora/))
- Game is single-player life/dynasty play: live one year at a time and continue through children, relatives or anyone known; Community tab is profiles/posts, not multiplayer gameplay. ([source](https://github.com/Mofferato/tempora))
- UI is pointer/click driven with buttons and tabs; sound module listens to pointerdown and keydown; shell includes viewport-fit mobile meta; mobile screenshot shows responsive phone layout with the same Age flow. ([source](https://raw.githubusercontent.com/Mofferato/tempora/main/src/sound.js))
- No gamepad, accelerometer, gyroscope, or on-screen joystick documented; no explicit touch-control statement beyond tap-friendly browser UI and responsive layout. ([source](https://github.com/Mofferato/tempora))
- package.json declares the tempora package, homepage, MIT license, build/test/start scripts, and Node \>=18 engine requirement. ([source](https://raw.githubusercontent.com/Mofferato/tempora/main/package.json))
- build.js bundles ordered src/\*.js modules plus CSS and shell.html into a single self-contained index.html with zero install dependencies. ([source](https://raw.githubusercontent.com/Mofferato/tempora/main/build.js))
- sound.js synthesizes per-era music and effects with the Web Audio API and no audio files; first click unlocks audio. ([source](https://raw.githubusercontent.com/Mofferato/tempora/main/src/sound.js))
- server/server.js is a plain-Node (no framework) platform server using http, crypto scrypt, HttpOnly cookies, server-sent events, and the official Anthropic SDK for an optional Claude proxy. ([source](https://raw.githubusercontent.com/Mofferato/tempora/main/server/server.js))
- No catalog entry matches this game: grep over games/\*/readme.json and README.md finds no Mofferato/tempora slug, title, or repository reference; catalog holds 36 prior game reports used only as score calibration. ([source](https://github.com/Mofferato/tempora))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 85/100: I started as a Natufian forager and died as an Egyptian blacksmith with three kids and a tax bill. Twelve thousand years of history kept moving without me and I could not stop pressing Age.
- 60/100: A fascinating dynasty machine buried in menus and stat bars. The systems run deep but evenings blur into the same loop of work, marry, age, inherit.
- 100/100: The most ambitious one-file life sim I have played. Eleven eras, real migrations, wars I could declare myself, then my granddaughter carried on. Nothing else does this.

## Links

- [Source repository](https://github.com/Mofferato/tempora)
- [Playable game](https://mofferato.github.io/tempora/)
