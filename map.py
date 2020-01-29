from cross_zeros.cell import Cell

class Field:

    def __init__(self, size):
        self.data = [[Cell.EMPTY for i in range(size)] for j in range(size)]
        self.size = size

    def calculate_win(self, x, y, type_player_cell): # функция проверки на победу
        win = False

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

        for i in range(len(x_line))
        if x_line[i] == type_player_cell:
            win = True

        # if x_line[0] == x_line[1] and x_line[0] == x_line[2]: win = True
        # if y_line[0] == y_line[1] and y_line[0] == y_line[2]: win = True
        # if diag_1_line[0] == diag_1_line[1] and diag_1_line[0] == diag_1_line[2]: win = True
        # if diag_2_line[0] == diag_2_line[1] and diag_2_line[0] == diag_2_line[2]: win = True

        return win
