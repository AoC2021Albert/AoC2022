#!/usr/bin/env python
from copy import deepcopy


def solve(crates, lines, rev):
    crates = deepcopy(crates)
    for line in lines:
        (_, q, _, f, _, t) = line.split(" ")
        q, f, t = int(q), int(f) - 1, int(t) - 1
        crates[f], moving = crates[f][:-q], crates[f][-q:]
        if rev:
            moving.reverse()
        crates[t] += moving

    print("".join([crate[-1] for crate in crates]))


f = open("in.raw", "r")
line = f.readline()
ncrates = len(line) // 4
crates = [[] for _ in range(ncrates)]

while line[1] != "1":
    for j in range(ncrates):
        item = line[j*4+1]
        if item != " ":
            crates[j].append(item)
    line = f.readline()

[crate.reverse() for crate in crates]

emptyline = f.readline()

lines = f.read().splitlines()

solve(crates, lines, True)
solve(crates, lines, False)
