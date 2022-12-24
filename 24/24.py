#!/usr/bin/env python
from collections import defaultdict
from copy import deepcopy
from functools import cache
from sys import stdin
from pprint import pprint

f = open("in.raw", "r")
lines = f.read().splitlines()
Y=0
X=1

DIRSSTRING="^>v<"
DIRS=(
    (-1,0),
    (0,1),
    (1,0),
    (0,-1)
)
class Point:
    def __init__(self, y, x) -> None:
        self.p = (y,x)

class Blizzard(Point):
    def __init__(self, y, x, dir) -> None:
        super().__init__(y, x)
        self.dir = dir

    def step(self):
        newy = self.p[Y]+DIRS[self.dir][Y]
        newx = self.p[X]+DIRS[self.dir][X]
        if newy==UPWALL:
            newy=DOWNMOST
        elif newy==DOWNWALL:
            newy=UPMOST
        if newx==RIGHTWALL:
            newx=LEFTMOST
        elif newx==LEFTWALL:
            newx=RIGHTMOST
        self.p=(newy,newx)



# PART 1
steps = 0
blizzards = []
for y, line in enumerate(lines):
    for x, p in enumerate(line):
        if p in DIRSSTRING:
            dir = DIRSSTRING.index(p)
            blizzards.append(Blizzard(y,x, dir))



def move(blizzards,positions, START, END):
    def valid(y,x):
        if (y,x) in [START,END]:
            return(True)
        if y in [UPWALL, DOWNWALL]:
            return(False)
        if x in [LEFTWALL, RIGHTWALL]:
            return(False)
        return(True)

    actiblizzard = set()
    # move blizzards
    for blizzard in blizzards:
        blizzard.step()
        actiblizzard.add(blizzard.p)
    newpositions = set()
    for position in positions:
        newpositions.add(position)
        for dir in range(len(DIRS)):
            newy = position[Y]+DIRS[dir][Y]
            newx = position[X]+DIRS[dir][X]
            if valid(newy,newx):
                newpositions.add((newy,newx))

    newpositions.difference_update(actiblizzard)
    return(newpositions)


UPWALL=0
LEFTWALL=0
DOWNWALL=len(lines)-1
RIGHTWALL=len(lines[0])-1
UPMOST=UPWALL+1
DOWNMOST=DOWNWALL-1
LEFTMOST=LEFTWALL+1
RIGHTMOST=RIGHTWALL-1

START=(UPWALL,LEFTMOST)
END=(DOWNWALL,RIGHTMOST)

positions=set([START])
while END not in positions:
    steps+=1
    print(steps)
    positions = move(blizzards, positions,START,END)

positions=set([END])
while START not in positions:
    steps+=1
    print(steps)
    positions = move(blizzards, positions,START,END)

print("START")
positions=set([START])
while END not in positions:
    steps+=1
    print(steps)
    positions = move(blizzards, positions,START,END)

print(steps)
