# Devi's Lab

[Open the game source](https://github.com/shyamathreye/devis-lab)
[Play the game](https://shyamathreye.github.io/devis-lab/)
**Repository created:** 2026-06-17T03:12:52Z
**Added to catalog:** 2026-09-27T04:41:33.565601+00:00
**Updated in catalog:** 2026-09-27T04:41:33.565601+00:00

**Overall rating:** 33/100. Three complete kid-friendly loops (hangman, unscramble, whack-a-mole) with 4 themes, 4 difficulties, word banks, TTS voice, synth audio, and local leaderboard give it broader scope than single-mechanic catalog games like 2048 (38), chess rot (30), TypeScript-Blackjack (28), and T-Rex Runner (35). Closest comparators: Pizza Chef (44) has deeper arcade systems and touch+keyboard support on the same React+Vite+Tailwind+Web Audio stack, so the target sits below it; Top-10 Tension (32) and Taipo (35) are similarly educational guessing/typing games with hints and word lists, placing the target between them at 33; Beachy Beachy Ball (25) shares modes/difficulties/local-best structure but the target has three games versus one. Far below Ashlands (55), OSRS Tower Defense (52), and Kart Royale (50) on 3D scope, systems depth, and polish. No gameplay screenshots could be inspected (repo contains zero images), so visual polish is unverified; score reflects documented scope and code evidence, not proven playability, performance, or balance.

**Screenshot score:** not scored. No inspectable gameplay screenshot.

## Play

- Type your name on the welcome screen and press Let's Play
- Pick a world: Unicorns, Animals, Ocean, Space (plus pirate copy variant)
- Pick a game: Save the Balloons, Mix-Up Magic, or Tap the Critter
- Pick a difficulty: Baby, Kid, Adult, or Thatha and play six rounds or a timed round
- Scores save to the on-device local leaderboard; use Switch player for a new profile

## Mechanics

- Friendly hangman over 6 rounds: tap on-screen letters, wrong guesses pop 1 of 6 balloons
- Letter unscramble: tap tray tiles into answer slots with 3-stage hint (clue, hear word, spell)
- Whack-a-mole reflex rounds: 9 holes, timed 30-second rounds with normal (10 pts) and golden (50 pts) critters
- Four difficulty tiers changing word length, shown first letter, auto voice, critter speed and count
- Four visual world themes plus pirate copy variant, persistent name and theme profile
- Per-game local leaderboard with top-10 sorted scores stored in localStorage
- Synthesized Web Audio sound effects with global mute toggle and browser text-to-speech word readout

## Tags

- educational
- kids
- word-game
- hangman
- unscramble
- whack-a-mole
- reflex
- party-collection
- single-player
- browser

## Controls

- Mobile controls: Supported
- Motion controls: Not established
- Gamepad: Not established
- Keyboard/mouse: Supported

## Player modes

- Human players: 1
- Modes: single-player

## Technologies

- **React 18.3.1** — framework ([evidence](https://raw.githubusercontent.com/shyamathreye/devis-lab/main/package.json))
- **Vite 5.3.5** — build ([evidence](https://raw.githubusercontent.com/shyamathreye/devis-lab/main/package.json))
- **Tailwind CSS 3.4.7** — framework ([evidence](https://raw.githubusercontent.com/shyamathreye/devis-lab/main/package.json))
- **Framer Motion 11.3.8** — framework ([evidence](https://raw.githubusercontent.com/shyamathreye/devis-lab/main/package.json))
- **JavaScript** — language ([evidence](https://api.github.com/repos/shyamathreye/devis-lab/languages))
- **Web Audio API** — audio ([evidence](https://raw.githubusercontent.com/shyamathreye/devis-lab/main/src/lib/sound.js))
- **Web Speech API (SpeechSynthesis)** — audio ([evidence](https://raw.githubusercontent.com/shyamathreye/devis-lab/main/src/lib/speech.js))

## Reconstructed prompt

Build a bright neon kid-friendly browser mini-game site called Devi's Lab with three games (friendly balloon hangman, tap-to-unscramble words, whack-a-mole critters), four world themes, four kid difficulties, emoji word hints with voice readout, synth sound effects with mute, and a localStorage leaderboard, using React plus Vite, Tailwind, and Framer Motion with a static dist build deployable to GitHub Pages.

## Source evidence

- Repository shyamathreye/devis-lab is a real public game project described as bright neon word and reflex games for kids (React + Vite); default branch main, JavaScript-dominant ([source](https://api.github.com/repos/shyamathreye/devis-lab))
- README defines three playable games: Save the Balloons (friendly hangman), Mix-Up Magic (unscramble by tapping tiles), Tap the Critter (whack-a-mole with golden star worth lots), plus name entry, 4 worlds, 4 difficulties, and local leaderboard ([source](https://raw.githubusercontent.com/shyamathreye/devis-lab/main/README.md))
- File tree confirms game implementations at src/games/Hangman.jsx, Unscramble.jsx, WhackAMole.jsx with screens, word/theme/difficulty data, sound/speech/storage libs, and no image assets (zero screenshots in repo) ([source](https://api.github.com/repos/shyamathreye/devis-lab/git/trees/main?recursive=1))
- GitHub Pages deployment succeeded with environment\_url https://shyamathreye.github.io/devis-lab/ and the live HTML shell serves the built SPA (title Devi Jones, div#root, compiled assets) ([source](https://shyamathreye.github.io/devis-lab/))
- Tap-to-play wording (tap letters, tapping tiles, tap critters) plus onClick handlers in all three games supports mouse and touch; viewport meta disables pinch zoom for a mobile app-like layout; no keydown handlers, gamepad, or motion input found ([source](https://raw.githubusercontent.com/shyamathreye/devis-lab/main/src/games/Hangman.jsx))
- Single-player only: Hangman/Unscramble run 6 solo rounds, WhackAMole runs solo timed rounds, scores stored per-device via localStorage leaderboard; no multiplayer code or claims ([source](https://raw.githubusercontent.com/shyamathreye/devis-lab/main/src/lib/storage.js))
- No existing catalog directory matches devis-lab; catalog index tops at Ashlands 55 with closest educational/casual comparators Pizza Chef 44, Taipo 35, Top-10 Tension 32, Beachy Beachy Ball 25 ([source](https://github.com/shyamathreye/devis-lab))

## Fictional reviews

Treat these as illustrative, not real user reviews.

- 75/100: My five-year-old guessed balloons with the voice hints on and begged for one more round of critter-tapping.
- 55/100: Sweet and gentle trio of games, though a grown-up will burn through the word lists fast.
- 90/100: The golden critter made the whole room scream. Simple, kind, and perfect for little hands.

## Links

- [Source repository](https://github.com/shyamathreye/devis-lab)
- [Playable build (GitHub Pages)](https://shyamathreye.github.io/devis-lab/)
