import tkinter as tk
from tkinter import messagebox
import random


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.geometry("620x760")
        self.root.resizable(False, False)
        self.root.configure(bg="#121212")

        # ---------------------------------------------------------
        # GAME VARIABLES
        # ---------------------------------------------------------

        self.board = [""] * 9
        self.current_player = "X"
        self.game_over = False

        self.player_x_score = 0
        self.player_o_score = 0
        self.draw_score = 0

        self.game_mode = "PvP"
        self.difficulty = "Hard"

        self.x_color = "#00E5FF"
        self.o_color = "#FF4081"
        self.bg_color = "#121212"
        self.panel_color = "#1E1E1E"
        self.button_color = "#292929"
        self.hover_color = "#383838"
        self.text_color = "#FFFFFF"
        self.secondary_text = "#AAAAAA"
        self.green_color = "#00E676"
        self.yellow_color = "#FFD740"

        self.buttons = []

        # ---------------------------------------------------------
        # CREATE INTERFACE
        # ---------------------------------------------------------

        self.create_header()
        self.create_scoreboard()
        self.create_status()
        self.create_board()
        self.create_control_panel()
        self.create_footer()

        # Keyboard shortcuts
        self.root.bind("<n>", lambda event: self.new_game())
        self.root.bind("<N>", lambda event: self.new_game())
        self.root.bind("<r>", lambda event: self.reset_scores())
        self.root.bind("<R>", lambda event: self.reset_scores())
        self.root.bind("<Escape>", lambda event: self.root.destroy())

    # ============================================================
    # HEADER
    # ============================================================

    def create_header(self):
        header = tk.Frame(
            self.root,
            bg=self.bg_color
        )
        header.pack(fill="x", pady=(20, 5))

        title = tk.Label(
            header,
            text="TIC-TAC-TOE",
            font=("Segoe UI", 28, "bold"),
            fg=self.text_color,
            bg=self.bg_color
        )
        title.pack()

        subtitle = tk.Label(
            header,
            text="Classic game • Modern interface",
            font=("Segoe UI", 10),
            fg=self.secondary_text,
            bg=self.bg_color
        )
        subtitle.pack(pady=(2, 0))

    # ============================================================
    # SCOREBOARD
    # ============================================================

    def create_scoreboard(self):
        scoreboard = tk.Frame(
            self.root,
            bg=self.bg_color
        )
        scoreboard.pack(fill="x", padx=40, pady=15)

        self.x_score_frame = tk.Frame(
            scoreboard,
            bg=self.panel_color,
            width=160,
            height=70
        )
        self.x_score_frame.pack(
            side="left",
            expand=True,
            fill="both",
            padx=(0, 8)
        )
        self.x_score_frame.pack_propagate(False)

        self.o_score_frame = tk.Frame(
            scoreboard,
            bg=self.panel_color,
            width=160,
            height=70
        )
        self.o_score_frame.pack(
            side="left",
            expand=True,
            fill="both",
            padx=8
        )
        self.o_score_frame.pack_propagate(False)

        self.draw_score_frame = tk.Frame(
            scoreboard,
            bg=self.panel_color,
            width=160,
            height=70
        )
        self.draw_score_frame.pack(
            side="left",
            expand=True,
            fill="both",
            padx=(8, 0)
        )
        self.draw_score_frame.pack_propagate(False)

        tk.Label(
            self.x_score_frame,
            text="PLAYER X",
            font=("Segoe UI", 10, "bold"),
            fg=self.x_color,
            bg=self.panel_color
        ).pack(pady=(8, 0))

        self.x_score_label = tk.Label(
            self.x_score_frame,
            text="0",
            font=("Segoe UI", 22, "bold"),
            fg=self.text_color,
            bg=self.panel_color
        )
        self.x_score_label.pack()

        tk.Label(
            self.o_score_frame,
            text="PLAYER O",
            font=("Segoe UI", 10, "bold"),
            fg=self.o_color,
            bg=self.panel_color
        ).pack(pady=(8, 0))

        self.o_score_label = tk.Label(
            self.o_score_frame,
            text="0",
            font=("Segoe UI", 22, "bold"),
            fg=self.text_color,
            bg=self.panel_color
        )
        self.o_score_label.pack()

        tk.Label(
            self.draw_score_frame,
            text="DRAWS",
            font=("Segoe UI", 10, "bold"),
            fg=self.yellow_color,
            bg=self.panel_color
        ).pack(pady=(8, 0))

        self.draw_score_label = tk.Label(
            self.draw_score_frame,
            text="0",
            font=("Segoe UI", 22, "bold"),
            fg=self.text_color,
            bg=self.panel_color
        )
        self.draw_score_label.pack()

    # ============================================================
    # STATUS
    # ============================================================

    def create_status(self):
        status_frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )
        status_frame.pack(fill="x", padx=40, pady=(5, 15))

        self.status_label = tk.Label(
            status_frame,
            text="Player X's turn",
            font=("Segoe UI", 14, "bold"),
            fg=self.x_color,
            bg=self.bg_color
        )
        self.status_label.pack()

        self.mode_label = tk.Label(
            status_frame,
            text="Mode: Player vs Player",
            font=("Segoe UI", 9),
            fg=self.secondary_text,
            bg=self.bg_color
        )
        self.mode_label.pack(pady=(3, 0))

    # ============================================================
    # BOARD
    # ============================================================

    def create_board(self):
        board_container = tk.Frame(
            self.root,
            bg="#333333",
            padx=5,
            pady=5
        )
        board_container.pack(padx=40, pady=5)

        for index in range(9):
            button = tk.Button(
                board_container,
                text="",
                font=("Segoe UI", 42, "bold"),
                width=3,
                height=1,
                bg=self.button_color,
                fg=self.text_color,
                activebackground=self.hover_color,
                activeforeground=self.text_color,
                relief="flat",
                borderwidth=0,
                cursor="hand2",
                command=lambda i=index: self.cell_clicked(i)
            )

            row = index // 3
            column = index % 3

            button.grid(
                row=row,
                column=column,
                padx=3,
                pady=3,
                ipadx=8,
                ipady=8
            )

            button.bind(
                "<Enter>",
                lambda event, b=button: self.on_hover(b)
            )

            button.bind(
                "<Leave>",
                lambda event, b=button: self.on_leave(b)
            )

            self.buttons.append(button)

    # ============================================================
    # CONTROL PANEL
    # ============================================================

    def create_control_panel(self):
        control = tk.Frame(
            self.root,
            bg=self.bg_color
        )
        control.pack(fill="x", padx=40, pady=20)

        mode_label = tk.Label(
            control,
            text="Game Mode",
            font=("Segoe UI", 10, "bold"),
            fg=self.secondary_text,
            bg=self.bg_color
        )
        mode_label.grid(
            row=0,
            column=0,
            sticky="w",
            padx=(0, 10)
        )

        self.mode_var = tk.StringVar(value="PvP")

        mode_menu = tk.OptionMenu(
            control,
            self.mode_var,
            "PvP",
            "PvC",
            command=self.change_mode
        )

        mode_menu.config(
            font=("Segoe UI", 10),
            bg=self.button_color,
            fg=self.text_color,
            activebackground=self.hover_color,
            activeforeground=self.text_color,
            highlightthickness=0,
            width=8
        )

        mode_menu["menu"].config(
            bg=self.panel_color,
            fg=self.text_color
        )

        mode_menu.grid(
            row=0,
            column=1,
            padx=5
        )

        difficulty_label = tk.Label(
            control,
            text="Difficulty",
            font=("Segoe UI", 10, "bold"),
            fg=self.secondary_text,
            bg=self.bg_color
        )
        difficulty_label.grid(
            row=0,
            column=2,
            padx=(20, 10)
        )

        self.difficulty_var = tk.StringVar(value="Hard")

        difficulty_menu = tk.OptionMenu(
            control,
            self.difficulty_var,
            "Easy",
            "Medium",
            "Hard",
            command=self.change_difficulty
        )

        difficulty_menu.config(
            font=("Segoe UI", 10),
            bg=self.button_color,
            fg=self.text_color,
            activebackground=self.hover_color,
            activeforeground=self.text_color,
            highlightthickness=0,
            width=8
        )

        difficulty_menu["menu"].config(
            bg=self.panel_color,
            fg=self.text_color
        )

        difficulty_menu.grid(
            row=0,
            column=3,
            padx=5
        )

        new_button = tk.Button(
            control,
            text="NEW GAME",
            font=("Segoe UI", 10, "bold"),
            bg=self.green_color,
            fg="#000000",
            activebackground="#69F0AE",
            activeforeground="#000000",
            relief="flat",
            cursor="hand2",
            command=self.new_game,
            width=12
        )

        new_button.grid(
            row=1,
            column=0,
            columnspan=2,
            pady=(15, 0),
            padx=5
        )

        reset_button = tk.Button(
            control,
            text="RESET SCORES",
            font=("Segoe UI", 10, "bold"),
            bg="#FF5252",
            fg="#FFFFFF",
            activebackground="#FF7676",
            activeforeground="#FFFFFF",
            relief="flat",
            cursor="hand2",
            command=self.reset_scores,
            width=12
        )

        reset_button.grid(
            row=1,
            column=2,
            columnspan=2,
            pady=(15, 0),
            padx=5
        )

    # ============================================================
    # FOOTER
    # ============================================================

    def create_footer(self):
        footer = tk.Frame(
            self.root,
            bg=self.bg_color
        )
        footer.pack(
            side="bottom",
            fill="x",
            pady=10
        )

        text = tk.Label(
            footer,
            text="N = New Game    |    R = Reset Scores    |    ESC = Exit",
            font=("Segoe UI", 8),
            fg="#666666",
            bg=self.bg_color
        )

        text.pack()

    # ============================================================
    # HOVER EFFECT
    # ============================================================

    def on_hover(self, button):
        if button["text"] == "":
            button.configure(
                bg=self.hover_color
            )

    def on_leave(self, button):
        if button["text"] == "":
            button.configure(
                bg=self.button_color
            )

    # ============================================================
    # CELL CLICK
    # ============================================================

    def cell_clicked(self, index):
        if self.game_over:
            return

        if self.board[index] != "":
            return

        if self.game_mode == "PvC" and self.current_player == "O":
            return

        self.make_move(index, self.current_player)

        if self.game_over:
            return

        if self.game_mode == "PvC":
            self.current_player = "O"
            self.update_status()

            self.root.after(
                400,
                self.computer_move
            )
        else:
            self.switch_player()

    # ============================================================
    # MAKE MOVE
    # ============================================================

    def make_move(self, index, player):
        self.board[index] = player

        button = self.buttons[index]

        button.configure(
            text=player,
            fg=self.x_color if player == "X" else self.o_color,
            bg=self.panel_color,
            activeforeground=self.x_color
            if player == "X"
            else self.o_color
        )

        winner = self.check_winner(self.board)

        if winner:
            self.handle_win(winner)
            return

        if self.is_draw(self.board):
            self.handle_draw()
            return

    # ============================================================
    # SWITCH PLAYER
    # ============================================================

    def switch_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

        self.update_status()

    # ============================================================
    # UPDATE STATUS
    # ============================================================

    def update_status(self):
        if self.game_over:
            return

        if self.current_player == "X":
            color = self.x_color
        else:
            color = self.o_color

        if self.game_mode == "PvC":
            if self.current_player == "X":
                message = "Your turn — X"
            else:
                message = "Computer is thinking..."
        else:
            message = f"Player {self.current_player}'s turn"

        self.status_label.configure(
            text=message,
            fg=color
        )

    # ============================================================
    # CHECK WINNER
    # ============================================================

    def check_winner(self, board):
        winning_combinations = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6)
        ]

        for combo in winning_combinations:
            a, b, c = combo

            if (
                board[a] != ""
                and board[a] == board[b]
                and board[a] == board[c]
            ):
                return board[a]

        return None

    # ============================================================
    # DRAW CHECK
    # ============================================================

    def is_draw(self, board):
        return all(cell != "" for cell in board)

    # ============================================================
    # HANDLE WIN
    # ============================================================

    def handle_win(self, winner):
        self.game_over = True

        if winner == "X":
            self.player_x_score += 1
            self.x_score_label.configure(
                text=str(self.player_x_score)
            )
            color = self.x_color
        else:
            self.player_o_score += 1
            self.o_score_label.configure(
                text=str(self.player_o_score)
            )
            color = self.o_color

        winning_cells = self.get_winning_cells(self.board)

        for index in winning_cells:
            self.buttons[index].configure(
                bg=color,
                fg="#000000"
            )

        self.status_label.configure(
            text=f"Player {winner} wins!",
            fg=color
        )

        self.root.after(
            250,
            lambda: self.show_result(
                f"Player {winner} wins!"
            )
        )

    # ============================================================
    # GET WINNING CELLS
    # ============================================================

    def get_winning_cells(self, board):
        winning_combinations = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6)
        ]

        for combo in winning_combinations:
            a, b, c = combo

            if (
                board[a] != ""
                and board[a] == board[b]
                and board[a] == board[c]
            ):
                return combo

        return []

    # ============================================================
    # HANDLE DRAW
    # ============================================================

    def handle_draw(self):
        self.game_over = True

        self.draw_score += 1

        self.draw_score_label.configure(
            text=str(self.draw_score)
        )

        self.status_label.configure(
            text="It's a draw!",
            fg=self.yellow_color
        )

        for button in self.buttons:
            button.configure(
                bg="#4A4A2A"
            )

        self.root.after(
            250,
            lambda: self.show_result(
                "It's a draw!"
            )
        )

    # ============================================================
    # SHOW RESULT
    # ============================================================

    def show_result(self, message):
        answer = messagebox.askyesno(
            "Game Over",
            f"{message}\n\nWould you like to play again?"
        )

        if answer:
            self.new_game()

    # ============================================================
    # NEW GAME
    # ============================================================

    def new_game(self):
        self.board = [""] * 9
        self.current_player = "X"
        self.game_over = False

        for button in self.buttons:
            button.configure(
                text="",
                bg=self.button_color,
                fg=self.text_color
            )

        self.update_status()

    # ============================================================
    # RESET SCORES
    # ============================================================

    def reset_scores(self):
        answer = messagebox.askyesno(
            "Reset Scores",
            "Are you sure you want to reset all scores?"
        )

        if not answer:
            return

        self.player_x_score = 0
        self.player_o_score = 0
        self.draw_score = 0

        self.x_score_label.configure(
            text="0"
        )

        self.o_score_label.configure(
            text="0"
        )

        self.draw_score_label.configure(
            text="0"
        )

        self.new_game()

    # ============================================================
    # CHANGE MODE
    # ============================================================

    def change_mode(self, value):
        self.game_mode = value

        if value == "PvP":
            self.mode_label.configure(
                text="Mode: Player vs Player"
            )
        else:
            self.mode_label.configure(
                text="Mode: Player vs Computer"
            )

        self.new_game()

    # ============================================================
    # CHANGE DIFFICULTY
    # ============================================================

    def change_difficulty(self, value):
        self.difficulty = value

        if self.game_mode == "PvC":
            self.new_game()

    # ============================================================
    # COMPUTER MOVE
    # ============================================================

    def computer_move(self):
        if self.game_over:
            return

        if self.game_mode != "PvC":
            return

        if self.current_player != "O":
            return

        available = [
            i for i, value in enumerate(self.board)
            if value == ""
        ]

        if not available:
            return

        if self.difficulty == "Easy":
            move = self.easy_move()

        elif self.difficulty == "Medium":
            move = self.medium_move()

        else:
            move = self.best_move()

        self.make_move(
            move,
            "O"
        )

        if self.game_over:
            return

        self.current_player = "X"
        self.update_status()

    # ============================================================
    # EASY AI
    # ============================================================

    def easy_move(self):
        available = [
            i for i, value in enumerate(self.board)
            if value == ""
        ]

        return random.choice(available)

    # ============================================================
    # MEDIUM AI
    # ============================================================

    def medium_move(self):
        # First, try to win.
        for index in range(9):
            if self.board[index] == "":
                self.board[index] = "O"

                if self.check_winner(self.board) == "O":
                    self.board[index] = ""
                    return index

                self.board[index] = ""

        # Then block player X.
        for index in range(9):
            if self.board[index] == "":
                self.board[index] = "X"

                if self.check_winner(self.board) == "X":
                    self.board[index] = ""
                    return index

                self.board[index] = ""

        # Prefer center.
        if self.board[4] == "":
            return 4

        # Prefer corners.
        corners = [
            0,
            2,
            6,
            8
        ]

        available_corners = [
            i for i in corners
            if self.board[i] == ""
        ]

        if available_corners:
            return random.choice(
                available_corners
            )

        return self.easy_move()

    # ============================================================
    # BEST MOVE
    # ============================================================

    def best_move(self):
        best_score = float("-inf")
        move = None

        for index in range(9):
            if self.board[index] == "":
                self.board[index] = "O"

                score = self.minimax(
                    self.board,
                    False
                )

                self.board[index] = ""

                if score > best_score:
                    best_score = score
                    move = index

        return move

    # ============================================================
    # MINIMAX ALGORITHM
    # ============================================================

    def minimax(self, board, maximizing):
        winner = self.check_winner(board)

        if winner == "O":
            return 10

        if winner == "X":
            return -10

        if self.is_draw(board):
            return 0

        if maximizing:
            best_score = float("-inf")

            for index in range(9):
                if board[index] == "":
                    board[index] = "O"

                    score = self.minimax(
                        board,
                        False
                    )

                    board[index] = ""

                    best_score = max(
                        best_score,
                        score
                    )

            return best_score

        else:
            best_score = float("inf")

            for index in range(9):
                if board[index] == "":
                    board[index] = "X"

                    score = self.minimax(
                        board,
                        True
                    )

                    board[index] = ""

                    best_score = min(
                        best_score,
                        score
                    )

            return best_score


# ================================================================
# APPLICATION ENTRY POINT
# ================================================================

def main():
    root = tk.Tk()

    game = TicTacToe(root)

    root.mainloop()


# ================================================================
# RUN PROGRAM
# ================================================================

if __name__ == "__main__":
    main()
