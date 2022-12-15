#!/usr/bin/env python
import re
# LOI = LINE OF INTEREST (part1)
# MAX = MAX RANGE (part2)

# f = open("test.raw", "r")
# LOI=10
# MAX=20
f = open("in.raw", "r")
LOI = 2000000
MAX = 4000000
lines = f.read().splitlines()

# PART 1
# Segments on the LOI, one per Sensor covering that LOI
segments = []
# Beacons present on the LOI.
# It is a set because the same beacon can appear multiple times in the LOI
beaconsloi = set()

for line in lines:
    m = re.match("Sensor at x=([0-9-]*), y=([0-9-]*): closest beacon is at x=([0-9-]*), y=([0-9-]*)",
                 line)
    # Sesor coordinates
    sx, sy = int(m.group(1)), int(m.group(2))
    # Beacon coordinates
    bx, by = int(m.group(3)), int(m.group(4))

    # Is the beacon in the LOI? add it!
    if by == LOI:
        beaconsloi.add(bx)

    # Sensor to Beacon Manhattan Distance, sbmd
    sbmd = abs(sx-bx) + abs(sy-by)
    # Sensor to LOI Manhattan Distance
    sloimd = abs(sy-LOI)
    if sloimd <= sbmd:
        # This sensor covers the LOI, dif is the "remaining" manhattan distance
        dif = sbmd - sloimd
        segments.append([sx-dif, sx+dif])


segments.sort()
covered = 0
curseg = segments[0]
for segment in segments[1:]:
    if segment[0] <= curseg[1]:
        if segment[1] > curseg[1]:
            # stretch segment
            curseg[1] = segment[1]
        else:
            # segment is inside curseg
            ...
    else:
        # segments do not overlap, count the curseg
        covered += curseg[1]-curseg[0] + 1
        curseg = segment

covered += curseg[1]-curseg[0] + 1

print("PART1", covered - len(beaconsloi))

# PART 2
def calcrow(sensors, depth):
    segments = []
    for (sx, sy, sbmd) in sensors:
        if abs(depth-sy) <= sbmd:
            # This sensor reaches the depth
            dif = (sbmd-abs(depth-sy))
            segstart = max(sx-dif, 0)
            segend = min(sx+dif, MAX)
            # Once intersected with 0..MAX, do we have a segment left?
            if segstart <= segend:
                segments.append([segstart, segend])
    segments.sort()
    covered = 0
    curseg = segments[0]
    if curseg[0] != 0:
        # A gap at the beginning of this depth
        print("Starting gap at:", depth, curseg[0])
        return(0)
    for segment in segments[1:]:
        if segment[0] <= curseg[1]:
            if segment[1] > curseg[1]:
                # stretch segment
                curseg[1] = segment[1]
            else:
                # segment is inside curseg
                ...
        else:
            # segments do not overlap (There's a potential gap)
            if segment[0]-curseg[1] > 1:
                print("Middle gap at:", depth, curseg, segment)
                return(curseg[1]+1)
            covered += curseg[1]-curseg[0] + 1
            curseg = segment

    covered += curseg[1]-curseg[0] + 1
    if covered != MAX+1:
        print("Finishing gap at: ", depth, curseg[1])
        return(4000000)

    return(None)


sensors = []
for line in lines:
    m = re.match("Sensor at x=([0-9-]*), y=([0-9-]*): closest beacon is at x=([0-9-]*), y=([0-9-]*)",
                 line)
    sx, sy = int(m.group(1)), int(m.group(2))
    bx, by = int(m.group(3)), int(m.group(4))

    sbmd = abs(sx-bx) + abs(sy-by)
    # We don't care about beacons anymore, just sensor and SensorBeaconManhattanDistance
    sensors.append((sx, sy, sbmd))

for depth in range(MAX+1):
    if gap := calcrow(sensors, depth):
        print("Part2: ", gap*4000000 + depth)