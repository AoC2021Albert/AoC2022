#!/usr/bin/env python
from collections import defaultdict
from copy import deepcopy
from functools import cache
from sys import stdin
from pprint import pprint

f = open("in.raw", "r")
lines = f.read().splitlines()
MAX=22
# PART 1
result = 0
SPACE=  0
SOLID = 1
EXTERIOR = 2
droplet=[[[SPACE for _ in range(MAX)]for _ in range(MAX)]for _ in range(MAX)]
for line in lines:
    x,y,z=(int(v) for v in line.split(","))
    droplet[x+1][y+1][z+1] = SOLID
import sys
sys.setrecursionlimit(MAX*MAX*MAX)

def exteriorflood(droplet, x, y , z):
    if 0<=x<MAX and 0<=y<MAX and 0<=z<MAX:
        if droplet[x][y][z] == SPACE:
            droplet[x][y][z] = EXTERIOR
            for dx,dy,dz in ((0,0,1),
                        (0,0,-1),
                        (0,1,0),
                        (0,-1,0),
                        (1,0,0),
                        (-1,0,0)):
                exteriorflood(droplet,x+dx,y+dy,z+dz)

exteriorflood(droplet,0,0,0)
for x in range(1,MAX):
    for y in range(1,MAX):
        for z in range(1,MAX):
            if droplet[x][y][z]==SOLID:
                for dx,dy,dz in ((0,0,1),
                      (0,0,-1),
                      (0,1,0),
                      (0,-1,0),
                      (1,0,0),
                      (-1,0,0)):
                    if droplet[x+dx][y+dy][z+dz]==EXTERIOR:
                        result+=1

                      


print(result)
