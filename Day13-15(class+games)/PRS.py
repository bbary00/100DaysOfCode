import sample_reader
from collections import OrderedDict
import random


"""Paper rock scissors game with 15 items"""


elements = OrderedDict(sorted(sample_reader.read_rolls().items()))
choices = list(elements.keys())


def compare(human, comp):
    print(f"Your choice is {human} and computer chose {comp}")
    if elements[human][comp] == "draw":
        return -1
    return elements[human][comp] == "win"


def game():
    lives = 3
    wins = 0

    while lives and wins != 3:
        for i, el in enumerate(choices, 1):
            print(f"{i}) {el}")
        i = int(input("Make your choice: "))
        res = compare(choices[i-1], random.choice(choices))
        if res is True:
            print("You win this round!")
            wins += 1
        elif res < 0:
            print("It's a draw. Continue...")
        else:
            print("You loose this round!")
            lives -= 1
        print('---------------------------------------')
        print("                Info                   ")
        print(f"Lives: {lives}, Wins: {wins}")
        print('---------------------------------------')

    if not lives:
        print("You loose all game. Try again")
    else:
        print("You are WINNER!!!")


if __name__ == '__main__':
    game()
