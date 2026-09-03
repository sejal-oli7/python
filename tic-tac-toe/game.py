from player import Player
from board import Board


class Game:
    def __init__(self):
        self.board = Board()

        self.player1 = Player("Sejal", "X")
        self.player2 = Player("Ram", "O")

        self.current_player = self.player1

    def switch_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def check_winner(self):
        board = self.board.board
        symbol = self.current_player.symbol

        # Check rows
        if board[0] == symbol and board[1] == symbol and board[2] == symbol:
            return True

        if board[3] == symbol and board[4] == symbol and board[5] == symbol:
            return True

        if board[6] == symbol and board[7] == symbol and board[8] == symbol:
            return True

        # Check columns
        if board[0] == symbol and board[3] == symbol and board[6] == symbol:
            return True

        if board[1] == symbol and board[4] == symbol and board[7] == symbol:
            return True

        if board[2] == symbol and board[5] == symbol and board[8] == symbol:
            return True

        # Check diagonals
        if board[0] == symbol and board[4] == symbol and board[8] == symbol:
            return True

        if board[2] == symbol and board[4] == symbol and board[6] == symbol:
            return True

        return False

    def check_draw(self):
        return " " not in self.board.board

    def start(self):
        print("Tic-Tac-Toe Game")
        print("-----------------")

        while True:
            self.board.display()

            print(
                f"{self.current_player.name}'s turn "
                f"({self.current_player.symbol})"
            )

            position = int(input("Choose position (1-9): "))

            index = position - 1

            if index < 0 or index > 8:
                print("Invalid position!")
                continue

            if self.board.board[index] != " ":
                print("Position already taken!")
                continue

            self.board.board[index] = self.current_player.symbol

            if self.check_winner():
                self.board.display()
                print(f"{self.current_player.name} wins!")
                break

            if self.check_draw():
                self.board.display()
                print("Game Draw!")
                break

            self.switch_player()