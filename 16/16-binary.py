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
# It works with a dictionary of dictionaries.
# The top level key is the origin
# The 2nd level key is the destination
def getalldist(d, walked):
    for next in tunnels[walked[-1]]:
        if d[walked[0]][next] > len(walked):
            d[walked[0]][next] = len(walked)
            walked.append(next)
            getalldist(d, walked )
            walked.pop()

# I don't want to be testing if entries exist
# If nobody had recorded a distance between two points
# I assign it a distance of 100 (which is bigger than the amount of valves in the problem)
d=defaultdict(lambda:defaultdict(lambda : 100))
# Start with the
d["AA"]["AA"] = 0
getalldist(d,["AA"])
for k in rates: #only interested in places with valves
    d[k][k] = 0
    getalldist(d, [k])

usefullvalves=list(rates.keys())

# only interested on distances between valves that are usefull (don't have a 0 rate) and that are not non-moves (distance = 0)
d = {oldk:{sk:sv for sk, sv in oldv.items() if sk in usefullvalves and sv != 0} for oldk, oldv in d.items() if oldk in usefullvalves or oldk=="AA"}
# The previous line is equivalent to
# neworiginsdict = dict()
# for origin, destinationsdict in d.items():
#     if origin in usefullvalves or origin == "AA":
#         newdestinationsdict = dict()
#         for destination, distance in destinationsdict.items():
#             if destination in usefullvalves and distance !=0 :
#                 newdestinationsdict[destination] = distance
#         neworiginsdict[origin] = newdestinationsdict
# d = neworiginsdict



def findsolutions(result, walked, remainingtime, flow, accumulated, allowed):
    result = max( result, flow*remainingtime + accumulated )
    for next, dist in d[walked[-1]].items():
        if next not in walked and next in allowed and dist + 1 < remainingtime:
            #we can go and open and still get something new
            walked.append(next)
            result = max( result, findsolutions(result,walked, remainingtime - dist - 1, flow + rates[next], accumulated + flow * (dist + 1), allowed))
            walked.pop()
    return(result)

print("Part 1:", findsolutions(0,["AA"], 30, 0, 0, usefullvalves))

# PART 2
result = 0
iteration = 0
testedcomb = 0
totalcomb = 0
#all possible groupings of 2 for the places with valves
# Prepare a numeric version of the distances table
# We will use it later so that nodes will be numeric from 0 to n
# Then we can do combinations where for example combination 24 would be
# 0b011000
#    xx    visited by elephant
#   x  xxx visited by me
# This makes calculating all the combinations of valves visited by the
# elephant and me trivial to generate and without repetitions
# BTW, I don't need to go from 000000 to 111111, I only need
# from 000000 to 011111. The reason is that
# - 010011 will have the same solution than
# - 101100 as the trained elephant is as efficient as myself (good boy!)
lenvalves = len(rates)
interestingvalves = usefullvalves + ["AA"] # "AA" must be the last
d = {interestingvalves.index(origin):{usefullvalves.index(destination):distance for destination, distance in destinations.items() }
     for origin, destinations in d.items()}
rates={interestingvalves.index(valve):rate for valve,rate in rates.items()}


for combination in range(2**(lenvalves-1)):
    myvalves = [v for v in range(lenvalves) if 2**v & combination != 0] # I get the 1's
    elevalves= [v for v in range(lenvalves) if 2**v & combination == 0] # Elefant gets the 0's
    result = max(result, findsolutions(0, [lenvalves] , 26, 0,0, myvalves) +
                         findsolutions(0, [lenvalves] , 26, 0,0, elevalves))

print("Part 2", result, totalcomb, testedcomb)
