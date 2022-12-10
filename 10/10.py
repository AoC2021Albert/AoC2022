#!/usr/bin/env python
from collections import defaultdict
from copy import deepcopy
from functools import cache
from sys import stdin
from pprint import pprint

f = open("in.raw", "r")
lines = f.read().splitlines()

# PART 1
result = 0
cycle=0
interesting=[20,60,100,140,180,220]
#interesting=[1,2,3,4,5,6,7]
interestingpos=0
currentval=1


def check(interesting,cycle,currentval):
    global interestingpos
    global result
    if interestingpos>=len(interesting):
        return(0)
    if cycle >= interesting[interestingpos]:
        mul=interesting[interestingpos]*currentval
        print(f'cycle: {cycle}, interestingcycle: {interesting[interestingpos]}, currentval: {currentval}, mul: {mul}')
        interestingpos+=1
        return(mul)
    else:
        return(0)

for line in lines:
    if line=="noop":
        cycle += 1
        result+=check( interesting,cycle,currentval)
    else:
        cycle += 2
        result+=check( interesting,cycle,currentval)
        currentval+=int(line.split(" ")[1])
if interestingpos<len(interesting):
    result+=currentval
print(result)

# PART 2
result = 0
cycle=0
currentval=1
HSIZE=40
VSIZE=6
screen=[[" "]*HSIZE for _ in range(VSIZE)]

def draw(currentval,screen):
    global cycle
    y=(cycle // HSIZE) % VSIZE 
    x=cycle % HSIZE
    print(f'x is {x}, currentval is {currentval}')
    if currentval - 1 <= x <= currentval +1:
        print(f'painting at {x},{y}')
        screen[y][x] = "#"
    cycle+=1
    
for line in lines:
    if line=="noop":
        draw(currentval,screen)
    else:
        draw(currentval,screen)
        draw(currentval,screen)
        currentval+=int(line.split(" ")[1])
for row in screen:
    print("".join(row))

