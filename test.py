from random import randint
import random
#minesweeper M6


squares={"mines":[],"noMines":[]}


def rng(size, mines):

    if size == "s":
        map = 5*5
    elif size == "m":
        map = 6*6
    else: map == 7*7
    

    for i in range (1, mines-1):
        mine = randint(0, map)
        


def main():
    s=input("What size map would you like to play?(s,m or l): ")
    m=input("How many mines would you like?: ")
    rng(s,m)

