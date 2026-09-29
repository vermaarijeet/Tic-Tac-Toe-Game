# Tic-Tac-Toe Project Statement

## Problem statement

People looking for a quick, accessible way to play Tic-Tac-Toe may not have another player nearby or may want a simple computer opponent. This project provides a desktop game that supports both local two-player matches and play against a computer, while clearly showing turns and results.

## Scope of the project

The project covers a single-player desktop application for standard 3×3 Tic-Tac-Toe. It includes a graphical board, two play modes (Player vs Player and Player vs Computer), three computer difficulty levels, turn and result feedback, session score tracking, and controls to start a new round or reset scores.

The computer opponent uses random moves on Easy, a basic win/block strategy on Medium, and minimax search on Hard. The application is intended to run locally with Python 3 and Tkinter. Online play, user accounts, persistent score storage, and networked multiplayer are outside the current scope.

## Target users

- People who want a casual, familiar game on a desktop computer.
- Two friends or family members sharing one computer.
- Individual players who want to play against a computer opponent.
- Beginner Python learners interested in a small graphical application and basic game logic.

## High-level features

- Play Tic-Tac-Toe locally in Player vs Player or Player vs Computer mode.
- Choose Easy, Medium, or Hard computer difficulty.
- View whose turn it is and see win or draw results.
- See winning squares highlighted on the board.
- Track X wins, O wins, and draws during the current session.
- Start another round or reset the scores.
- Use keyboard shortcuts to start a new game, reset scores, or exit.
