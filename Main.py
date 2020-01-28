import map
from player import Player
import view
#import sys
#from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel


player1 = Player()
player1.Name = input("Введите имя Игрока1: ")
player1.type = 1

player2 = Player()
player2.Name = input("Введите имя Игрока2: ")
player2.type = input("Введите тип Игрока2 (1 - человек, 2 - комп): ")

