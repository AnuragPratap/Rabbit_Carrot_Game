import random
import msvcrt
import sys
import os
def random_map():
    pathWayStones ="-"
    map=[]
    map.extend([pathWayStones for i in range(50)])
    objects = random.sample(range(50), 3)
    map[objects[0]]="c"
    map[objects[1]]="r"
    map[objects[2]]="O"
    return map
def gamePlay(map):
    r=0
    for i in map:
        if i=='r':
            break
        r+=1
    while True:
        s=""
        s=s.join(map)
        sys.stdout.write("\r"+s)
        c = playInput()
        if(c==b'a' or c==b'A') and r>0 and map[r-1]=="-":
            map[r-1]=map[r]
            map[r]="-"
            r-=1
        elif(c==b'd' or c==b'D') and r<49 and map[r+1]=="-":
            map[r+1]=map[r]
            map[r]="-"
            r+=1
        elif(c==b'j' or c==b'J'):
            if(r<48 and map[r+1]=="O" and map[r+2]=="-"):
                map[r+2]=map[r]
                map[r]="-"
                r+=2
            elif (r>1 and map[r-1]=="O" and map[r-2]=="-"):
                map[r-2]=map[r]
                map[r]="-"
                r-=2
        elif(c==b'p' or c==b'P'):
            if(map[r+1]=="c"):
                map[r+1]="-"
                map[r]="R"
            elif(map[r-1]=="c"):
                map[r-1]="-"
                map[r]="R"
            elif(map[r+1]=="O" or map[r-1]=="O") and map[r]=="R":
                map[r]="r"
                sys.stdout.flush()
                s=""
                s=s.join(map)
                sys.stdout.write("\r"+s)
                break
        sys.stdout.flush()
def replay():
    print("\nPress Enter to play again and E to Exit")
    char = msvcrt.getch()
    if char==b'E' or char==b'\r' or char==b'e':
        return char
    else:
        print("\nWrong Input")
        return replay()
def playInput():
    char = msvcrt.getch()
    if char in [b'a',b'A',b'd',b'D',b'p',b'P',b'j',b'J']:
        return char
    else:
        return playInput()
while True:
    os.system('cls')
    map=random_map()
    gamePlay(map)
    char = replay()
    if char==b'E' or char==b'e':
        break
    elif char==b'\r':
        continue