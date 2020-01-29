from cell import Cell
from view import View
from map import Field
from player import Player


class Controller:
    def __init__(self):
        self.field = Field(3)
        self.view = View(self.field)

    def get_user_turn(self):
        try:
            x = int(input("X: "))
            y = int(input("Y: "))

            if x < 0 or x >= self.field.size:
                return None
            if y < 0 or y >= self.field.size:
                return None

            if self.field.data[x][y] != Cell.EMPTY:
                return None
            return x, y
        except:
            return None

    def select_opponent_type(self):  # функция выбора типа оппонента
        opponent_type = input("Choose your opponent: \n 1. Player2 \n 2. Bot \n 3. AI \n ")
        if opponent_type == "1":
            self.type_player = "Player 2"
        elif opponent_type == "2":
            self.type_player = "Bot"
        elif opponent_type == "3":
            self.type_player = "AI"
        else:
            pass
        print(self.type_player)

    # def select_map_size(self):
    #     n = int(input("Input map size (for more experience prefer 3, 5, 7, 9...) : "))
    #     field = Field(n)

    def start_game(self):
        # self.select_opponent_type()
        # self.select_map_size()

        while win == 0:  # основной цикл игры

            self.view.display_field()  # отображаем поле
            type_player_cell = Cell.CROSS  # назначаем крестики первому игроку
            player1_input = self.get_user_turn()  # первый игрок вводит свои координаты

            if player1_input is None:  # проверка координат на валидность
                print("Wrong coords! Retry!")
                continue

            self.field.data[player1_input[0]][player1_input[1]] = type_player_cell  # вставка крестика на поле

            if self.field.calculate_win(player1_input[0], player1_input[1],
                                        type_player_cell):  # проверка хода на победу
                print("Player 1 win!")
                break

            self.view.display_field()
            type_player_cell = Cell.ZERO  # назначаем нолики второму игроку
            player2_input = self.get_user_turn()  # второй игрок вводит свои координаты

            if player2_input is None:  # проверка координат на валидность
                print("Wrong coords! Retry!")
                continue

            self.field.data[player2_input[0]][player2_input[1]] = type_player_cell  # вставка нолика на поле

            if self.field.calculate_win(player2_input[0], player2_input[1],
                                        type_player_cell) == True:  # проверка хода на победу
                print("Player 2 win!")
                break



# type_player_cell = Cell.EMPTY
win = 0
ctrl = Controller()
ctrl.start_game()

# get_user_turn()
