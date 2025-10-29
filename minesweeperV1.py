# -------------------------------------------------------------------------------------------------
# Minesweeper
# Terminal (i.e. python shell) text based game.
# Created for module 6 of the course "Introduktion till informationsteknik" at Uppsala University
# By Max Molund and Ture Nilsson
#--------------------------------------------------------------------------------------------------
import random
import math

squares={"mines":[],"noMines":[]}

def rng(mines):
    
    squares["mines"] = random.sample(squares["noMines"], mines)
    for mine in squares["mines"]:
        squares["noMines"].remove(mine)

def findAdjacent():
    for i in range(len(squares["noMines"])):
        x1=squares["noMines"][i][1][0]
        y1=squares["noMines"][i][1][1]
        adjacent=0
        for j in range(len(squares["mines"])):
            x2=squares["mines"][j][1][0]
            y2=squares["mines"][j][1][1]
            if x2==(x1-1) and y2==(y1-1):
                adjacent+=1
            elif x2==(x1-1) and y2==(y1):
                adjacent+=1
            elif x2==(x1-1) and y2==(y1+1):
                adjacent+=1   
            elif x2==(x1) and y2==(y1-1):
                adjacent+=1
            elif x2==(x1) and y2==(y1+1):
                adjacent+=1
            elif x2==(x1+1) and y2==(y1-1):
                adjacent+=1
            elif x2==(x1+1) and y2==(y1):
                adjacent+=1
            elif x2==(x1+1) and y2==(y1+1):
                adjacent+=1
        squares["noMines"][i].append(adjacent)

def clearAdjacent(cord):
    x1=cord[0]
    y1=cord[1]
    for i in range(len(squares["noMines"])):
        x2=squares["noMines"][i][1][0]
        y2=squares["noMines"][i][1][1]
        if x2==(x1-1) and y2==(y1-1) and squares["noMines"][i][2]==False:
            squares["noMines"][i][2]=True
            revealed.add(squares["noMines"][i][0])
            if squares["noMines"][i][4]==0:
                clearAdjacent(squares["noMines"][i][1])
        elif x2==(x1-1) and y2==(y1) and squares["noMines"][i][2]==False:
            squares["noMines"][i][2]=True
            revealed.add(squares["noMines"][i][0])
            if squares["noMines"][i][4]==0:
                clearAdjacent(squares["noMines"][i][1])
        elif x2==(x1-1) and y2==(y1+1) and squares["noMines"][i][2]==False:
            squares["noMines"][i][2]=True
            revealed.add(squares["noMines"][i][0])
            if squares["noMines"][i][4]==0:
                clearAdjacent(squares["noMines"][i][1])
        elif x2==(x1) and y2==(y1-1) and squares["noMines"][i][2]==False:
            squares["noMines"][i][2]=True
            revealed.add(squares["noMines"][i][0])
            if squares["noMines"][i][4]==0:
                clearAdjacent(squares["noMines"][i][1])
        elif x2==(x1) and y2==(y1+1) and squares["noMines"][i][2]==False:
            squares["noMines"][i][2]=True
            revealed.add(squares["noMines"][i][0])
            if squares["noMines"][i][4]==0:
                clearAdjacent(squares["noMines"][i][1])
        elif x2==(x1+1) and y2==(y1-1) and squares["noMines"][i][2]==False:
            squares["noMines"][i][2]=True
            revealed.add(squares["noMines"][i][0])
            if squares["noMines"][i][4]==0:
                clearAdjacent(squares["noMines"][i][1])
        elif x2==(x1+1) and y2==(y1) and squares["noMines"][i][2]==False:
            squares["noMines"][i][2]=True
            revealed.add(squares["noMines"][i][0])
            if squares["noMines"][i][4]==0:
                clearAdjacent(squares["noMines"][i][1])
        elif x2==(x1+1) and y2==(y1+1) and squares["noMines"][i][2]==False:
            squares["noMines"][i][2]=True
            revealed.add(squares["noMines"][i][0])
            if squares["noMines"][i][4]==0:
                clearAdjacent(squares["noMines"][i][1])

def printNoFog(size):
    print('\n',end="")
    width=math.isqrt(size)
    for x in range(size):
        if x!=0 and (x%width)==0:
            #new row
            print('\n',end="") 
        for n in range(len(squares["mines"])):
            if x==squares["mines"][n][0]:
                #mine
                print("m",end="")
        for n in range(len(squares["noMines"])):
            if x==squares["noMines"][n][0]:
                #number of adjacent mines
                print(f"{squares['noMines'][n][4]}",end="")

revealed = set()
flagged=set()

def game():

    s=input("What size map would you like to play?(s,m or l): ")

    if s == "s":
        size = 5*5
    elif s == "m":
        size = 9*9
    else: 
        size = 16*16

    for n in range(size):
        width=math.isqrt(size)
        
        x=n%width
        
        if n==0:
            y=0 #solves divide by 0 error
        else:
            y=math.floor(n/width)

        squares["noMines"].append([n,(x,y),False,False])
        #första bool (index 2) är om grävd; andra (index 3) är om flaggad
        # #print((x,y))

    m=int(input("How many mines would you like?: "))
    rng(m)
    findAdjacent()
        
    width=math.isqrt(size)
    
    while True:
        print("\nCurrent board:")
        for i in range(size):
            if i % width == 0:
                print()
            if i in revealed:
                    num = [sq[4] for sq in squares["noMines"] if sq[0] == i][0]
                    print(num, end="")
            elif i in flagged:
                print("+",end="")
            else:
                print("X", end="")
        print("\n")
        while True:
            try:
                x = int(input("Enter X coordinate: "))
                y = int(input("Enter Y coordinate: "))
                break
            except ValueError: print("Please choose valid coordinates!")
        target = None
        for sq in squares["noMines"] + squares["mines"]:
            if sq[1] == (x, y):
                target = sq
                break
        if target is None:
            print("Invalid coordinates!")
            continue
        
        

        t = input("Do you want to dig (d) or flag (f)?: ")
        if t=="f":
            for n in range(len(squares["mines"])):
                if target==squares["mines"][n]:
                    if squares["mines"][n][3]==True:
                        squares["mines"][n][3]=False
                        flagged.remove(target[0])
                        break
                    elif squares["mines"][n][3]==False:
                        squares["mines"][n][3]=True
                        flagged.add(target[0])
                        break
            for n in range(len(squares["noMines"])):
                if target==squares["noMines"][n]:
                    if target==squares["noMines"][n]:
                        if squares["noMines"][n][3]==True:
                            squares["noMines"][n][3]=False
                            flagged.remove(target[0])
                            break
                        elif squares["noMines"][n][3]==False:
                            squares["noMines"][n][3]=True
                            flagged.add(target[0])
                            break
        elif t=="d":
            if target[3]==True:
                print("You can't dig a flag. To remove it, use the flag action on this square again")
                continue
            if target in squares["mines"]:
                print("You hit a mine!")
                print("Game Over!")
                print("This was your board:")
                printNoFog(size)
                break
            else:
                revealed.add(target[0])
                for n in range(len(squares["noMines"])):
                    if squares["noMines"][n]==target:
                        squares["noMines"][n][2]=True
                    if target[4]==0:
                        clearAdjacent(target[1])
            if len(revealed) == len(squares["noMines"]):
                print("You win!")
                print("This was your board:")
                printNoFog(size)
                break
        else:
            print("invalid action")
            continue

def main():
    s=input("What size map would you like to play?(s,m or l): ")

    if s == "s":
        size = 5*5
    elif s == "m":
        size = 9*9
    else: 
        size = 16*16

    for n in range(size):
        width=math.isqrt(size)
        
        x=n%width
        
        if n==0:
            y=0 #solves divide by 0 error
        else:
            y=math.floor(n/width)

        squares["noMines"].append([n,(x,y),False,False])
       #first bool (index 2) is if dug; second (index 3) is if flagged
       

    m=int(input("How many mines would you like?: "))

    rng(m)
    
    findAdjacent()

    game(size)

main()
