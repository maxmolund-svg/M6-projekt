from random import randint

#minesweeper M6

squares={"mines":[],"noMines":[]}

def rng(a, b):
    size = a*a
    for i in range (1, b-1):
        mine = randint(0, size)
        