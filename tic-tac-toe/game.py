from player import Player
from board import Board


class Game:
    def __init__(self):
        # Create board
        self.board = Board()

        # Create players
        self.player1 = Player("Sejal", "X")
        self.player2 = Player("Sita", "O")

        # First turn belongs to player 1
        self.current_player = self.player1

    def switch_player(self):
        # Change current player
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
        # If no empty space remains, game is draw
        return " " not in self.board.board

    def start(self):
        print("Tic-Tac-Toe Game")
        print("-----------------")

        while True:
            # Display current board
            self.board.display()

            # Show current player's turn
            print(
                f"{self.current_player.name}'s turn "
                f"({self.current_player.symbol})"
            )

            # Get position from user
            try:
                position = int(input("Choose position (1-9): "))
            except ValueError:
                print("Please enter a number between 1 and 9!")
                continue

            # Convert position to list index
            index = position - 1

            # Check valid position
            if index < 0 or index > 8:
                print("Invalid position! Choose between 1 and 9.")
                continue

            # Check whether position is already occupied
            if self.board.board[index] != " ":
                print("Position already taken!")
                continue

            # Put player's symbol on board
            self.board.board[index] = self.current_player.symbol

            # Check winner
            if self.check_winner():
                self.board.display()
                print(f"{self.current_player.name} wins!")
                break

            # Check draw
            if self.check_draw():
                self.board.display()
                print("Game Draw!")
                break

            # Switch player
            self.switch_player()