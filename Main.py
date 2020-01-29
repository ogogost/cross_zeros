from cross_zeros.cell import Cell
from cross_zeros.view import View
from cross_zeros.map import Field
from cross_zeros.player import Player

class Controller:
    def __init__(self):
        self.field = Field()
        self.view = View()


    def get_user_turn(self):
        try:
            x = int(input("X: "))
            y = int(input("Y: "))

            if x < 0 or x >= self.field.size:
                return None
            if y < 0 or y >= self.field.size:
                return None
            return x, y
        except:
            return None

    def select_opponent_type(self):
        opponent_type = input("Choose your opponent: \n 1. Player2 \n 2. Bot \n 3. AI \n ")
        if opponent_type == "1":
            self.type_player = "Player 2"
        elif opponent_type == "2":
            self.type_player = "Bot"
        elif opponent_type == "3":
            self.type_player = "AI"
        else:
            pass
        print(self.type_player)


    def start_game(self):
        self.select_opponent_type()
        while True:
            self.view.display_field()
            coords = self.get_user_turn()
            if coords is None:
                print("Wrong coords! Retry!")
                continue
            win_result = self.field.calculate_win(coords[0],coords[1])
            if win_result == 1:
                print("Player" + self.Player.name + "win!")
            else:
                pass
ctrl = Controller()
ctrl.start_game()

