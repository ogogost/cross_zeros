import cell

class Map():
    def __init__(self, size):
        self.data = [[cell(i) for i in range(1, size - 1)] for i in range(1, size - 1)]
        self.size = size
        #self.isEven = True if self.size % 2 == 0 else False



