#!/usr/bin/env python
import sys
from collections import defaultdict
from copy import deepcopy
from functools import cache
from sys import stdin
from pprint import pprint

MAX = 22
SPACE = 0
SOLID = 1
EXTERIOR = 2

sys.setrecursionlimit(MAX*MAX*MAX)


def exteriorflood(droplet, x, y, z):
    if 0 <= x < MAX and 0 <= y < MAX and 0 <= z < MAX:
        if droplet[x][y][z] == SPACE:
            droplet[x][y][z] = EXTERIOR
            for dx, dy, dz in ((0, 0, 1),
                               (0, 0, -1),
                               (0, 1, 0),
                               (0, -1, 0),
                               (1, 0, 0),
                               (-1, 0, 0)):
                exteriorflood(droplet, x+dx, y+dy, z+dz)


def countadjacent(droplet, kind):
    result = 0
    for x in range(1, MAX):
        for y in range(1, MAX):
            for z in range(1, MAX):
                if droplet[x][y][z] == SOLID:
                    for dx, dy, dz in ((0, 0, 1),
                                       (0, 0, -1),
                                       (0, 1, 0),
                                       (0, -1, 0),
                                       (1, 0, 0),
                                       (-1, 0, 0)):
                        if droplet[x+dx][y+dy][z+dz] == kind:
                            result += 1
    return (result)


droplet = [[[SPACE for _ in range(MAX)]for _ in range(MAX)]for _ in range(MAX)]

f = open("in.raw", "r")
lines = f.read().splitlines()
for line in lines:
    x, y, z = (int(v) for v in line.split(","))
    droplet[x+1][y+1][z+1] = SOLID

print("Part 1: ", countadjacent(droplet, SPACE))

exteriorflood(droplet, 0, 0, 0)
print("Part 2: ", countadjacent(droplet, EXTERIOR))
