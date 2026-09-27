# Infinite Craft

[Open the original game link](https://neal.fun/infinite-craft/) — No verified source repository.
[Play the game](https://neal.fun/infinite-craft/)

**Overall rating:** 52/100. Far from AAA: single blank-canvas drag-and-drop loop, no campaign, multiplayer, cinematics, voice, progression economy or live-ops scale; source code not public so performance, balance and backend cost are unverified. Catalog comparison across all 18 listed games: Ashlands (55 overall, ~94k-line 3D RPG systems breadth but zero inspectable screenshots) is the calibration top; Kart Royale (50 overall, ~60k-line complete 3D kart loop with two inspected 70/100 polished frames) and Turbo Kart Rally (40, complete 3D racer) beat it on visual polish, composition and real-time execution; neverquest (45, deepest text-systems scope but monochrome dashboard) is the closest scope analogue. Infinite Craft exceeds neverquest, TypeScript-Blackjack (28, single-table DOM), Top-10 Tension (32, flat quiz UI), Beachy Beachy Ball (25), Taipo (35, single-map typing TD), Neural Sight (30, 4-scene prototype) and curiositY (18, static riddles) on content infinitude, shipped maturity and proven traction: 2024 viral hit on Twitch/YouTube, 100M+ combos claimed, official iOS/Android apps, global shared database. It trails Ashlands on simulated systems depth and both kart racers on scene rendering, but its verified live playability and cultural scale place it just above Kart Royale at 52. Code and stills do not prove performance, fairness or long-term balance.

**Screenshot score:** 32/100. One inspected gameplay frame only; judged from stills without inferring motion. The frame shows the game's own output: white infinite canvas with small pill-shaped text nodes and thin grey link lines, plus a right sidebar discovery list. Clean, coherent and readable minimalist styling, but flat DOM text with no lighting, texture, environment, effects or composed scene. Against catalog calibration it sits with TypeScript-Blackjack (35, clean flat card table), Top-10 Tension (32, flat quiz cards) and neverquest (30, monochrome dashboard), below Taipo (55, pixel-art board with map decor) and far below Kart Royale, Turbo Kart Rally and Neural Sight (all 70 for dense 3D or photographic scenes with HUD, scenery and dynamic framing). Title and logo art discounted.

## Screenshots

![Inspected 457x218 gameplay frame: white infinite canvas covered with small pill nodes such as Peter Griffin, Mickey Mouse, Sea Unicorn, Head-first, Ghost, Aquarium, Red Dragon, Mountain Range and Donald Trump linked by thin grey lines; right sidebar lists Discoveries with emoji rows and search/sort controls; top bars show NEAL.FUN and Infinite Craft logos. Clearly the game's own runtime output, not concept art.](https://upload.wikimedia.org/wikipedia/en/a/aa/Gameplay_screenshot_of_Infinite_Craft%2C_2024.png)

Inspected 457x218 gameplay frame: white infinite canvas covered with small pill nodes such as Peter Griffin, Mickey Mouse, Sea Unicorn, Head-first, Ghost, Aquarium, Red Dragon, Mountain Range and Donald Trump linked by thin grey lines; right sidebar lists Discoveries with emoji rows and search/sort controls; top bars show NEAL.FUN and Infinite Craft logos. Clearly the game's own runtime output, not concept art.

## Play

- Open https://neal.fun/infinite-craft/ in a desktop or mobile browser; no install or account is needed.
- Start with the four base elements Water, Fire, Wind and Earth in the sidebar or palette.
- Drag one element onto the empty canvas, then drag a second element on top of it to combine them (on mobile tap one item then tap a second).
- New results such as Steam from Water plus Fire are added to the sidebar collection for reuse.
- Keep chaining outputs into new inputs, combine an item with itself to scale up, and use sidebar search and sort as the collection grows.
- Use the trash or broom control to clear the canvas without deleting discoveries; use Reset only to wipe all discoveries.

## Mechanics

- Drag-and-drop combination of any two discovered elements on an infinite canvas workspace
- AI-generated results via Llama 2 and Llama 3.1 with emoji assignment for novel pairs
- Server-side recipe database with dedup so the same pair always yields the same result
- First Discovery labeling for the first player worldwide to find an element
- Persistent sidebar inventory of discoveries with search, sort by time, and Discoveries view
- Canvas management: clear workspace without losing collection versus full reset of progress
- Save files, infinite canvas, and import or export of saves in later web and app versions
- Content filter for offensive results with occasional incoherent but amusing outputs

## Tags

- sandbox
- crafting
- puzzle
- browser-game
- ai-generated
- single-player
- casual
- endless
- experimental

## Controls

- Mobile controls: Supported
- Motion controls: Not established
- Gamepad: Not established
- Keyboard/mouse: Supported

## Player modes

- Human players: 1
- Modes: single-player

## Reconstructed prompt

Build Infinite Craft, a browser sandbox crafting game: blank infinite canvas plus sidebar inventory starting with Water, Fire, Wind and Earth; drag any two items together to combine them, call an LLM to invent a new emoji-labeled element for unseen pairs, dedupe via a global recipe database, award First Discovery to the first finder, persist discoveries in local storage with search/sort/clear/reset, filter offensive outputs, and ship matching mobile apps.

## Source evidence

- Infinite Craft is a 2024 sandbox game by Neal Agarwal released January 31 2024 on neal.fun, later on iOS April 27 2024 and Android May 21 2024; genre Sandbox, Mode Single-player ([source](https://en.wikipedia.org/wiki/Infinite_Craft))
- Live page scrape shows the playable UI: Items 0 counter, Discoveries panel, sort-by-time control, trash, clear-canvas, dark-mode, sound, recipes, logo and menu icons, and clear-all confirmation ([source](https://neal.fun/infinite-craft/))
- Gameplay layout has infinite workspace on the left and element list with Discoveries and sorting menu on the right; player clicks and drags elements from the right onto the canvas to combine them ([source](https://www.ign.com/wikis/infinite-craft/How_to_Play_Infinite_Craft))
- Start with Water, Fire, Wind and Earth; drag from menu into play area; Water plus Fire makes Steam; combining same item with itself works, e.g. Earth plus Earth makes Mountain; Reset wipes discoveries while broom clears only the workspace ([source](https://dotesports.com/general/news/how-to-play-infinite-craft-from-neal-fun))
- Uses Llama 2 and Llama 3.1 to create new elements and emojis; unseen pairs go to generative AI then saved to database so the same pair always outputs the same result; first finder gets First Discovery label; no defined goal ([source](https://en.wikipedia.org/wiki/Infinite_Craft))
- Official app description: endless crafting from neal.fun, start with Water, Fire, Earth and Wind, over 100 million combinations, be first to discover new items ([source](https://play.google.com/store/apps/details?id=fun.neal.infinite.craft&hl=en))
- Mouse control: all you need is a working mouse to click and drag elements; combining is done by dropping one element on another ([source](https://www.ign.com/wikis/infinite-craft/How_to_Play_Infinite_Craft))
- Mobile control: on mobile tap an object then tap a second object to merge them; PC uses click-and-drag workspace ([source](https://infinite-craft.com/))
- GitHub API search finds no verified official Neal Agarwal source repository for Infinite Craft, only third-party clones such as Scottidk/infinite-craft-clone and guides such as expitau/InfiniteCraftWiki; nealagarwal user lookup returns no matching official repo ([source](https://api.github.com/search/repositories?q=infinite-craft+neal&per_page=5))
- Direct fetch of the game page returns Cloudflare 403 challenge, so page body was corroborated via search-provider live crawl, Wikipedia, IGN, DotEsports and store listings; source code was not cloned and no official code findings are claimed ([source](https://neal.fun/infinite-craft/))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 85/100: Fictional illustrative review one: started with Fire and Water at midnight and looked up to find I'd built Steam engines, planets, and somehow Shrek — the First Discovery pop-up when I made something nobody had seen felt absurdly good.
- 60/100: Fictional illustrative review two: made-up casual player note — endlessly clever for an evening, but after an hour it's the same drag-and-drop on a blank page and the jokes repeat; fun toy, thin game.
- 100/100: Fictional illustrative review three: invented systems-fan take — an AI that turns any two words into a new word with 100 million combos and still loads in a tab? As an internet toy this is the defining browser game of 2024.

## Links

- [https://neal.fun/infinite-craft/](https://neal.fun/infinite-craft/)
- [https://en.wikipedia.org/wiki/Infinite\_Craft](https://en.wikipedia.org/wiki/Infinite_Craft)
- [https://www.ign.com/wikis/infinite-craft/How\_to\_Play\_Infinite\_Craft](https://www.ign.com/wikis/infinite-craft/How_to_Play_Infinite_Craft)
- [https://dotesports.com/general/news/how-to-play-infinite-craft-from-neal-fun](https://dotesports.com/general/news/how-to-play-infinite-craft-from-neal-fun)
- [https://play.google.com/store/apps/details?id=fun.neal.infinite.craft&hl=en](https://play.google.com/store/apps/details?id=fun.neal.infinite.craft&hl=en)
