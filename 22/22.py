#!/usr/bin/env python
from collections import defaultdict
from copy import deepcopy
from functools import cache
from sys import stdin
from pprint import pprint

f = open("in.raw", "r")
lines = f.read().splitlines()

# PART 1

DIRS=((0,1), (1,0), (0, -1), (-1,0))

def leftmost(map, y):
    x=0
    while map[y][x]==" ":
        x+=1
    return(x)

def rightmost(map, y):
    return(len(map[y])-1)

def topmost(map,x):
    y = 0
    while map[y][x]==" ":
        y+=1
    return(y)

def bottommost(map,x):
    y=len(map)-1
    while len(map[y]) <= x:
        y-=1
    while map[y][x] ==" ":
        y-=1
    return(y)

def step(map, p, dir):
    y=p[0]
    x=p[1]
    LIMITDETECT = (rightmost(map, y)==x, bottommost(map, x)==y, leftmost(map, y)==x, topmost(map,x)==y )
    if LIMITDETECT[dir]:
        next = ((y,leftmost(map,y)), (topmost(map,x),x), (y,rightmost(map,y)), (bottommost(map,x),x))[dir]
    else:
        next = (y+DIRS[dir][0], x+DIRS[dir][1])
    if map[next[0]][next[1]] == ".":
        return(next)
    elif map[next[0]][next[1]] == "#":
        return((y,x))
    else:
        print("FAIL")
        exit()

map=lines[:-2]
path=lines[-1]

pos=(0,leftmost(map,0))
i =0
steps = 0
while path[i] in "0123456789":
    steps = steps * 10 + int(path[i])
    i+=1
dir = 0
for _ in range(steps):
    pos=step(map,pos,dir)

while i<len(path):
    cd = path[i]
    if cd == "R":
        dir += 1
    elif cd == "L":
        dir -= 1
    else:
        print("FAIL2")
        exit()
    dir%=4
    i+=1
    steps = 0
    while i<len(path) and path[i] in "0123456789":
        steps = steps *10 + int(path[i])
        i+=1
    for _ in range(steps):
        pos=step(map,pos,dir)
    

print((pos[0]+1)*1000 + (pos[1]+1) * 4 + dir) 

# PART 2
result = 0
for line in lines:
    ...
print(result)
