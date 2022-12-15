#!/usr/bin/env python
from collections import defaultdict
from copy import deepcopy
from functools import cache
from sys import stdin
from pprint import pprint
import re
f = open("in.raw", "r")
#LOI=10
#MAX=20
LOI=2000000
MAX=4000000
lines = f.read().splitlines()

# PART 1
segments=[]
beaconsloi = set()
for line in lines:
    m = re.match("Sensor at x=([0-9-]*), y=([0-9-]*): closest beacon is at x=([0-9-]*), y=([0-9-]*)",
                line)
    sx,sy = int(m.group(1)), int(m.group(2))
    bx,by = int(m.group(3)), int(m.group(4))
    if by==LOI:
        beaconsloi.add(bx)

    print(sx,sy,bx,by)
    sbmd = abs(sx-bx) + abs(sy-by)
    sloimd = abs(sy-LOI)
    if sloimd <= sbmd:
        dif=sbmd - sloimd
        print("sensor at ", sx, sy, "create segment : ",[sy-dif, sy+dif] )
        segments.append([sx-dif, sx+dif])
segments.sort()
print(segments)
result = 0
curseg=segments[0]
for segment in segments[1:]:
    if segment[0] <= curseg[1]:
        if segment[1] > curseg[1]:
            # stretch segment
            curseg[1] = segment[1]
        else:
            # segment is inside curseg
            ...
    else:
        #segments do not overlap
        result+=curseg[1]-curseg[0] + 1
        curseg=segment

result+=curseg[1]-curseg[0] + 1
        



print(result, beaconsloi, result- len(beaconsloi))
print("PART2")
# PART 2
segments=[]
s=[]
for line in lines:
    m = re.match("Sensor at x=([0-9-]*), y=([0-9-]*): closest beacon is at x=([0-9-]*), y=([0-9-]*)",
                line)
    sx,sy = int(m.group(1)), int(m.group(2))
    bx,by = int(m.group(3)), int(m.group(4))

    sbmd = abs(sx-bx) + abs(sy-by)
    s.append((sx,sy,sbmd))

def calcrow(sensors, depth):
    segments=[]
    for (sx, sy, sbmd) in sensors:
        if abs(depth-sy) <=  sbmd:
            rem = (sbmd-abs(depth-sy))
            segstart = max(sx-rem,0)
            segend = min(sx+rem,MAX)
            #print(depth, sx, sy, sbmd, segstart, segend)
            if segstart<=segend:
                segments.append([segstart,segend])
    #print(segments)
    segments.sort()
    result = 0
    curseg=segments[0]
    if curseg[0] != 0:
        print("curseg starts at ",curseg[0])
    for segment in segments[1:]:
        if segment[0] <= curseg[1]:
            if segment[1] > curseg[1]:
                # stretch segment
                curseg[1] = segment[1]
            else:
                # segment is inside curseg
                ...
        else:
            #segments do not overlap (There's a potential gap)
            print("GAP AT ", depth, curseg, segment, 4000000 * (curseg[1]-1) + depth)
            result+=curseg[1]-curseg[0] + 1
            curseg=segment

    result+=curseg[1]-curseg[0] + 1
    if result != MAX+1:
        print("depth incomplete at ", depth, result)

for i in range(MAX+1):
    calcrow(s, i)
