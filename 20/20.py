#!/usr/bin/env python
from collections import defaultdict
from copy import deepcopy
from functools import cache
from sys import stdin
from pprint import pprint


class Dll:
    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None

    def __repr__(self):
        return (f'{self.prev.value}<{self.value}>{self.next.value}')

    def move(self, n, multiplier, modulo, forward):
        oldnext = self.next
        oldprev = self.prev
        if forward:
            newprev = self
        else:
            newprev = self.prev
        for _ in range(n * multiplier % modulo):
            if forward:
                newprev = newprev.next
            else:
                newprev = newprev.prev
        newnext = newprev.next

        oldprev.next, oldnext.prev = oldnext, oldprev

        newprev.next = self
        newnext.prev = self
        self.prev = newprev
        self.next = newnext


f = open("in.raw", "r")
lines = f.read().splitlines()


def solve20(lines, multiplier, rounds):
    # Initialize and load
    result = 0
    l = []
    v0 = None
    LENL = len(lines) - 1
    for line in lines:
        value = int(line)
        v = Dll(value)
        l.append(v)
        if value == 0:
            v0 = v

    for i in range(len(l)):
        l[i].prev = l[(i-1) % len(l)]
        l[i].next = l[(i+1) % len(l)]

    # Do rounds
    for _ in range(rounds):
        for v in l:
            if v.value > 0:
                v.move(v.value, multiplier, LENL, True)
            if v.value < 0:
                v.move(-v.value, multiplier, LENL, False)

    # Get solution
    # Convert dll to list
    newl = [0]
    curv = v0.next
    while curv.value != 0:
        newl.append(curv.value)
        curv = curv.next

    # Calculate result
    for k in 1000, 2000, 3000:
        num = newl[k % len(newl)]
        result += num * multiplier
    return(result)


print("Part1: ", solve20(lines, 1, 1))
print("Part2: ", solve20(lines, 811589153, 10))
