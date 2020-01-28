from map import Map
from player import Player
from view import View
from cell import Cell
import time
#import sys
#from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

def GameOver():
    return False

def PlayerTurn(x = 0, y = 0, player = None):
    pass


player1 = Player()
# player1.Name = input("Введите имя Игрока1: ")
player1.name = "Тупой человечишка"
player1.type = Player.PLAYER_TYPE
player1.turn = Player.MY_TURN
player1.figure = Cell.ZERO

player2 = Player()
# player2.Name = input("Введите имя Игрока2: ")
# player2.type = input("Введите тип Игрока2 (1 - человек, 2 - комп): ")
player2.name = "Крутанский ИИ!"
player2.type = Player.BOT_TYPE
player2.turn = Player.NOTMY_TURN
player2.figure = Cell.CROSS

m = Map(6)
v = View(m)
v.ViewAll()

while not GameOver():
    if player1.turn == Player.MY_TURN:
        inp = (input(f"Ходит: {player1.name}, Введите координаты x,y : ").split(","))
        # turn
        player1.turn = Player.NOTMY_TURN
        player2.turn = Player.MY_TURN
    else:
        if player2.type == Player.BOT_TYPE:
            inp = ("0", "0")
            print(f"Ходит: {player2.name}, думает... ")
            time.sleep(2)
        else:
            inp = (input(f"Ходит: {player2.name}, Введите координаты x,y : ").split(","))
        # turn
        player2.turn = Player.NOTMY_TURN
        player1.turn = Player.MY_TURN
        
    v.ViewAll()

