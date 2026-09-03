class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def display_info(self):
        print(f"Player:{self.name}")
        print(f"Symbol:{self.symbol}")



player1 = Player("Sejal", "X")
player2 = Player("Sita", "O")

player1.display_info()
player2.display_info()