#!/usr/bin/env python
from collections import defaultdict
from copy import deepcopy
from functools import cache
from sys import stdin
from pprint import pprint
from math import copysign

f = open("in.raw", "r")
lines = f.read().splitlines()

# PART 1
def tail_follow_head(head, tail):
    if abs(head[0] - tail[0]) > 1:
        newy = head[0] + (-1 if head[0] > tail[0] else 1)
        newx = head[1]
        return((newy,newx))
    elif abs(head[1] - tail[1]) > 1:
        newy = head[0]
        newx = head[1] + (-1 if head[1] > tail[1] else 1)
        return((newy,newx))
    else:
        return(tail)

move={"U" : (-1,  0),
      "D" : ( 1,  0),
      "L" : ( 0, -1),
      "R" : ( 0,  1)}

visited=set()
tail=(0,0)
head=(0,0)
for line in lines:
    dir, steps = line.split(" ")
    steps = int(steps)
    for _ in range(steps):
        head=(head[0]+move[dir][0],
              head[1]+move[dir][1])
        tail = tail_follow_head(head, tail)
        visited.add(tail)
print(len(visited))

# PART 2
def sign(x):
    if x > 0:
        return(1)
    elif x < 0:
        return(-1)
    else:
        return(0)
def tail_follow_fast_head(head, tail):
    newpositions=set([tail])
    ydif = head[0]-tail[0]
    xdif = head[1]-tail[1]
    while max(abs(ydif), abs(xdif)) > 1:
        tail = (tail[0] + sign(ydif),
                tail[1] + sign(xdif))
        ydif = head[0]-tail[0]
        xdif = head[1]-tail[1]
        newpositions.add(tail)
    return(newpositions, tail)

visited=set()
rope=[(0,0)] * 10
for line in lines:
    dir, steps = line.split(" ")
    steps = int(steps)
    for _ in range(steps):
        rope[0]=(rope[0][0]+move[dir][0],
                rope[0][1]+move[dir][1])
        for knot in range(1, 10):
            newpos, rope[knot] = tail_follow_fast_head(rope[knot-1], rope[knot])
            
        visited.update(newpos)
#pprint(visited)
print(len(visited))

'''
...H
..2.
.1..
0...

...H
....
..2.
.1..
0...

...H
...2
....
.1..
0...

...H
...2
....
.1..
0...

...H
...2
....
.1..
0...


'''