from cell import Cell

class Field:

    def __init__(self, size):
        self.size = size
        self.data = [[Cell.EMPTY for i in range(self.size)] for j in range(self.size)]

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


        # print(x_line)
        # print(y_line)
        # print(diag_1_line)
        # print(diag_2_line)


        for i in range(len(x_line)):
            if x_line[i] == type_player_cell:
                win = True

        for i in range(len(y_line)):
            if y_line[i] == type_player_cell:
                win = True

        for i in range(len(diag_1_line)):
            if diag_1_line[i] == type_player_cell:
                win = True

        for i in range(len(diag_2_line)):
            if diag_2_line[i] == type_player_cell:
                win = True



        return win


