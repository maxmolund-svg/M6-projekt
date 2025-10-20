from random import randint
import random
#minesweeper M6


squares={"mines":[],"noMines":[]}


def rng(mines):
    
    squares["mines"] = random.sample(squares["noMines"], mines)
    for mine in squares["mines"]:
        squares["noMines"].remove(mine)




def main():
    s=input("What size map would you like to play?(s,m or l): ")

    if s == "s":
        size = 5*5
    elif s == "m":
        size = 6*6
    else: s = 7*7

    squares["noMines"] = list(range(size))

    m=int(input("How many mines would you like?: "))
    rng(m)

