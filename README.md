# Tic-Tac-Toe: Classic Game, Modern Interface

## Project overview

A desktop Tic-Tac-Toe game built with Python and Tkinter. Play locally with another person or against a computer opponent, with a dark themed interface, score tracking, and selectable AI difficulty.

## Features

- **Player vs Player (PvP):** Two people take turns as X and O.
- **Player vs Computer (PvC):** Play as X against the computer as O.
- **Three computer difficulty levels:**
  - **Easy:** chooses a random available square.
  - **Medium:** takes a winning move when possible, blocks an immediate X win, and otherwise favors the center and corners.
  - **Hard:** uses the minimax algorithm to choose an optimal move.
- **Scoreboard:** Tracks wins for X and O, plus draws for the current session.
- **Game feedback:** Highlights winning squares and announces a win or draw, with the option to play again.
- **Game controls:** Start a new round or reset all scores (with confirmation).
- **Keyboard shortcuts:** `N` starts a new round, `R` resets the scores, and `Esc` closes the window.
- **Modern interface:** Dark theme, colored X and O marks, and hover feedback on the board.

## Technologies and tools

- Python 3
- Tkinter (`tkinter` and `tkinter.messagebox`) for the desktop interface
- Python `random` module for the Easy and Medium computer moves
- Minimax search for the Hard computer opponent

No third-party Python packages are required. Tkinter is included with most standard Python installations; on some Linux distributions it may need to be installed separately.

## Install and run

1. Install Python 3. Confirm that Tkinter is available by running:

   ```bash
   python -m tkinter
   ```

   A small Tkinter demo window should appear. Close it after confirming.

2. Save the supplied game code as `tic_tac_toe.py`.

3. Open a terminal or command prompt in the folder containing the file and run:

   ```bash
   python tic_tac_toe.py
   ```

   On systems where the Python launcher is used, you can run `py tic_tac_toe.py` instead.

The game opens in its own window. No internet connection or package installation is needed to play.

## Testing instructions

Run the program, then check these behaviors manually:

1. **PvP turns:** Make alternating moves as X and O. Confirm that a square cannot be played twice and the turn indicator changes.
2. **Win detection:** Complete a row, column, or diagonal. Confirm the winning squares are highlighted, the winner is announced, and that player's score increases by one.
3. **Draw detection:** Fill the board without making three in a row. Confirm the draw is announced and the draw count increases.
4. **New round:** Select **NEW GAME** or press `N`. Confirm the board clears, X starts, and scores remain unchanged.
5. **Computer modes:** Select **PvC**, then try each difficulty. Confirm the computer responds as O and that Easy, Medium, and Hard make moves.
6. **Reset scores:** Select **RESET SCORES** or press `R`. Confirm the prompt appears; choose **No** to keep scores, then repeat and choose **Yes** to clear scores and start a fresh round.
7. **Exit shortcut:** Press `Esc` and confirm the game window closes.


