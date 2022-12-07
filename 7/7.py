#!/usr/bin/env python
from collections import defaultdict, Counter
from copy import deepcopy
from functools import lru_cache
from sys import stdin
from pprint import pprint


f = open("in.raw", "r")
lines = f.read().splitlines()

# PART 1


def sumsmallerthan100000(cwd):
    ownsize = 0
    smallerthan100000 = 0
    for sub in cwd:
        if sub == ".size":
            ownsize += cwd[sub]
        else:
            subsize, subsmallerthan100000 = sumsmallerthan100000(cwd[sub])
            ownsize += subsize
            smallerthan100000 += subsmallerthan100000
    if ownsize <= 100000:
        smallerthan100000 += ownsize
    # for part2
    cwd[".totalsize"] = ownsize

    return(ownsize, smallerthan100000)


rootdir = dict()
# ugly but efficient
rootdir[".size"] = 0
cwd = rootdir
dirstack = []

i = 1

while i < len(lines):
    cmd = lines[i].split(" ")
    i += 1
    if cmd[1] == "cd":
        if cmd[2] == '..':
            cwd = dirstack.pop()
        else:
            dirstack.append(cwd)
            cwd = cwd[cmd[2]]
    else:
        assert(cmd[1] == "ls")
        while i < len(lines) and lines[i][0] != "$":
            size, name = lines[i].split(" ")
            if size == "dir":
                cwd[name] = dict()
                cwd[name][".size"] = 0
            else:
                cwd[".size"] += int(size)
            i += 1

result = sumsmallerthan100000(rootdir)
pprint(rootdir)
print(result)

# PART 2


def findmindir(cwd, freesize):
    result = 70000000
    for sub in cwd:
        if sub != ".size" and sub != ".totalsize":
            bestsub = findmindir(cwd[sub], freesize)
            if bestsub < result and bestsub >= freesize:
                result = bestsub
    if cwd[".totalsize"] < result and cwd[".totalsize"] >= freesize:
        result = cwd[".totalsize"]
    return(result)


result = 0
freesize = 30000000 - (70000000 - rootdir[".totalsize"])
result = findmindir(rootdir, freesize)
print(result)
