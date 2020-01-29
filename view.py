from map import Field
from player import Player

class View:
    def __init__(self, field):
        self.field = field

    def display_field(self):
        [print(self.field.data[i]) for i in range(len(self.field.data))]

    # def display_players_status:
    #     print("Player 1 :", self.player.type_player)


# f = Field(7)
# view = View(f)
#
# view.display_field()