class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
    def display_board(self):
        print("\n")
        for i in range(3):
            row = " | ".join(self.board[i * 3:(i + 1) * 3])
            print(f" {row} ")
            if i < 2:
                print("---+---+---")
        print("\n")
    def make_move(self, position):
        if self.board[position] == " ":
            self.board[position] = self.current_player
            return True
        return False
    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
    def is_winner(self):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        for condition in win_conditions:
            if all(self.board[i] == self.current_player for i in condition):
                return True
        return False
    def is_draw(self):
        return " " not in self.board
    def play(self):
        print("Welcome to Tic-Tac-Toe!")
        print("Positions are numbered 1–9 as follows:\n")
        print(" 1 | 2 | 3 ")
        print("---+---+---")
        print(" 4 | 5 | 6 ")
        print("---+---+---")
        print(" 7 | 8 | 9 \n")
        while True:
            self.display_board()
            try:
                move = int(input(f"Player {self.current_player}, choose position (1-9): ")) - 1
                if move < 0 or move > 8:
                    print("Invalid position. Try again.")
                    continue
            except ValueError:
                print("Please enter a number between 1 and 9.")
                continue
            if not self.make_move(move):
                print("Position already taken. Try again.")
                continue

            if self.is_winner():
                self.display_board()
                print(f"🎉 Player {self.current_player} wins!")
                break
            if self.is_draw():
                self.display_board()
                print("It's a draw!")
                break
            self.switch_player()
if __name__ == "__main__":
    game = TicTacToe()
    game.play()