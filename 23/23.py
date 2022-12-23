#!/usr/bin/env python
from collections import defaultdict
from copy import deepcopy
from functools import cache
from sys import stdin
from pprint import pprint

f = open("test.raw", "r")
lines = f.read().splitlines()

Y=0
X=1
# PART 1
def move(elfs, dirs):
    newocu = set()
    collisions = set()
    newelfs = set()
    AROUND = (
        (-1,-1),(-1,0), (-1,1),
        ( 0,-1),        ( 0,1),
        ( 1,-1),( 1,0), ( 1,1),
    )
    for elf in elfs:
        d = 0
        while d<4 and any(((elf[Y]+dirs[d][i][Y],elf[X]+dirs[d][i][X]) in elfs for i in range(3))):
            d+=1
        if (d==0 and all(((elf[Y]+AROUND[i][Y],elf[X]+AROUND[i][X]) not in elfs for i in range(8))))\
            or d>=4:
            newocu.add(elf)
        else:
            oldlen = len(newocu)
            newocu.add((elf[Y]+dirs[d][1][Y],elf[X]+dirs[d][1][X]))
            if oldlen == len(newocu):
                collisions.add((elf[Y]+dirs[d][1][Y],elf[X]+dirs[d][1][X]))
    for elf in elfs:
        d = 0
        while d<4 and any(((elf[Y]+dirs[d][i][Y],elf[X]+dirs[d][i][X]) in elfs for i in range(3))):
            d+=1
        if (d==0 and all(((elf[Y]+AROUND[i][Y],elf[X]+AROUND[i][X]) not in elfs for i in range(8))))\
            or d>=4 \
            or (elf[Y]+dirs[d][1][Y],elf[X]+dirs[d][1][X]) in collisions:
            newelfs.add(elf)
        else:
            newelfs.add((elf[Y]+dirs[d][1][Y],elf[X]+dirs[d][1][X]))
    return(newelfs)
    
def printmap(elfs):
    return()
    map=[["."]*20 for _ in range(20)]
    for elf in elfs:
        map[elf[Y]+4][elf[X]+4] = "#"
    for line in map:
        print("".join(line))

elfs=set()
for y, row in enumerate(lines):
    for x, cell in enumerate(row):
        if cell == "#":
            elfs.add((y,x))
dirs=[
    ((-1,-1),(-1, 0),(-1, 1)),
    (( 1,-1),( 1, 0),( 1, 1)),
    ((-1,-1),( 0,-1),( 1,-1)),
    ((-1, 1),( 0, 1),( 1, 1))
]

printmap(elfs)
pprint(dirs)
for i in range(100000):
    newelfs = move(elfs, dirs)
    if len(newelfs.difference(elfs))==0:
        print(i)
        exit()
    #printmap(elfs)
    dirs=dirs[1:]+dirs[:1]
    #pprint(dirs)
    elfs=newelfs


maxx=-999999999999
maxy=-999999999999
minx=999999999999
miny=999999999999

for elf in elfs:
    minx=min(minx,elf[X])
    maxx=max(maxx,elf[X])
    miny=min(miny,elf[Y])
    maxy=max(maxy,elf[Y])

print(maxx,minx,maxy,miny)

print((maxx-minx+1)*(maxy-miny+1) - len(elfs))

# PART 2
result = 0
for line in lines:
    ...
print(result)
