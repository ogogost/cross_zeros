
class Cell():
    EMPTY = '*'
    CROSS = 'X'
    ZERO = 'O'
    def __init__(self, type = EMPTY):
        self.type = type