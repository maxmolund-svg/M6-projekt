from random import randint

#minesweeper M6

squares={"mines":[],"noMines":[]}

def rng(size, mines):
    
    for i in range (1, mines-1):
        mine = randint(0, size)
        