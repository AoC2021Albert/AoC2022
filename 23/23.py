#!/usr/bin/env python

Y=0
X=1

def move(elfs, dirs):
    newocu = set()      # New occupied, where elfs propose to go
    collisions = set()  # Places where more than 1 elf propose to go
    newelfs = set()     # Where elfs will be after they move (return value)
    AROUND = (
        (-1,-1),(-1,0), (-1,1),
        ( 0,-1),        ( 0,1),
        ( 1,-1),( 1,0), ( 1,1),
    )
    # Check where elfs propose to go with the goal of detecting collisions
    for elf in elfs:
        d = 0
        # Iterate the 4 directions and check if movement possible
        while d<4 and any(((elf[Y]+dirs[d][i][Y],elf[X]+dirs[d][i][X]) in elfs for i in range(3))):
            # Can't move in that direction, try next
            d+=1
        # if elf does not want to move (AROUND is empty) OR elf can't move (d>=4)
        # Note: d==0 is just an optimization, do not check AROUND if d>0, as AROUND will be occupied
        if (d==0 and all(((elf[Y]+AROUND[i][Y],elf[X]+AROUND[i][X]) not in elfs for i in range(8))))\
            or d>=4:
            # elf does not move
            newocu.add(elf)
        else:
            # elf proposes to move
            proposed = (elf[Y]+dirs[d][1][Y],elf[X]+dirs[d][1][X])
            # We could check if proposed is in newocu to detect collisions
            # But checking if the len of newocu changes is more efficient
            oldlen = len(newocu)
            newocu.add(proposed)
            if oldlen == len(newocu):
                collisions.add(proposed)
    # Now we move the elfs
    for elf in elfs:
        d = 0
        # Same as before
        while d<4 and any(((elf[Y]+dirs[d][i][Y],elf[X]+dirs[d][i][X]) in elfs for i in range(3))):
            d+=1
        # Same as before, but we also check for collisions
        if (d==0 and all(((elf[Y]+AROUND[i][Y],elf[X]+AROUND[i][X]) not in elfs for i in range(8))))\
            or d>=4 \
            or (elf[Y]+dirs[d][1][Y],elf[X]+dirs[d][1][X]) in collisions:
            newelfs.add(elf)
        else:
            newelfs.add((elf[Y]+dirs[d][1][Y],elf[X]+dirs[d][1][X]))
    return(newelfs)
    
f = open("in.raw", "r")
lines = f.read().splitlines()

elfs=set()
for y, row in enumerate(lines):
    for x, cell in enumerate(row):
        if cell == "#":
            elfs.add((y,x))
dirs=[
    ((-1,-1),(-1, 0),(-1, 1)), # North
    (( 1,-1),( 1, 0),( 1, 1)), # South
    ((-1,-1),( 0,-1),( 1,-1)), # West
    ((-1, 1),( 0, 1),( 1, 1))  # East
]

def emptyspaces(elfs):
    maxx=-999999999999
    maxy=-999999999999
    minx=999999999999
    miny=999999999999

    for elf in elfs:
        minx=min(minx,elf[X])
        maxx=max(maxx,elf[X])
        miny=min(miny,elf[Y])
        maxy=max(maxy,elf[Y])
    return((maxx-minx+1)*(maxy-miny+1) - len(elfs))

iteration=0
while True:
    if iteration==10:
        print("Part 1: ", emptyspaces(elfs))
    iteration += 1
    newelfs = move(elfs, dirs)
    if len(newelfs.difference(elfs))==0:
        print("Part 2: ", iteration)
        exit()
    dirs=dirs[1:]+dirs[:1]
    elfs=newelfs