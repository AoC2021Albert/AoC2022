#!/usr/bin/env python
from collections import defaultdict
from copy import deepcopy
from functools import cache
from sys import stdin
from pprint import pprint
import sys
sys.setrecursionlimit(10000)


def cangoup(a, b):
    return (a - b <= 1)


def cangodown(a, b):
    return (b - a <= 1)


def calccost(y, x, currentcost, currentheight, cango):
    global W, H, cost
    if 0 <= y < H and \
       0 <= x < W and \
       cost[y][x] > currentcost and \
       cango(map[y][x], currentheight):
        cost[y][x] = currentcost
        for d in ((0, 1), (-1, 0), (0, -1), (1, 0)):
            calccost(y+d[0], x+d[1], currentcost+1, map[y][x], cango)


f = open("in.raw", "r")
lines = f.read().splitlines()


def height(c):
    if c.islower():
        return (ord(c))
    else:
        if c == 'S':
            return (ord('a')-1)
        if c == 'E':
            return (ord('z')+1)


map = [[height(c) for c in line] for line in lines]
H = len(map)
W = len(map[0])

cost = [[H*W for _ in row] for row in map]

start = [[y, row.index('S')] for y, row in enumerate(lines) if 'S' in row]
start = start[0]

end = [[y, row.index('E')] for y, row in enumerate(lines) if 'E' in row]
end = end[0]

calccost(start[0], start[1], 0, map[start[0]][start[1]], cangoup)

print("Part1: ", cost[end[0]][end[1]])

# PART 2
cost = [[H*W for _ in row] for row in map]
# We start in the end (up high) and calculate the cost of reaching any point
calccost(end[0], end[1], 0, map[end[0]][end[1]], cangodown)

# Now we look which 'a' point has the minimum value
mincost = W*H
for y, row in enumerate(map):
    for x, c in enumerate(row):
        if c == ord('a') and cost[y][x] < mincost:
            mincost = cost[y][x]

print("Part2: ", mincost)
