# Deep Dive

[Play the game](https://deep-dive-rosy.vercel.app) · [View source](https://github.com/chichiroxursox-droid/deep-dive)

| Overall rating | Screenshot score |
| :---: | :---: |
| **50/100** | **55/100** |

<details>
<summary>Read the scoring rationale</summary>

### Overall rating

Excluding the target, closest comparators are Kart Royale (50, complete polished single-track 3D loop), neverquest (45, deepest catalog systems scope but text-only), Wilderness (44, ambitious 3D voxel survival with no inspectable screenshots and dead demo), and moorestech (64, catalog top with broad verified systems and dense 3D HUDs). Deep Dive sits at 50 alongside Kart Royale: it proves more breadth than Wilderness (8 real-mechanism labs, live tokenizer plus train-in-browser LM, 3D hub plus fully keyboard-accessible Map mode, live static deployment, unit-tested logic) with six inspected first-party frames, but its moment-to-moment play is gentler than a racer and its low-poly station is simpler than moorestech or the kart titles, and source/docs cannot prove performance, balance, or late-game depth.

### Screenshot score

Four inspected 3D frames (Next Word Machine, station, corridor, token goggles) show coherent stylized low-poly scenes with clean composition, readable signage, and full HUD hints; the Next Word Machine is the densest gameplay evidence. Below Kart Royale/Turbo Kart Rally/Neural Sight (70) and OSRS Tower Defense (65) on geometric detail, lighting richness, and scene density, roughly level with Taipo (55) but cleaner, and well above flat DOM games such as 2048 (45) and Beachy Beachy Ball (35). Lesson UI and map-list frames discounted as non-3D gameplay. Stills cannot prove motion, performance, or feel.

</details>

## At a glance

| Detail | Value |
| --- | --- |
| Repository created | 26 Sep 2026 · 17:56 UTC |
| Added to catalog | 27 Sep 2026 · 06:20 UTC |
| Last updated | 27 Sep 2026 · 06:20 UTC |
| Documented creation models | Not established |

## Screenshots

![Deep Dive gameplay](screenshots/f52e6b90dee9f31f00757d20b3a8c080fa235eb52fc1250f4a10c7da80e60f31.png)

Inspected 1440x900 frame: diver from behind facing a 5-tube Next Word Machine; balls piling in tubes labeled same 13%, admira(l) 5%, (b)ottom 3%, rate 3%; wall placard reads 'The captain looked at the \_\_' with real-odds sampling note; glowing lesson console at right; WASD/E/F hint bar and Map/Graphics buttons visible. Densest gameplay evidence, game's own runtime output.

[Original screenshot](https://raw.githubusercontent.com/chichiroxursox-droid/deep-dive/main/docs/next-word-machine.png)

![Deep Dive gameplay](screenshots/5b4875305f7b82455a92b75a4f3509d7730a4967129a9ede8f1f0238188d4b5d.png)

Inspected 1440x900 frame: third-person diver in orange suit with gold helmet on sand facing DEEP DIVE STATION entrance; Welcome diver signboard, Station Map board, beach balls, kelp, light rays; DIVER'S LICENSE 1-5 tracker top-right, WASD/Shift/drag/E/F hint bar bottom-left. Game's own runtime output.

[Original screenshot](https://raw.githubusercontent.com/chichiroxursox-droid/deep-dive/main/docs/station.png)

![Deep Dive gameplay](screenshots/312a5b2a7faed8fe646e877cdc7ba3a6a150f4a39d61e404a0fc4136c5c6ecac.png)

Inspected 1440x900 frame: diver centered in white-tiled corridor with blue runner rug, pastel lab doors both sides, hanging signs for Lab 1 Token Reef, Lab 2 Guessing Machine, Lab 3 Backpack, Lab 4 Robot Chef; license tracker and controls hint bar visible. Game's own runtime output.

[Original screenshot](https://raw.githubusercontent.com/chichiroxursox-droid/deep-dive/main/docs/corridor.png)

![Deep Dive gameplay](screenshots/8dc9cd2397a50e27def747f0c221c6c60991570bebbd2970e4db0cf868733be2.png)

Inspected 1280x800 frame: same corridor with Token goggles on; banner reads every sign is split into tokens; door signs repainted as colored chunks (Fact/Check/Lagoon, Tool/box); Token goggles active button plus Map/Graphics buttons. Shows live tokenizer overlay in 3D, game's own runtime output.

[Original screenshot](https://raw.githubusercontent.com/chichiroxursox-droid/deep-dive/main/docs/goggles.png)

![Deep Dive gameplay](screenshots/d9d7ec0b67839e1d90d898cbffbf20b7a81c35cf47fefccc2a4099559e423f5c.png)

Inspected 1280x800 lesson UI: Lab 1 Token Reef card showing real split of 'strawberry' into st/302, raw/1618, berry/19772 token chips after a correct guess of 3, with counting-letters explanation and Next button. Game's own 2D lesson output, not 3D gameplay.

[Original screenshot](https://raw.githubusercontent.com/chichiroxursox-droid/deep-dive/main/docs/token-reef.png)

![Deep Dive gameplay](screenshots/7d4709b88107b485bb98a191afcb1dcd32d5c088148c8ba6dbc68bcd7c326289.png)

Inspected 1280x800 menu UI: Deep Dive Station Map list with Labs 1-5 plus Diver's License progress (Labs done 2 of 5), Done/Not yet states, Bonus labs section, Walk the 3D station button. Menu screen, not gameplay.

[Original screenshot](https://raw.githubusercontent.com/chichiroxursox-droid/deep-dive/main/docs/map-mode.png)

## Play

- Open https://deep-dive-rosy.vercel.app in a desktop browser with WebGL2; no account needed.
- Walk with WASD, run with Shift, drag to look around; walk up to a glowing console and press E to start its lesson.
- Finish the five core labs (Token Reef, Guessing Machine, Backpack, Robot Chef, Fact Check Lagoon) to earn the Diver's License on the Captain's Deck.
- Press T or the Token goggles button to repaint every sign as GPT-4o tokens; use Map mode for a keyboard-only no-3D path through all labs.
- In Lab 2 watch sampled balls fill the top-5 tubes; in Lab 3 chat with Pip and test what survives the 60-token trough.

## Mechanics

- Third-person 3D underwater station hub: sea floor, airlock lobby, 8-door corridor, Captain's Deck license goal
- Console-triggered lessons (walk up, press E) across 5 core labs plus 3 bonus labs, about 20 minutes
- Token Reef guessing game backed by the live GPT-4o (o200k\_base) tokenizer via js-tiktoken
- Next Word Machine physics toy sampling balls into top-5 tubes from a real in-browser trigram model with temperature dial
- Backpack 60-token context-window simulation weighing chat with the real tokenizer, with pin/discard strategies
- Robot Chef scripted prompt-assembly scoring, Fact Check Lagoon NOAA-linked true/false quiz, Toolbox agent approval steps, Library retraining bias demo, Safe Harbor privacy sorting
- Token goggles overlay re-tokenizing every station sign live; Map mode delivering all lessons as keyboard-only accessible UI
- Diver's License checklist of learned rules; Graphics High/Low switch with auto-low on low-core machines

## Tags

- educational
- 3d
- exploration
- minigames
- sci-fi
- underwater
- single-player
- kids

## Controls

- Mobile controls: Not supported
- Motion controls: Not established
- Gamepad: Not established
- Keyboard/mouse: Supported

## Player modes

- Human players: 1
- Modes: single-player

## Technologies

- **three.js 0.186.1** — rendering ([evidence](https://raw.githubusercontent.com/chichiroxursox-droid/deep-dive/main/package.json))
- **React 19.3.0** — framework ([evidence](https://raw.githubusercontent.com/chichiroxursox-droid/deep-dive/main/package.json))
- **@react-three/fiber 9.8.1** — framework ([evidence](https://raw.githubusercontent.com/chichiroxursox-droid/deep-dive/main/package.json))
- **@react-three/rapier 2.2.0** — physics ([evidence](https://raw.githubusercontent.com/chichiroxursox-droid/deep-dive/main/package.json))
- **TypeScript 7.0.2** — language ([evidence](https://raw.githubusercontent.com/chichiroxursox-droid/deep-dive/main/package.json))
- **Vite 8.3.1** — build ([evidence](https://raw.githubusercontent.com/chichiroxursox-droid/deep-dive/main/package.json))
- **Tailwind CSS 4.3.3** — framework ([evidence](https://raw.githubusercontent.com/chichiroxursox-droid/deep-dive/main/package.json))

## Reconstructed prompt

Build a free 3D browser edugame for ages 10-14 called Deep Dive: a walkable underwater station where each lab bay teaches one chatbot idea with a short robot explanation plus a minigame running the real mechanism (GPT-4o tokenizer, tiny in-browser trigram LM, 60-token context trough, scripted prompting/quiz/agent/privacy games), token-goggles overlay, keyboard-only Map mode, Diver's License finale, Vite+React+three.js static deploy, no accounts or API calls.

## Source evidence

- Repository is a public game repo titled Deep Dive, described as a free 3D browser game for kids 10-14, with a Play link to a Vercel deployment and docs screenshots of the station, corridor, minigames, and modes. ([source](https://github.com/chichiroxursox-droid/deep-dive))
- Game loop: walk a diver through sea floor, lobby, and 8-door corridor; glowing consoles start 5 core labs plus 3 bonus labs; Diver's License finale; about 20 minutes, no account, solo play. ([source](https://github.com/chichiroxursox-droid/deep-dive))
- Lessons run real mechanisms live in the browser: GPT-4o o200k\_base tokenizer, trigram LM with bigram backoff trained on 55,689 words, 60-token context trough, real calculator, NOAA-linked fact checks. ([source](https://github.com/chichiroxursox-droid/deep-dive))
- Keyboard/mouse controls documented on-screen and in screenshots: WASD walk, Shift run, drag look, E use, F kick ball, T token goggles; Map mode verified keyboard-only with Tab/arrows/Space/Enter via scripted Playwright runs. ([source](https://github.com/chichiroxursox-droid/deep-dive))
- Touch explicitly ruled out for the 3D station; phones and tablets are pointed to Map mode instead. No gamepad or motion-control support documented. ([source](https://github.com/chichiroxursox-droid/deep-dive))
- Single-player only: solo kid play, no accounts, no server or database, no multiplayer systems; progress intentionally not saved. ([source](https://github.com/chichiroxursox-droid/deep-dive))
- Stack documented as Vite, React 19, TypeScript, Tailwind 4, three.js with @react-three/fiber, drei, rapier and ecctrl, js-tiktoken; static Vercel deploy; package.json pins three, fiber, drei, rapier, react, vite, typescript, tailwind. ([source](https://raw.githubusercontent.com/chichiroxursox-droid/deep-dive/main/package.json))
- AI disclosure: built with Claude Code directed by the author; no AI at runtime; ElevenLabs used once at build time for narration MP3s. No exact creation model identifiers, so creation\_models left empty. ([source](https://github.com/chichiroxursox-droid/deep-dive))
- Playable deployment link published in README as the official play URL; live-site fetch returned only a JS-shell title, so in-motion playability and performance remain evidence gaps. ([source](https://deep-dive-rosy.vercel.app))
- No catalog match: no existing games/ directory for deep-dive or chichiroxursox-droid; target compared against all prior entries with moorestech (64), Kart Royale (50), neverquest (45), and Wilderness (44) as calibration. ([source](https://github.com/AwesomeClaude/.github/blob/main/README.md))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 85/100: My 11-year-old got the token goggles joke before I did and now explains context windows with backpack metaphors. The Next Word Machine finally made sampling click for her.
- 62/100: Sweet idea and the labs are honest about what is real, but I wanted more game between lessons. Walking the corridor is calm; the minigames carry it.
- 100/100: A kids game that runs a real tokenizer and a real tiny language model in the browser with zero accounts? Instant classroom classic.

## Links

- [Source repository](https://github.com/chichiroxursox-droid/deep-dive)
- [Playable game](https://deep-dive-rosy.vercel.app)
