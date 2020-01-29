from cell import Cell

class Map():
    def __init__(self, size):
        self.data = [[Cell() for i in range(size)] for i in range(size)]
        #print(self.data)
        #self.data = [[Cell(), Cell(), Cell(type=Cell.ZERO)], [Cell(), Cell(type=Cell.CROSS), Cell(type=Cell.ZERO)], [Cell(), Cell(type=Cell.CROSS), Cell(type=Cell.ZERO)]]
        # self.data = [[Cell(), Cell(), Cell()],
        #              [Cell(), Cell(type=Cell.CROSS), Cell(type=Cell.CROSS)],
        #              [Cell(type=Cell.ZERO), Cell(type=Cell.ZERO), Cell(type=Cell.ZERO)]]
        self.size = size
        #self.isEven = True if self.size % 2 == 0 else False



