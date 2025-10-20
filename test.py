from random import randint
import random
#minesweeper M6


squares={"mines":[],"noMines":[]}


def rng(size, mines):

    for i in range (mines-1):
        mine = randint(0, size-1)
        squares["noMines"].remove(mine)
        squares["mines"].append(mine)


def main():
    s=input("What size map would you like to play?(s,m or l): ")

    if s == "s":
        size = 5*5
    elif s == "m":
        size = 6*6
    else: s == 7*7

    squares["noMines"] = list(range(size))

    m=input("How many mines would you like?: ")
    rng(size,m)

