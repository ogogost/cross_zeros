from map import Map
from player import Player
from view import View
from cell import Cell
import time
import random


def GameOver():
    result = None
    sum_pl1 = 0
    sum_pl2 = 0
    y = 0
    
    # ищем пустую клетку
    result = "over"
    for x in range(m.size):
        for y in range(m.size):
            if m.data[x][y].type == Cell.EMPTY:
                result = None
                break
    if result is not None: return result
    
    # ищем по вертикали нужное кол-во крестиков или ноликов
    while y < m.size:
        sum_pl1 = 0
        sum_pl2 = 0
        for x in range(m.size):
            if m.data[x][y].type == player1.figure: sum_pl1 += 1
            if m.data[x][y].type == player2.figure: sum_pl2 += 1
        if sum_pl1 == m.size: result = player1
        if sum_pl2 == m.size: result = player2
        y += 1
    if result is not None: return result
    
    # ищем по горизонтали нужное кол-во крестиков или ноликов
    sum_pl1 = 0
    sum_pl2 = 0
    y = 0
    while y < m.size:
        sum_pl1 = 0
        sum_pl2 = 0
        for x in range(m.size):
            if m.data[y][x].type == player1.figure: sum_pl1 += 1
            if m.data[y][x].type == player2.figure: sum_pl2 += 1
        if sum_pl1 == m.size: result = player1
        if sum_pl2 == m.size: result = player2
        y += 1
    if result is not None: return result
    
    #ищем по диагонали
    sum_pl1 = 0
    sum_pl2 = 0
    for x in range(m.size):
        if m.data[x][x].type == player1.figure: sum_pl1 += 1
        if m.data[x][x].type == player2.figure: sum_pl2 += 1
    if sum_pl1 == m.size: result = player1
    if sum_pl2 == m.size: result = player2
    if result is not None: return result
    
    # ищем по обратной диагонали
    sum_pl1 = 0
    sum_pl2 = 0
    y = m.size-1
    for x in range(m.size):
        if m.data[y][x].type == player1.figure: sum_pl1 += 1
        if m.data[y][x].type == player2.figure: sum_pl2 += 1
        y -= 1
    if sum_pl1 == m.size: result = player1
    if sum_pl2 == m.size: result = player2
    return result

def GetBotTurn():

    while True:
        result=[]
        result.clear()
        result.append(random.randint(1, m.size))
        result.append(random.randint(1, m.size))
        if CanIMakeThisTurn(result[0], result[1]):
            break
    return result

# проедура в которой обрабатывается ход
def PlayerTurn(x = 0, y = 0, player = None):
    if player.type == Player.PLAYER_TYPE: # если человек
        m.data[x-1][y-1].type = player.figure
    else: # если комп
        res = GetBotTurn()
        m.data[res[0]-1][res[1]-1].type = player.figure

def CanIMakeThisTurn(x, y):
    if x > m.size or y > m.size or y<=0 or x<=0: return False
    if m.data[x - 1][y - 1].type == Cell.EMPTY:
        return True
    else:
        return False
        

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


while GameOver() == None: # цикл, ход за ходом, пока процедура GameOver не вернет какого нибудь инг
    if player1.turn == Player.MY_TURN: # Если ход первого игрока
        while True:
            inp = (input(f"Ходит: {player1.name}, Введите координаты x,y : ").split(","))
            if CanIMakeThisTurn(int(inp[0]), int(inp[1])) == True:
                break
        PlayerTurn(x=int(inp[0]), y=int(inp[1]), player=player1)
        player1.turn = Player.NOTMY_TURN
        player2.turn = Player.MY_TURN
    else:  # Если ход второго играка
        if player2.type == Player.BOT_TYPE: # Если второй игрок бот
            inp = ("0", "0")
            print(f"Ходит: {player2.name}, думает... ")
            time.sleep(2)
        else: # Если не бот
            while True:
                inp = (input(f"Ходит: {player2.name}, Введите координаты x,y : ").split(","))
                if CanIMakeThisTurn(int(inp[0]), int(inp[1])) == True:
                    break
                    
        PlayerTurn(x=int(inp[0]), y=int(inp[1]), player=player2)
        player2.turn = Player.NOTMY_TURN
        player1.turn = Player.MY_TURN
        
    v.ViewAll()

if isinstance(GameOver(), Player) :
    print("Победа!!!! : " + GameOver().name)
else:
    print("Ничья!!! ")
