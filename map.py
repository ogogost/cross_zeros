from cell import Cell

class Map():
    def __init__(self, size):
        self.data = [[Cell() for i in range(size)] for i in range(size)]
        self.size = size
        #self.isEven = True if self.size % 2 == 0 else False



