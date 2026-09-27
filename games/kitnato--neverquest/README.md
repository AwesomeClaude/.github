# neverquest

[View source](https://github.com/kitnato/neverquest)

| Overall rating | Screenshot score |
| :---: | :---: |
| **45/100** | **30/100** |

<details>
<summary>Read the scoring rationale</summary>

### Overall rating

Far from AAA (no 3D world, voice, cinematics, multiplayer or live-ops scale; monochrome text UI only), but the deepest systems scope in the catalog: 8 attributes, 15+ derived stats, 9 caravan crew roles, multiple weapon classes, ailments, gems/relics, 100+ quests, indefinite stages and retirement metagame across ~591 tracked files of TypeScript/React. Most relevant comparators: Turbo Kart Rally (40 overall, complete indie loop with menus/HUD but one track and simple arcade systems) and Kart Royale (50 overall, ~60k-line 3D tech demo with one 1.6km track) — Neverquest exceeds both on mechanics breadth, build variety and long-tail progression, but trails both badly on visual scene rendering and moment-to-moment action feel. Above Neural Sight (30 overall, tiny 4-scene shooter prototype) on scope and completeness. Evidence gaps: judged from gh api source plus 5 still screenshots only; did not play the live build, so playability, balance, pacing and performance are unverified from stills and code alone.

### Screenshot score

Visible gameplay frames show a clean, coherent monochrome dashboard UI (health/stamina bars, stat grids, gear cards, monster panels, progress meters) that is legible and consistent, but there is no rendered 3D scene, lighting, environment or character art — only icons and bars. Against catalog calibration (Kart Royale, Turbo Kart Rally and Neural Sight all 70/100 for coherent in-engine 3D worlds with HUD, scenery and composition), Neverquest ranks far lower on polish, composition and scene detail despite its UI tidiness. Stills reveal nothing about motion or combat feel, so no animation or game-feel credit is inferred.

</details>

## At a glance

| Detail | Value |
| --- | --- |
| Documented creation models | Not established |

## Screenshots

![Inspected full combat frame at Coast of the Screams stage 33: player panel with health 431/463 DODGED, stamina, attack/recovery timers, six-stat grid, Titanium Halberd / Tasset of Destitution / Alchemical Wall gear, Butchery mastery 69/78; monster panel for Blighted Scoundrel 135/696 with attack timer and ailment meters; essence 864/1,444 progress. Densest gameplay UI, clearly the game's own output.](https://raw.githubusercontent.com/kitnato/neverquest/main/public/nq-screenshot-4.png)

Inspected full combat frame at Coast of the Screams stage 33: player panel with health 431/463 DODGED, stamina, attack/recovery timers, six-stat grid, Titanium Halberd / Tasset of Destitution / Alchemical Wall gear, Butchery mastery 69/78; monster panel for Blighted Scoundrel 135/696 with attack timer and ailment meters; essence 864/1,444 progress. Densest gameplay UI, clearly the game's own output.

![Inspected ranged combat frame in Shrouded Canyon vs Flatulent Myrmidon (1,142/1,170 HP, 1.19s attack): player low-health tooltip 'The meaning of life is that it ends', exhausted stamina, stat grid, Brass Caltrop / Pallium of Cinders gear, essence 2,401 with 8,089/8,940 progress. Same monochrome runtime UI as above; game's own output.](https://raw.githubusercontent.com/kitnato/neverquest/main/public/nq-screenshot-3.png)

Inspected ranged combat frame in Shrouded Canyon vs Flatulent Myrmidon (1,142/1,170 HP, 1.19s attack): player low-health tooltip 'The meaning of life is that it ends', exhausted stamina, stat grid, Brass Caltrop / Pallium of Cinders gear, essence 2,401 with 8,089/8,940 progress. Same monochrome runtime UI as above; game's own output.

![Inspected caravan hub frame: health 90/90 and stamina 20/20 bars, combat stats, Sordid Claymore / Soiled Helm / Weak Stormshield gear; hired Merchant plus crew for hire (Medic 20, Tailor 35, Blacksmith 50 essence, locked stages 15-27). Management UI, game's own output.](https://raw.githubusercontent.com/kitnato/neverquest/main/public/nq-screenshot-2.png)

Inspected caravan hub frame: health 90/90 and stamina 20/20 bars, combat stats, Sordid Claymore / Soiled Helm / Weak Stormshield gear; hired Merchant plus crew for hire (Medic 20, Tailor 35, Blacksmith 50 essence, locked stages 15-27). Management UI, game's own output.

![Inspected journal overlay in Cellar with 929,811 essence: completion bonuses, Conquests/Routines/Triumphs tabs, 2/103 progress, quest list (Hoarding I/II, None shall pass, Bloodlust tiers) with +1% rewards. Menu/overlay over live stats, not active combat.](https://raw.githubusercontent.com/kitnato/neverquest/main/public/nq-screenshot-5.png)

Inspected journal overlay in Cellar with 929,811 essence: completion bonuses, Conquests/Routines/Triumphs tabs, 2/103 progress, quest list (Hoarding I/II, None shall pass, Bloodlust tiers) with +1% rewards. Menu/overlay over live stats, not active combat.

![Inspected sparse start frame: dark header with neverquest v1.0.0 logo, two empty cards ('???' and 'The darkness stirs'), large blank white area. Near-blank initial frame, discounted as non-representative of gameplay depth.](https://raw.githubusercontent.com/kitnato/neverquest/main/public/nq-screenshot-1.png)

Inspected sparse start frame: dark header with neverquest v1.0.0 logo, two empty cards ('???' and 'The darkness stirs'), large blank white area. Near-blank initial frame, discounted as non-representative of gameplay depth.

## Play

- Open https://kitnato.github.io/neverquest/ in a browser (or npm install, npm start, then http://localhost:5173).
- In the wilderness, choose attack to engage the lurking monster and trade automatic blows on your attack rate while managing health and stamina.
- Retreat to disengage, or fight until one side dies; loot essence and items on kills, watch for boss monsters every few stages.
- When the stage is cleared, collect loot, rest, and travel to the caravan to trade with the merchant and hire crew (medic, tailor, blacksmith, fletcher, mercenary, alchemist, occultist, witch).
- Spend essence on attribute ranks, train skills via the mercenary, craft gear via blacksmith/fletcher, socket gems, expand encumbrance via tailor, and complete journal conquests/routines/triumphs.
- Death rebirths you a stage lower keeping items and power level but losing unspent essence — scavenge your corpse; retire later for a fresh start with mighty perks toward the true ending.

## Mechanics

- Automatic attack-rate combat with retreat/disengage, recovery lockout, stamina exhaustion and dodge/block/parry mitigation
- Health/stamina reserves with regeneration, ailments (bleeding, blight, poison, stagger, stun, thorns) and deflection
- 8 essence-bought attributes (agility, dexterity, endurance, perception, speed, strength, vigor, vitality) raising power level
- Melee (piercing/slashing/blunt/two-handed), ranged with distance/range, shields with stagger, armor protection and burden costs
- Skills, masteries (butchery, cruelty, finesse, marksmanship, resilience, might) and traits/retirement perks
- Wilderness stages with progress meters, rage/frenzy, bosses dropping gems and relics
- Caravan crew economy: merchant buyback, medic healing/bandages, tailor encumbrance, blacksmith/fletcher crafting, alchemist transmutation, occultist respec, witch potions
- Inventory with weight/encumbrance, knapsack, gear comparison indicators, gem socketing, relic infusions, munitions
- Quest journal with conquest/routine/triumph classes and completion bonuses, plus death corpse-scavenging and phylactery resurrection

## Tags

- incremental
- text-based
- action-rpg
- browser-game
- idle
- roguelite
- souls-like
- react
- typescript

## Reconstructed prompt

Build neverquest, an irreverent text-based incremental action RPG as a React/TypeScript web app: automatic attack-rate wilderness combat with stamina, ailments and boss stages; essence loot economy; caravan hub with merchant, medic, tailor, blacksmith, fletcher, mercenary, alchemist, occultist and witch; deep attributes/skills/masteries/traits/quests/retirement progression with indefinite stages and a true ending; clean monochrome Bootstrap UI using game-icons.net icons, deployable to GitHub Pages.

## Source evidence

- Repo is neverquest: 'An irreverent text-based incremental action role-playing game', TypeScript, homepage https://kitnato.github.io/neverquest/, 9 stars, 1 fork, CC BY-NC-SA 4.0. ([source](https://github.com/kitnato/neverquest))
- README lists gameplay manual, 5 screenshots, local setup (Node 18, npm install/start, Vite localhost:5173), and design goals: always something to do, no arbitrary waits, frequent impactful decisions, high build variety. ([source](https://github.com/kitnato/neverquest/blob/main/README.md))
- Warren Spector appendix names influences (Diablo, Dark Souls, Progress Quest, Kingdom of Loathing, Candy Box, NGU Idle) and pitch: text-based Diablo/Dark Souls hybrid, funny web app. ([source](https://github.com/kitnato/neverquest/blob/main/README.md))
- Manual documents attack-rate wilderness combat, engaging/retreating, recovery lockout, stamina burden, boss intervals, loot/collect/rest/travel loop, caravan crew, death corpse-scavenge and retirement. ([source](https://github.com/kitnato/neverquest/blob/main/source/data/manual.md))
- Manual details 8 attributes, 15+ derived statistics (DPS, bleed/block/critical/deflection/dodge/execution/parry/protection/range/recovery/stagger/stun), gear classes, ailments and relics. ([source](https://github.com/kitnato/neverquest/blob/main/source/data/manual.md))
- package.json v1.1.2: React 18, Recoil, Bootstrap, Vite, TypeScript; keywords include incremental, souls-like, rogue-lite; repo tree ~591 files dominated by TypeScript (~700k chars). ([source](https://github.com/kitnato/neverquest/blob/main/package.json))
- Screenshots referenced in README map to public/nq-screenshot-1..5.png (start, caravan, ranged, melee, quests). ([source](https://github.com/kitnato/neverquest/blob/main/README.md))
- Active multi-year project created 2021-06-13, pushed 2024-06-25, with quest revamps, traits, cheats and scaling fixes in recent commits. ([source](https://github.com/kitnato/neverquest/commits/main))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 85/100: Fictional illustrative review: three years in and my Titanium Halberd build still surprises me — dodging a Blighted Scoundrel at 36% block chance while Butchery ticks to 69/78 is unreasonably tense for black-and-white buttons.
- 65/100: Fictional illustrative review: the caravan loop is clever and the journal's 100+ quests kept me grinding stages, but staring at health bars for hours made me miss the kart racers' sunsets — great spreadsheets, zero spectacle.
- 100/100: Fictional illustrative review: a funny text Diablo that runs anywhere and never wastes my time — hired the Medic, socketed gems, retired for perks, chased the true ending. The deepest browser incremental I have ever played.

## Links

- [Source repository](https://github.com/kitnato/neverquest)
- [Related link](https://kitnato.github.io/neverquest/)
- [Related link](https://github.com/kitnato/neverquest/blob/main/source/data/manual.md)
