#!/usr/bin/env python
from collections import defaultdict
from copy import deepcopy
from functools import cache
from sys import stdin
from pprint import pprint

f = open("in.raw", "r")
lines = f.read().splitlines()


def solve(part2):
    H = 200
    W = 1000
    map = [[" "] * W for _ in range(H)]
    result = 0
    finaly = 0
    for line in lines:
        points = [[int(coor) for coor in point.split(",")]
                  for point in line.split(" -> ")]
        currpoint = points[0]
        for i in range(1, len(points)):
            nextpoint = points[i]
            minx = min(nextpoint[0], currpoint[0])
            maxx = max(nextpoint[0], currpoint[0])
            miny = min(nextpoint[1], currpoint[1])
            maxy = max(nextpoint[1], currpoint[1])
            finaly = max(finaly, maxy)
            for x in range(minx, maxx+1):
                for y in range(miny, maxy+1):
                    map[y][x] = "#"
            currpoint = nextpoint

    falling = False
    result = 0
    if part2:
        map[finaly+2] = ["#"] * W
    while not falling:
        sand = [0, 500]
        moving = True
        while moving:
            if sand[0] > finaly+2:
                falling = True
                moving = False  # meh
            else:
                newy = sand[0] + 1
                curx = sand[1]
                if map[newy][curx] == " ":
                    sand = [newy, curx]
                elif map[newy][curx-1] == " ":
                    sand = [newy, curx - 1]
                elif map[newy][curx+1] == " ":
                    sand = [newy, curx + 1]
                else:
                    moving = False
                    map[sand[0]][sand[1]] = "o"
                    result += 1
        if sand == [0, 500]:
            break

    return (result)


print(solve(False))

print(solve(True))
