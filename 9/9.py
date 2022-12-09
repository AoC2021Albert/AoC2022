#!/usr/bin/env python

f = open("in.raw", "r")
lines = f.read().splitlines()

move = {"U": (-1,  0),
        "D": ( 1,  0),
        "L": ( 0, -1),
        "R": ( 0,  1)}


def sign(x):
    if x > 0:
        return (1)
    elif x < 0:
        return (-1)
    else:
        return (0)


def tail_follow_head(head, tail):
    ydif = head[0]-tail[0]
    xdif = head[1]-tail[1]
    if max(abs(ydif), abs(xdif)) > 1:
        tail = (tail[0] + sign(ydif),
                tail[1] + sign(xdif))
    return (tail)


# PART 1
visited = set()
tail = (0, 0)
head = (0, 0)
for line in lines:
    dir, steps = line.split(" ")
    steps = int(steps)
    for _ in range(steps):
        head = (head[0]+move[dir][0],
                head[1]+move[dir][1])
        tail = tail_follow_head(head, tail)
        visited.add(tail)
print(len(visited))

# PART 2
visited = set()
rope = [(0, 0)] * 10
for line in lines:
    dir, steps = line.split(" ")
    steps = int(steps)
    for _ in range(steps):
        rope[0] = (rope[0][0]+move[dir][0],
                   rope[0][1]+move[dir][1])
        for knot in range(1, 10):
            rope[knot] = tail_follow_head(rope[knot-1], rope[knot])
        visited.add(rope[-1])
print(len(visited))
