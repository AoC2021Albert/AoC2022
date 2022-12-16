#!/usr/bin/env python
from collections import defaultdict
from copy import deepcopy
from functools import cache
from sys import stdin
from pprint import pprint
import re

f = open("in.raw", "r")
lines = f.read().splitlines()
tunnels=dict()
rates=dict()
for line in lines:
    m = re.match('Valve (..) has flow rate=([0-9]*); tunnels* leads* to valves* (.*)', line)
    valve, rate, dest = m.groups()
    tunnels[valve] = {k:1 for k in dest.split(', ')}
    if rate != "0" :
        rates[valve] = int(rate)
pprint(tunnels)
pprint(rates)
# calculate distances
# d is distnace table
def getalldist(d, walked):
    for next in tunnels[walked[-1]]:
        if d[walked[0]][next] > len(walked):
            d[walked[0]][next] = len(walked)
            walked.append(next)
            getalldist(d, walked )
            walked.pop()

d=defaultdict(lambda:defaultdict(lambda : 100))
d["AA"]["AA"] = 0
getalldist(d,["AA"])
for k in rates: #only interested in places with valves
    d[k][k] = 0
    getalldist(d, [k])
pprint(d)
# only interested on distances between valves
d = {oldk:{sk:sv for sk, sv in oldv.items() if sk in rates.keys() and sv !=0 } for oldk, oldv in d.items() if oldk in rates.keys() or oldk=="AA"}
pprint(d)

result = 0
def findsolutions(walked, remainingtime, flow, accumulated):
    global result, resultpath
    if flow*remainingtime + accumulated > result:
        result = flow*remainingtime + accumulated
    for next, dist in d[walked[-1]].items():
        if next not in walked and dist + 1 < remainingtime:
            #we can go and open
            walked.append(next)
            findsolutions(walked, remainingtime - dist - 1, flow + rates[next], accumulated + flow * (dist + 1))
            walked.pop()

findsolutions(["AA"], 30, 0,0)

print(result)

# PART 2
result = 0


print(result)
