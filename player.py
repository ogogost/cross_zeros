from cell import Cell

class Player():
    BOT_TYPE = 2
    PLAYER_TYPE = 1
    
    MY_TURN = 1
    NOTMY_TURN = 0
    
    def __init__(self):
        self.name = ""
        self.type = self.PLAYER_TYPE
        self.turn = self.MY_TURN
        self.figure = Cell.EMPTY