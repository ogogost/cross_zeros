
import random
import time
win = 0
print("Welcome to our best casino in the world!")
print("You must try to guess kubik number, it is random factor")

while win == 0:

    player1_input = int(input("Player1 input number:"))
    player2_input = int(input("Player2 input number:"))
    kubik = random.randint(1,6)
    # print('Three')
    # time.sleep(1)
    # print('Two')
    # time.sleep(1)
    # print('One')
    # time.sleep(1)
    print("Kubik number is:", kubik)

    if player1_input == kubik:
        print("Player 1 win!")
        win = 1
    elif player2_input == kubik:
        print("Player 2 win!")
        win = 1
    else:
        print("Nobody win, play again")