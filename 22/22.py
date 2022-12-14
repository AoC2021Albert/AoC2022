#!/usr/bin/env python

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3
# Mode is
WRAP = 0  # for part 1
CUBE = 1  # for part 2

DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))


def leftmost(map, y):
    x = 0
    while map[y][x] == " ":
        x += 1
    return (x)


def rightmost(map, y):
    return (len(map[y])-1)


def topmost(map, x):
    y = 0
    while map[y][x] == " ":
        y += 1
    return (y)


def bottommost(map, x):
    y = len(map)-1
    while len(map[y]) <= x:
        y -= 1
    while map[y][x] == " ":
        y -= 1
    return (y)


def step(map, p, dir, mode):
    y = p[0]
    x = p[1]
    newdir = dir
    LIMITDETECT = (rightmost(map, y) == x,
                   bottommost(map, x) == y,
                   leftmost(map, y) == x,
                   topmost(map, x) == y)
    if LIMITDETECT[dir]:
        if mode == WRAP:
            next = ((y, leftmost(map, y)),
                    (topmost(map, x), x),
                    (y, rightmost(map, y)),
                    (bottommost(map, x), x))[dir]
        elif mode == CUBE:
            REMAPRIGHT = (((0),                 (0),                (149-y, 99, LEFT)),
                          ((0),                 (49, 100+(y-50), UP), (0)),
                          ((0),                 ((149-y), 149, LEFT), (0)),
                          ((149, 50+(y-150), UP), (0),                (0)))

            REMAPDOWN = (((0),            (0),                  (50+(x-100), 99, LEFT)),
                         ((0),            (0),                  (0)),
                         ((0),            (150+(x-50), 49, LEFT), (0)),
                         ((0, x+100, DOWN), (0),                  (0)))

            REMAPLEFT = (((0), (100+(49-y), 0, RIGHT), (0)),
                         ((0), (100, y-50, DOWN), (0)),
                         ((149-y, 50, RIGHT), (0), (0)),
                         ((0, y-150+50, DOWN), (0), (0)))

            REMAPUP = (((0), (x-50+150, 0, RIGHT), (199, x-100, UP)),
                       ((0), (0), (0)),
                       ((x+50, 50, RIGHT), (0), (0)),
                       ((0), (0), (0)))

            ysect = y // 50
            xsect = x // 50
            newy, newx, newdir = (REMAPRIGHT,
                                  REMAPDOWN,
                                  REMAPLEFT,
                                  REMAPUP)[dir][ysect][xsect]
            next = (newy, newx)
        else:
            print("What mode?")
            exit()
    else:
        next = (y+DIRS[dir][0], x+DIRS[dir][1])
    if map[next[0]][next[1]] == ".":
        return (next, newdir)
    elif map[next[0]][next[1]] == "#":
        return ((y, x), dir)
    else:
        print("Out of map")
        exit()


def solve(mode):
    pos = (0, leftmost(map, 0))
    i = 0
    steps = 0
    while path[i] in "0123456789":
        steps = steps * 10 + int(path[i])
        i += 1
    dir = 0
    for _ in range(steps):
        pos, dir = step(map, pos, dir, mode)

    while i < len(path):
        cd = path[i]
        if cd == "R":
            dir += 1
        elif cd == "L":
            dir -= 1
        else:
            print("What direction?")
            exit()
        dir %= 4
        i += 1
        steps = 0
        while i < len(path) and path[i] in "0123456789":
            steps = steps * 10 + int(path[i])
            i += 1
        for _ in range(steps):
            pos, dir = step(map, pos, dir, mode)
    return ((pos[0]+1)*1000 + (pos[1]+1) * 4 + dir)


f = open("in.raw", "r")
lines = f.read().splitlines()
map = lines[:-2]
path = lines[-1]

print("Part 1: ", solve(WRAP))
print("Part 2: ", solve(CUBE))
