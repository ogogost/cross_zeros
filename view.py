from map import Map

class View():
    def __init__(self, map):
        self.map = map
        
        
    def ViewAll(self):
        for row in self.map.data:
            print("", end="\n")
            for cell in row:
                print(str(cell.type), end=" ")

        print("", end="\n")
