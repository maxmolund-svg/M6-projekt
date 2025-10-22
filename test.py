from random import randint
import random
import math
#minesweeper M6


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
            #elif x2==(x1) and y2==(y1): samma kan ej vara närliggande
            #    adjacent+=1
            elif x2==(x1) and y2==(y1+1):
                adjacent+=1
            elif x2==(x1+1) and y2==(y1-1):
                adjacent+=1
            elif x2==(x1+1) and y2==(y1):
                adjacent+=1
            elif x2==(x1+1) and y2==(y1+1):
                adjacent+=1
        squares["noMines"][i].append(adjacent)


def testPrint(size): #trasig
    for x in range(size):
        width=math.isqrt(size)
        if x!=0 and math.floor(x/width)>math.floor((x-1)/width):
            print('\n',end="") 
        elif x==squares["mines"][x][0]:
            print("m",end="")
        elif x==squares["noMines"][x][0]:
            print(f"{squares['noMines'][x][4]}",end="")

def main():
    s=input("What size map would you like to play?(s,m or l): ")

    if s == "s":
        size = 5*5
    elif s == "m":
        size = 6*6
    else: 
        size = 7*7

    for n in range(size):
        width=math.isqrt(size)
        
        x=n%width
        
        if n==0:
            y=0 #solves divide by 0 error
        else:
            y=math.floor(n/width)

        squares["noMines"].append([n,(x,y),False,False])
        #print((x,y))

    m=int(input("How many mines would you like?: "))

    rng(m)
    
    findAdjacent()
    
    testPrint(size)
    #print(squares)

main()