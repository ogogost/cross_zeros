class Cell:
    EMPTY = '_'
    CROSS = 'X'
    ZERO = 'O'
    def __init__(self, s = EMPTY):
        self.status = s
