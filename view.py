from cross_zeros.map import Field
from cross_zeros.player import Player

class View:
    def __init__(self):
        self.field = Field()

    def display_field(self):
        [print(self.field.data[i]) for i in range(len(self.field.data))]

    # def display_players_status:
    #     print("Player 1 :", self.player.type_player)
