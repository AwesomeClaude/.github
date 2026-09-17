# SparkyGames — The Nine Lives of Ash — Reverse-Engineered Game Dossier

> Method: **no checkout**. All analysis via GitHub REST API (`api.github.com/repos/phirogue/SparkyGames`) + `raw.githubusercontent.com` file reads + commit history. No `git clone`.
> Repo: https://github.com/phirogue/SparkyGames
> Analyzed: 2026-09-17 | Branch: `main` | HEAD at analysis: `3b370c0` (2026-09-01)
> Engine: Godot 4.4, GDScript ~1.17M bytes, Python ~299k (tools), TeX ~301k (novel), project `game/project.godot` v0.1.0, portrait 720x1280.

---

## 1. What this game is (1-paragraph pitch)

**The Nine Lives of Ash** is a mobile-first, offline, single-player **story-driven roguelite deckbuilder**. You are **Ash**, a 15-year-old (old, retired) black cat familiar of the murdered witch Elspeth, spending your nine lives to solve her murder in the fog-bound city of **Hollowmere**. Runs ("prowls") are 3–5 minutes. The inversion: **you don't draw actions — you equip 5 skills and draw fuel** (energy cards in 4 humours). Combat + 5 investigation minigames + quest/story choices + death-as-currency (Hollow Court). Current build: playable prologue (4 encounters as one continuous prowl) + Chapter 1 content in design/data; free Chapters 0–1 + tip jar model.

## 2. Source-code architecture (from API tree walk)

```
game/
  core/       pure rules, RefCounted only, no Node/FileAccess/global RNG
    combat_state.gd (~40k), catalog.gd (~64k), rules.gd, case_state.gd,
    crossing_state.gd, stitch_state.gd, ward_state.gd, testimony_state.gd,
    lattice_state.gd, minigame.gd, prowl_script.gd, quest_gate.gd,
    core_rng.gd, command_log.gd, achievement_tracker.gd, chronicle.gd
  services/   ONLY layer touching disk: content, save, prose
  scenes/     UI; game.gd decides what comes next
  ui/         shared widgets + layout contract UITheme
  data/       JSON content + tuning, stable string ids:
    rules.json, skills.json (15), enemies.json (16), encounters.json (26),
    quests.json (~94k), crossings.json, wards.json, lattices.json,
    testimonies.json, stitch_charts.json, patch_shapes.json, lessons.json,
    minigame_tutorials.json, achievements.json, case.json, favors/guilds/
    music/sfx/energy_cards/environments
  story/      prose: prologue/ (01_the_gift … 05_the_parlor + index + interludes),
              world/ canon, interface.json (~23k, all player-facing strings)
  tests/      unit + tour + simulate.gd (19.2k bot fights/pass) + chaos fuzzer
docs/
  architecture/ HOW IT FITS TOGETHER + change-map.json
  design/ core-gameplay.md, minigames.md, bestiary.md (generated), balance-notes.md,
          world-bible.md, story-*, art-*, death-and-lives.md, monetization.md, tech-stack.md …
  research/ dated read-only reports | brainstorm/ rejected ideas
tools/ verify.py, kb_check.py, tour_all.py, prose_telling.py, batches/
play/ double-click launchers from parts.json | assets/ art library + archive
screenshots/ tour output (untracked) + reference/ (tracked, 2 files)
novel/ story-bible (authoritative for canon since 2026-08-16)
```

Key engineering rules (from `CLAUDE.md`, 30 laws): seeded `CoreRng` + `CombatState.do_command()` + `CommandLog` = deterministic tests/sims/replays; prose lives in JSON never `.gd`; tuning numbers live in `data/rules.json` with fallback defaults in `core/rules.gd`; `Catalog.validate()` gates content; tour must photograph EVERY quest (law 17); layout calibrated not guessed (`UITheme.PAGE_MARGIN`, zone templates); type floor 22px (body 30).

Activity: 103 commits, created 2026-07-29, last push 2026-09-01. 0 stars/0 forks. Recent commits: Hollow Court death filming, chapter finale First File card, 299 tests green, 16.5k fuzz runs clean, 8 new skills + 3 new enemies (Doorman, Left Glove, Votive Stub).

## 3. Screenshots analysis (only tracked `screenshots/reference/`)

`screenshots/` is **generated/untracked by design** (200MB+/tour, 903MB history) — `prologue/` via `godot --path game -- --tour`, `quests/` via `tools/tour_all.py`. Only 2 curated files are committed:

### 3.1 `screenshots/reference/02_title.png` (326 KB, 506x900 approx)
- Black full-bleed. Ornate ivory serif logotype: **"The Nine Lives of Ashcat"** (in-game title now "The Nine Lives of Ash" — asset predates rename).
- Black cat silhouette in profile, red/orange neckerchief, tail becomes flourished thread ending in orange yarn-ball + needle charm.
- Small orange 4-point star accent. Bottom: grey italic "— tap to begin —". Top-left hamburger.
- Read: storybook-gothic, wry-cute, premium-casual. No red-neckerchief on Ash in canon (prose fix owed — he tears it in `sc_collar`).

### 3.2 `screenshots/reference/battle.png` (239 KB)
- Portrait battle page with stitched-dashed border, parchment texture.
- Top: environment plates "The Rooftops, Dusk" + "Last light: sunbeams on turns 2 and 4 return a spent card."
- Enemy card right: "The Vole" (0/5 HP bar dashed), framed portrait (vole on rooftop chimney at dusk — AI art, painterly), "Next: Hold Very Still — 0 damage".
- Center modal: "The Vole: dealt with." + orange [Continue] — victory flow.
- Mid: dimmed combat log behind modal, single energy chip "I / Ferocity".
- Bottom tray: [spent SCRATCH] greyed, [POUNCE x2] with 2 red pips (charge-to-power UI), action row [End Turn (orange)] [Concentrate x2] [Slip Away (navy)]. Corner X-stitches.
- Read: ≤3 taps/turn, big type (title 44 / body 30), telegraphed intents, one-thumb portrait — matches design docs exactly.

No other screenshots committed. Full visual verification requires running the tour locally.

## 4. Reverse-engineered prompt (what prompt would regenerate this game)

```text
Build a portrait, one-handed, offline-first mobile roguelite deckbuilder in Godot 4 GDScript
called "The Nine Lives of Ash".

Premise: You are Ash, a 15-year-old retired black cat familiar. Your witch Elspeth
was murdered behind a locked door in Needle Lane. Spend your nine lives solving it
in Hollowmere — a fog gaslamp city on a black lake (the Mere), split into day-side
and night-side by a sewn seam (the Hush) that cats can see. Tone: wry-cute, low-text,
precise old-cat report voice. Never narrate mechanics in story voice; never future-tell.

Core inversion: player equips 5 skills (MOBA bar, big art) and draws only ENERGY fuel.
Energies: Ferocity (red/body), Guile (green/wit), Shadow (black/stealth),
Moonlight/Mysticism (silver/wild, rare, hers). 15-card starter all value-1;
spent energy NEVER reshuffles (deck = run clock). Hand 5, opening 3, 1 draw/turn,
3 paws (AP)/turn, loadout 5, 2 Concentrates/run. Free weak instinct Scratch always
available. Charge-to-power: feed energy onto cards pip-by-pip, power persists.
No banking, no discard (removed as traps). 14+Scratch skills across humours,
each humour has a job (Ferocity hurts, Guile sustains, Shadow refuses, Moonlight
does the impossible).

Combat: turn-based vs telegraphed intent cycle (health / hand-steal / skill jam+burn /
self block+heal / pierce). 3 pressures. Enemies: wisps, chained dog, geese, rag-wraiths,
candle-golems, Drowned, Tallowman (boss), the Unpicked (60HP scripted unbeatable).
Approaches (Stalk/Ambush/Case/Ward, flat 2-energy off-spool). Masked intents until
familiar. Night-presses +2 from turn 8. Slip Away always (enemy full move lands +
half satchel forfeit); no_retreat / hp_floor / doom_turn / withdraw_after scripted
fights. Death only at mortal:true beats; ordinary loss = Hollow Court REFUSED
(10% filing fee + enemy Grudge); true death = Toll 25% + satchel spill + canon
death scene. World remembers.

Structure: prowl = 2-4 encounters, Press On (+25% loot) or Slip Away (bank half).
Between: quest board, Magpie Exchange shop (Gleam run-currency + Favor-knots meta),
Mantel long-rest loadouts only. 5 minigames reusing same deck/paws: Seam&Stitch
(Slitherlink), Testimony (Ace Attorney press/present), Patch the Ward (polyomino
draw-from-spool), The Unpicking (Mikado stack), Long Way crossing (pay-your-way
decisions). Story choices set mechanical flags. 3-5 min/run. Free Ch0-1 + tip jar,
Ch2 paid. No PvP ever, no ads, no timers, plane-playable.

Tech: Godot 4.4 mobile renderer, pure core/ (RefCounted, seeded RNG, command log),
JSON data w/ stable ids + Catalog.validate, versioned 3-book saves, headless CI +
GUT + 19k bot sims + screenshot tour that must be READ. UI: storybook stitched
parchment, fixed zone templates, fitted type (44/34/30/26/22), AI art (gpt-image-2)
with reference-locked characters, strict style.
```

## 5. How to play (current Windows build)

1. Double-click `run_game.bat` (needs Godot at `C:\Users\yurim\tools\godot\`) — phone-shaped 506x900 window. Or open `game/` in Godot editor, F5.
2. Title → tap to begin → prologue: 4 encounters as one continuous prowl (vole hunt tutorial → wisp → dog → wraith lesson → parlor mortal).
3. Per fight: optionally pick Approach (pay 2 off spool). Each turn: draw to 5 → tap skill → feed energy chips (1 paw per placement) until pips full → tap skill again to fire (or auto-pay remainder) → End Turn. Watch enemy "Next:" intent. `Concentrate` (give whole turn, will back 1 spent card), `Slip Away` (flee) below tray.
4. After each fight: Press On (deeper, richer) or Slip Away (bank half satchel). Death at mortal beat spends a life via Hollow Court; ordinary loss = REFUSED + fee.
5. Between prowls: Mantel (re-fit 5-skill loadout + deck), quest board, Magpie shop, journal/case board, minigames when offered.
6. Dev shortcuts: `godot --path game -- --scene dev` (jump any screen/fight/prowl/minigame/save), `--tour` screenshots, `--scene stitch:<id>` etc.

## 6. Game mechanics used (catalog)

- Inverted deckbuilder (skills equipped × energy drawn) + wild-resource (Moonlight)
- Action points (Paws=3) + charge-to-power persistent windup + slow-draw economy
- Telegraphed intent cycles + masked intents (familiarity unlocks) + pierce/jam/burn/block/heal intent vocabulary
- Exhaustion clock (no reshuffle) + limited charges/adventure + free instinct fallback
- Push-your-luck delve (Press On ×1.25 / Slip Away −50%) + visible odds omens
- Approach draft (initiative-as-choice) + environment cost_mods + sunbeam/alarm tiles
- Scripted fights (hp_floor/doom_turn/withdraw_after/no_retreat) + night-presses escalation
- Death economy (lives-spent-never-taken, Toll/Refusal, Grudge buffs, satchel spill/reclaim)
- Dual currency (Gleam + Favor-knots) + shadow-pocket inventory (9 moon-phased slots) + Magpie deck-tuning shop
- Case board (evidence/leads/threads) + quest gates + consequential choices + canon deaths
- 5 minigames on shared resources (Slitherlink / Ace Attorney / Patchwork-push-luck / Mikado / pay-path traversal)
- Fate-deck variance-with-memory (no raw dice) + bot-simmed balance + deterministic seeded replays
- Cat-behavior verbs as systems (Purr channel, Loaf anti-theft+stun, Bask, Scratch props, Shelf Justice, Zoomies, Slow Blink, Gifts, Catnap/Dream-fragments)

## 7. Tags

`roguelite-deckbuilder` `card-battler` `story-driven` `cozy-gothic` `cat-protagonist`
`murder-mystery` `detective` `fantasy` `original-IP` `mobile-portrait` `one-handed`
`offline-first` `single-player` `3-5-minute-runs` `godot-4` `gdscript` `json-driven`
`indie` `free-with-tip-jar` `no-ads` `wry-cute` `low-text` `ai-assisted-art` `minigames`
`push-your-luck` `resource-management` `investigation`

## 8. Rating: **AA (of A → AAA scale)**

- **A = prototype/hobby** (core loop works, placeholder art, <1h content)
- **AA = strong indie-vertical-slice** (playable arc end-to-end, real art direction, tested+balanced systems, publishing path started, not yet content-complete/live-ops)
- **AAA = full commercial launch** (store-live, complete chapters, localization, accessibility, analytics, marketing)

Verdict **AA**: playable prologue end-to-end in-engine + 299 green tests + sim/fuzz gates + curated art + economy/shipping scaffolding (export presets, privacy/store drafts) + novel-grade world bible. Deduct from AAA: Chapter 1 still in design/data, no store listing live, 3 economy exploits spec'd-not-built, harness gaps noted in ship-review, tour output untracked (can't verify all quests remotely), 0 external players/stars.

## 9. Simulated user reviews (clearly synthetic — repo has 0 stars, no store page)

### ★★★★★ 5/5 — "Slay the Spire meets a cat detective novel" — @MereFogWatcher (roguelite veteran)
> 40 prowls in on the Windows build. The energy-not-actions flip sounded like a gimmick and it's the whole reason it works on phone — I read 5 cards once and then just PLAY. Pounce math is tight, Bite threading a guard feels illegal. Lost to the Captain's pierce because I turtled like it was StS — lesson learned. Story beats every run without slowing the 4-minute loop. Tip jar day one.
> *Playtime: ~12h (prowls + sims) | Build: prologue*

### ★★★★☆ 4/5 — "Cozy, clever, wants a undo button for my heart" — @CozyQuestMum (cozy/mystery player)
> Ash is the best narrator since my last visual novel. Slow blinking at a goose to avoid a fight?? Loafing through theft?? I adore it. Docking one star because the Unpicking lattice had me staring for 90 seconds with no clue what "no thread over it" meant until the ? replay, and Moonlight economy is STINGY — three cards and the shop wants double. Battle UI text is big and readable though, huge plus on my small phone.
> *Playtime: ~5h | Build: prologue + Ch1 quests*

### ★★★☆☆ 3/5 — "Brilliant engine, bring patience" — @BalanceGoblin (systems tinkerer)
> As an engine it's A+: deterministic seeds, JSON everything, bot sims I can rerun — respect. As a game RIGHT NOW it's a prologue + promise. Four fights and then you're replaying for Gleam while Ch1 lands. Crossing boards ate my spool alive pre-8/16 patch, better now. If you love Hades structure talk and cat jokes you'll wait happily. If you want 20h today, wishlist and come back at Ch2 paid drop.
> *Playtime: ~8h | Build: main @3b370c0*

Average synthetic: **4.0/5**

## 10. Links collected

- Repo: https://github.com/phirogue/SparkyGames
- API root: https://api.github.com/repos/phirogue/SparkyGames
- README (raw): https://raw.githubusercontent.com/phirogue/SparkyGames/main/README.md
- Rules/contract: https://raw.githubusercontent.com/phirogue/SparkyGames/main/CLAUDE.md
- Design — core loop: https://raw.githubusercontent.com/phirogue/SparkyGames/main/docs/design/core-gameplay.md
- Design — minigames: https://raw.githubusercontent.com/phirogue/SparkyGames/main/docs/design/minigames.md
- Design — world: https://raw.githubusercontent.com/phirogue/SparkyGames/main/docs/design/world-bible.md
- Design — bestiary (generated): https://github.com/phirogue/SparkyGames/blob/main/docs/design/bestiary.md
- Data — tuning: https://raw.githubusercontent.com/phirogue/SparkyGames/main/game/data/rules.json
- Data — skills: https://raw.githubusercontent.com/phirogue/SparkyGames/main/game/data/skills.json
- Data — enemies: https://raw.githubusercontent.com/phirogue/SparkyGames/main/game/data/enemies.json
- Data — encounters: https://raw.githubusercontent.com/phirogue/SparkyGames/main/game/data/encounters.json
- Engine config: https://raw.githubusercontent.com/phirogue/SparkyGames/main/game/project.godot
- Monetization: https://raw.githubusercontent.com/phirogue/SparkyGames/main/docs/design/monetization.md
- Tech stack: https://raw.githubusercontent.com/phirogue/SparkyGames/main/docs/design/tech-stack.md
- Screenshots README: https://raw.githubusercontent.com/phirogue/SparkyGames/main/screenshots/README.md
- Reference shots: https://github.com/phirogue/SparkyGames/blob/main/screenshots/reference/02_title.png · https://github.com/phirogue/SparkyGames/blob/main/screenshots/reference/battle.png
- Latest commit: https://github.com/phirogue/SparkyGames/commit/3b370c0e21522c2fc496295e25e650443a070aac
- Owner: https://github.com/phirogue

---
*Generated without checkout (API-only). Reviews in §9 are synthetic illustrations, not store reviews. Rating AA = indie vertical slice, not commercial AAA.*
