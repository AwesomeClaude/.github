# chess rot

[Open the game source](https://github.com/jaimec00/chess-game)

**Overall rating:** 30/100. Far from AAA: single fixed chessboard, white-only, depth-3 minimax plus prompt-based LLM, flat 2D DOM/SVG presentation, no multiplayer, ratings, variants, progression, or live-ops scale; source and stills do not prove playability, strength, balance or performance. Most relevant comparators: TypeScript-Blackjack (28 overall) as complete single-table 2D rules-faithful game — chess rot exceeds it on rules breadth, hand-rolled engine, and dual AI/LLM modes with cleaner glass UI; Taipo (35) as complete distinctive loop with multi-year releases and itch traction — chess rot trails on originality, scope variety and shipped validation; Neural Sight (30) as narrow tech prototype — chess rot matches on overall polish-vs-scope tradeoff with a finished loop but flat visuals. Below neverquest (45) systems depth and both kart racers (40-50) 3D systems/HUD/menus. Evidence gaps: gh api rate-limited so judged via web README plus raw source and 3 PR screenshots only; did not play live, no stars/forks, no performance or AI-strength data.

**Screenshot score:** 40/100. Best gameplay frame shows a clean coherent flat 2D board: sharp cburnett SVGs, aligned coordinates, glass frame and readable side panel. Rewarded for tidy stylization above TypeScript-Blackjack (35) flat felt and Beachy Beachy Ball (35) sparse runway and neverquest (30) text dashboard. Deducted heavily vs Taipo (55) pixel scene and all three catalog 70s (Kart Royale, Turbo Kart Rally, Neural Sight) for no lighting, texture, environment, effects or composition beyond a single board; stills reveal nothing about motion or feel.

## Screenshots

![Inspected 2800x1800 gameplay frame: starting chess position on flat blue-gray 2D board with rank/file coordinates, cburnett-style white/black pieces with drop shadows, dark glass frame, right info panel with CHESS / PLAYER VS ENGINE, White to move dot, WHITE/BLACK CAPTURES rows, NEW GAME button. Game's own runtime output, sharpest board detail.](https://raw.githubusercontent.com/jaimec00/chess-game/pr-screenshots/pr-34-play.png)

Inspected 2800x1800 gameplay frame: starting chess position on flat blue-gray 2D board with rank/file coordinates, cburnett-style white/black pieces with drop shadows, dark glass frame, right info panel with CHESS / PLAYER VS ENGINE, White to move dot, WHITE/BLACK CAPTURES rows, NEW GAME button. Game's own runtime output, sharpest board detail.

![Inspected 2800x1800 gameplay frame of LLM mode: same starting board left, right stack with PROVIDER Anthropic (Claude), MODEL Haiku 4.5, API KEY input with SAVE, CHAT panel PLAYER VS HAIKU 4.5, White to move, captures rows, NEW GAME. Game's own output; gameplay plus setup/chat chrome.](https://raw.githubusercontent.com/jaimec00/chess-game/pr-screenshots/pr-34-api.png)

Inspected 2800x1800 gameplay frame of LLM mode: same starting board left, right stack with PROVIDER Anthropic (Claude), MODEL Haiku 4.5, API KEY input with SAVE, CHAT panel PLAYER VS HAIKU 4.5, White to move, captures rows, NEW GAME. Game's own output; gameplay plus setup/chat chrome.

![Inspected 2800x1800 title card: near-black background with large outlined CHESS ROT wordmark centered and two glass buttons new game (local) and new game (api). Menu/title only, no board or gameplay; discounted for graphics scoring.](https://raw.githubusercontent.com/jaimec00/chess-game/pr-screenshots/pr-34-landing.png)

Inspected 2800x1800 title card: near-black background with large outlined CHESS ROT wordmark centered and two glass buttons new game (local) and new game (api). Menu/title only, no board or gameplay; discounted for graphics scoring.

## Play

- Run npm install then npm run dev and open http://localhost:5173, or open the deployed build.
- On the CHESS ROT landing page choose new game (local) for built-in AI or new game (api) for LLM play.
- For API mode select provider Anthropic and model Haiku 4.5 or Sonnet 4.5, paste your Anthropic key and save (stored locally).
- Play White: click one of your white pieces to select and show legal-move highlights, then click a highlighted target square.
- If moving a pawn to the last rank, pick the promotion piece in the dialog.
- Wait for Black to reply (local engine thinking indicator or LLM chat thinking); repeat until checkmate, stalemate or draw.
- Use NEW GAME to reset the board and captures; in API mode read and reply via the chat panel.

## Mechanics

- Play-White-only vs Black AI turn structure with click-select then click-move input
- Hand-written pseudo-legal move generation plus legality filtering by king-in-check test
- Castling with rights tracking and attacked-square validation
- En passant capture with double-push target tracking
- Pawn promotion picker (local AI always queens)
- Check, checkmate and stalemate detection via all-legal-moves plus attack maps
- 50-move rule draw at 100 halfmoves
- Threefold repetition draw via board-plus-turn string hashes
- Insufficient material draws (K vs K, K+minor vs K, same-color bishops)
- Local minimax alpha-beta depth-3 opponent with material plus piece-square evaluation and capture-first ordering
- LLM opponent playing Black via SAN with board description, illegal-move retry up to 3x, and chat commentary
- Captured-pieces tracking, last-move highlight, legal-move dots, check indicator, move history in SAN

## Tags

- chess
- board-game
- strategy
- 2d
- browser-game
- react
- vite
- tailwind
- minimax
- llm-opponent
- single-player

## Reconstructed prompt

Build chess rot, a browser chess game in React 19 + Vite + Tailwind v4 + shadcn/ui with no chess libraries: hand-written engine with full rules (castling, en passant, promotion, check/mate/stalemate, 50-move, threefold, insufficient material), local minimax alpha-beta depth-3 Black opponent, bring-your-own-key LLM opponent mode vs Claude Haiku/Sonnet with chat, flat 2D blue-gray glassmorphism board with cburnett SVGs, coordinates, highlights, promotion modal, captures panel, landing plus local and API routes.

## Source evidence

- Repo title is 'chess rot': browser chess, play as White vs local AI or LLM opponent, built from scratch with React, Vite, Tailwind CSS, no external chess libraries ([source](https://github.com/jaimec00/chess-game/blob/master/README.md))
- Full chess rules claimed: castling, en passant, pawn promotion, check/checkmate/stalemate, 50-move rule, threefold repetition, insufficient material draws ([source](https://github.com/jaimec00/chess-game/blob/master/README.md))
- Local AI is minimax with alpha-beta pruning at depth 3, runs entirely in browser; evaluation is material plus piece-square tables, captures ordered first, always promotes to queen ([source](https://github.com/jaimec00/chess-game/blob/master/src/engine/ai.js))
- Move generation covers pawn pushes/captures/promotion/double-push/en-passant, knight, sliding pieces, king plus castling with attacked-square checks, then filters pseudo-legal moves by cloning board and rejecting moves leaving own king in check ([source](https://github.com/jaimec00/chess-game/blob/master/src/engine/moves.js))
- gameState makeMove applies special moves, flips turn, tracks captures and position hashes, and detects checkmate/stalemate, 50-move draw at halfMoveClock\>=100, threefold repetition, and insufficient material (K vs K, K+minor vs K, same-color bishops) ([source](https://github.com/jaimec00/chess-game/blob/master/src/engine/gameState.js))
- LLM mode is bring-your-own-key vs Claude via Anthropic Messages API (Haiku 4.5 default, Sonnet 4.5), direct browser fetch with dangerous-direct-browser-access header, max 300 tokens, SAN on line 1 plus comment, up to 3 retries on illegal moves ([source](https://github.com/jaimec00/chess-game/blob/master/CLAUDE.md))
- Tech stack React 19 + Vite 7 + Tailwind v4 + shadcn/ui + react-router-dom; routes / local play, /play/api LLM play with chat and provider controls, catch-all to landing; dark glassmorphism with blue-gray board and cburnett SVG pieces ([source](https://github.com/jaimec00/chess-game/blob/master/package.json))
- Local game loop: click White piece to show legal-move highlights, click target to move, promotion opens picker modal, Black replies after 100ms thinking delay; white-only play, New Game resets state ([source](https://github.com/jaimec00/chess-game/blob/master/src/components/Game.jsx))
- Board UI is flat 2D glass frame with rank/file labels, last-move highlight, selection glow, legal-move hint dots, check throb; landing page is minimal 'CHESS ROT' title with new game (local) and new game (api) buttons ([source](https://github.com/jaimec00/chess-game/blob/master/src/components/Board.jsx))
- PR screenshots confirm live runtime output: headless Brave captures at 1400x900 2x of /play, / and /play/api waiting for .board/h1 selectors; closed PRs host pr-30, pr-31-play/landing/api and pr-34-play/landing/api images ([source](https://github.com/jaimec00/chess-game/pull/31))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 75/100: Fictional illustrative review one: finally beat the local engine after it hung my knight — full castling and en passant just worked, and the glass board with those chunky pieces looks way classier than I expected.
- 55/100: Fictional illustrative review two: solid chess in a tab, but depth-3 AI feels wooden and white-only gets stale; the LLM chat is fun until it blunders a queen. Fine for a quick game, not a club replacement.
- 100/100: Fictional illustrative review three: hand-rolled move gen plus SAN plus Anthropic chat with zero chess deps? As a code toy this is delightful — I came for the minimax and stayed to argue openings with Haiku.

## Links

- [Source repository](https://github.com/jaimec00/chess-game)
- [Related link](https://github.com/jaimec00/chess-game/blob/master/README.md)
- [Related link](https://github.com/jaimec00/chess-game/blob/master/src/engine/ai.js)
- [Related link](https://github.com/jaimec00/chess-game/pull/34)
