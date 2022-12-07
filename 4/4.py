#!/usr/bin/env python
from collections import defaultdict
from copy import deepcopy
from functools import lru_cache
from sys import stdin
from pprint import pprint

f = open("in.raw", "r")
lines = f.read().splitlines()

# PART 1
result = 0
for line in lines:
    p = line.split(",")
    q = [[int(v) for v in s.split('-')] for s in p]
    if (q[0][0] <= q[1][0] and
        q[0][1] >= q[1][1]) or (
        q[0][0] >= q[1][0] and
        q[0][1] <= q[1][1]
    ):
        result += 1
        pprint(f"match:{q}")
print(result)

# PART 2
result = 0
for line in lines:
    p = line.split(",")
    q = [[int(v) for v in s.split('-')] for s in p]
    start = max(q[0][0], q[1][0])
    end = min(q[0][1], q[1][1])
    if end >= start:
        r = 1
 #        r=end-start+1
    else:
        r = 0
    pprint(f"{q}:{r}")
    result += r
print(result)
