from map import Map
from player import Player
from view import View
from cell import Cell
import time
#import sys
#from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

def GameOver():
    return False

# проедура в которой обрабатывается ход
def PlayerTurn(x = 0, y = 0, player = None):
    if player.type == Player.PLAYER_TYPE: # если человек
        m.data[x-1][y-1].type = player.figure
    else: # если комп
        m.data[2-1][2-1].type = player.figure


# параметры первого игрока, потом будут воодиться, пока хардом
player1 = Player()
# player1.Name = input("Введите имя Игрока1: ")
player1.name = "Тупой человечишка"
player1.type = Player.PLAYER_TYPE
player1.turn = Player.MY_TURN
player1.figure = Cell.ZERO

# параметры второго игрока, потом будут воодиться, пока хардом
player2 = Player()
# player2.Name = input("Введите имя Игрока2: ")
# player2.type = input("Введите тип Игрока2 (1 - человек, 2 - комп): ")
player2.name = "Крутанский ИИ!"
player2.type = Player.BOT_TYPE
player2.turn = Player.NOTMY_TURN
player2.figure = Cell.CROSS

# создаем поле 6х6
m = Map(6)
# создаем вьювир и показываем пустое поле
v = View(m)
v.ViewAll()

while not GameOver(): # цикл, ход за ходом, пока процедура GameOver не вернет TRUE
    if player1.turn == Player.MY_TURN: # Если ход первого игрока
        inp = (input(f"Ходит: {player1.name}, Введите координаты x,y : ").split(","))
        PlayerTurn(x=int(inp[0]), y=int(inp[1]), player=player1)
        player1.turn = Player.NOTMY_TURN
        player2.turn = Player.MY_TURN
    else:  # Если ход второго играка
        if player2.type == Player.BOT_TYPE: # Если второй игрок бот
            inp = ("0", "0")
            print(f"Ходит: {player2.name}, думает... ")
            time.sleep(2)
        else: # Если не бот
            inp = (input(f"Ходит: {player2.name}, Введите координаты x,y : ").split(","))
        PlayerTurn(x=int(inp[0]), y=int(inp[1]), player=player2)
        player2.turn = Player.NOTMY_TURN
        player1.turn = Player.MY_TURN
        
    v.ViewAll()

