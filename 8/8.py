#!/usr/bin/env python
f = open("in.raw", "r")
lines = f.read().splitlines()

# PART 1
map = [[int(tree) for tree in row] for row in lines]
YLEN = len(map)
XLEN = len(map[0])
visible = [[False] * XLEN for _ in range(YLEN)]
for y in range(YLEN):
    maxleft = -1
    maxright = -1
    for x in range(XLEN):
        if map[y][x] > maxleft:
            visible[y][x] = True
            maxleft = map[y][x]
        if map[y][-x-1] > maxright:
            visible[y][-x-1] = True
            maxright = map[y][-x-1]

for x in range(YLEN):
    maxup = -1
    maxdown = -1
    for y in range(XLEN):
        if map[y][x] > maxup:
            visible[y][x] = True
            maxup = map[y][x]
        if map[-y-1][x] > maxdown:
            visible[-y-1][x] = True
            maxdown = map[-y-1][x]

print(sum(sum(row) for row in visible))

# PART 2


def calculate_score(y, x):
    # up
    nx = x
    ny = y
    myh = map[y][x]

    up = y-1
    while up >= 0 and map[up][x] < myh:
        up -= 1
    if up == -1:
        upd = y-up - 1
    else:
        upd = y - up

    down = y+1
    while down < YLEN and map[down][x] < myh:
        down += 1
    if down == YLEN:
        downd = down - y - 1
    else:
        downd = down - y

    left = x-1
    while left >= 0 and map[y][left] < myh:
        left -= 1
    if left == -1:
        leftd = x-left - 1
    else:
        leftd = x - left

    right = x+1
    while right < XLEN and map[y][right] < myh:
        right += 1
    if right == XLEN:
        rightd = right - x - 1
    else:
        rightd = right - x

    result = upd*downd*leftd*rightd
    return(result)


result = 0
for y in range(YLEN):
    for x in range(XLEN):
        score = calculate_score(y, x)
        if score > result:
            result = score

print(result)
