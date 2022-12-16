#!/usr/bin/env python
from collections import defaultdict
from itertools import combinations
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

# only interested on distances between valves
d = {oldk:{sk:sv for sk, sv in oldv.items() if sk in rates.keys() and sv !=0 } for oldk, oldv in d.items() if oldk in rates.keys() or oldk=="AA"}


def findsolutions(result, walked, remainingtime, flow, accumulated, allowed):
    if flow*remainingtime + accumulated > result:
        result = flow*remainingtime + accumulated
    for next, dist in d[walked[-1]].items():
        if next not in walked and next in allowed and dist + 1 < remainingtime:
            #we can go and open
            walked.append(next)
            newr = findsolutions(result,walked, remainingtime - dist - 1, flow + rates[next], accumulated + flow * (dist + 1), allowed)
            if newr > result:
                result = newr
            walked.pop()
    return(result)

print("Part 1:", findsolutions(0,["AA"], 30, 0,0, list(rates.keys())))

# PART 2
result = 0
iteration = 0
#all possible groupings of 2 for the places with valves
allvalves=set(rates.keys())
tested = set()
for l in range(1,len(allvalves)):
    for mycombination in combinations(allvalves, l):
        iteration+=1
        if mycombination not in tested:
            tested.add(frozenset(mycombination))
            elecombination = allvalves - set(mycombination)
            tested.add(frozenset(elecombination))
            newresult = findsolutions(0,["AA"], 26, 0,0, mycombination) + \
                        findsolutions(0,["AA"], 26, 0,0, elecombination)
            result = max(result, newresult)

print("Part 2", result)
