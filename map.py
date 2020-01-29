from cross_zeros.cell import Cell

class Field:

    def __init__(self, size =3):
        self.data = [[Cell.EMPTY for i in range(size)] for j in range(size)]
        self.size = size

    def calculate_win(self, x, y): # функция проверки на победу
        x_line = []
        y_line = []
        diag_1_line = []
        diag_2_line = []

        for i in range(len(self.data)):
            x_line.append(self.data[i][y]) # заполняем горизонтальную линию
        for j in range(len(self.data)):
            y_line.append(self.data[x][j]) # заполняем вертикальную линию
        for r in range(len(self.data)):
            diag_1_line.append(self.data[r][r]) # заполняем первую диагональную линию
        for t in range(len(self.data)):
            diag_2_line.append(self.data[t][-t-1])  # заполняем первую диагональную линию
        print("x_line:", x_line)
        print("y_line:", y_line)
        print("diag_1_line:", diag_1_line)
        print("diag_2_line:", diag_2_line)

# field = Field()
# field.data[0][0] = Cell.CROSS
# field.data[0][1] = Cell.CROSS
# field.data[0][2] = Cell.ZERO
# field.data[1][0] = Cell.ZERO
# field.data[1][1] = Cell.CROSS
# field.data[1][2] = Cell.CROSS
# field.data[2][0] = Cell.ZERO
# field.data[2][1] = Cell.ZERO
# field.data[2][2] = Cell.CROSS

# field.calculate_win(1,1)


# print("Map here:")
# [print(field.data[i]) for i in range(len(field.data))]



