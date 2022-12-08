#!/usr/bin/env python
f = open("in.raw", "r")
lines = f.read().splitlines()

# PART 1
map = [[int(tree) for tree in row] for row in lines]
MAPSIZE = len(map)
visible = [[False] * MAPSIZE for _ in range(MAPSIZE)]

for pos in range(MAPSIZE):
    for yinc, xinc, y, x in (
        (-1,  0, MAPSIZE-1,       pos),
        ( 1,  0,         0,       pos),
        ( 0, -1,       pos, MAPSIZE-1),
        ( 0,  1,       pos,         0)):
        maxseen = -1
        while -1 < y < MAPSIZE and -1 < x < MAPSIZE:
            if map[y][x] > maxseen:
                visible[y][x] = True
                maxseen = map[y][x]
            y += yinc
            x += xinc

print(sum(sum(row) for row in visible))

# PART 2


def calculate_score(y, x):
    # up
    nx = x
    ny = y
    myh = map[y][x]
    result = 1
    for yinc, xinc in (
        (-1,  0),
        ( 1,  0),
        ( 0, -1),
        ( 0,  1)):
        nwy = y + yinc
        nwx = x + xinc
        while -1 < nwy < MAPSIZE and -1 < nwx < MAPSIZE and map[nwy][nwx] < myh:
            nwy, nwx = nwy+yinc, nwx+xinc
        if nwy == -1 or nwy == MAPSIZE or nwx == -1 or nwx == MAPSIZE:
            dist = abs(nwy-y + nwx - x) - 1
        else:
            dist = abs(nwy-y + nwx - x)
        result = result * dist
    return(result)


result = 0
for y in range(MAPSIZE):
    for x in range(MAPSIZE):
        score = calculate_score(y, x)
        if score > result:
            result = score

print(result)
