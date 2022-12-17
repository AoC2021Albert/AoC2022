#!/usr/bin/env python
from collections import defaultdict
from copy import deepcopy
from functools import cache
from sys import stdin
from pprint import pprint

f = open("in.raw", "r")
jetpattern = f.read().splitlines()[0]

# Upside down as I want [0] to be the bottom
rockshapes = [
    [0b0011110],

    [0b0001000,
     0b0011100,
     0b0001000],

    [0b0011100,
     0b0000100,
     0b0000100],

    [0b0010000,
     0b0010000,
     0b0010000,
     0b0010000],

    [0b0011000,
     0b0011000]
]

# ROUNDS=2022   # PART 1
ROUNDS = 1000000000000  # PART 2
MAXH = 40000*5  # I already know my cycle and offset. This is at least an order or magnitude bigger than needed
chimney = [0] * MAXH


def rockfits(chimney, rock, rockbottom):
    fits = True
    for i, segment in enumerate(rock):
        if chimney[rockbottom + i] & segment != 0:
            fits = False
    return (fits)


def rockcangodown(chimney, rock, rockbottom):
    return (rockfits(chimney, rock, rockbottom-1))


def blowrockright(chimney, rock, rockbottom):
    if all((segment % 2 == 0 for segment in rock)):
        # not hitting a wall, let's check if we hit something else
        newrock = [segment // 2 for segment in rock]
        if rockfits(chimney, newrock, rockbottom):
            return (newrock)
    return (rock)


def blowrockleft(chimney, rock, rockbottom):
    if all((segment < 2**6 for segment in rock)):
        # not hitting a wall, let's check if we hit something else
        newrock = [segment * 2 for segment in rock]
        if rockfits(chimney, newrock, rockbottom):
            return (newrock)
    return (rock)


def fixrock(chimney, rock, rockbottom):
    for i in range(len(rock)):
        chimney[rockbottom + i] |= rock[i]


def printchimney(chimneypart):
    print()
    for row in chimneypart:
        print('{:07b}'.format(row))
    print()


# The "chimney" starts with solid ground on
# chimney[0] and it goes up from there
chimney[0] = 0b1111111
towerheight = 0
jetround = 0
round = 0
# For part 2 (also works on part 1)
saw = []
heights = []
cyclefound = False
while not cyclefound and round < ROUNDS:
    initrock = round % len(rockshapes)
    # Create a new copy of the rockshape
    rock = rockshapes[round % len(rockshapes)][:]
    # We start one higher than specified as we loop like:
    # while can move down
    #   movedown
    #   jets
    rockbottom = towerheight + 5
    while rockcangodown(chimney, rock, rockbottom):
        rockbottom -= 1
        if jetpattern[jetround] == ">":
            rock = blowrockright(chimney, rock, rockbottom)
        else:
            rock = blowrockleft(chimney, rock, rockbottom)
        jetround += 1
        jetround %= len(jetpattern)
    # We have "landed" a rock. Lets memorize what we have just seen
    # So we can later check for a cycle
    # We "encode" as a string the relevant "top" part of the chimney
    # The one that goes from the top to where we landed
    toprockformation = ".".join((str(row)
                                for row in chimney[rockbottom:towerheight+1]))
    # We add to the encoding what jetround we are at and what rock
    see = f'{jetround},{initrock},{toprockformation}'
    if see in saw:
        # BINGO! We found that tha same "toprockformation" with the same
        # jetround and initrock are appearing again. We Have a Cycle!!
        cyclefound = True
        sawinround = saw.index(see)
        reseeninround = round
        print("MATCH FOUND", round, sawinround, see, towerheight)
        cyclesize = round - sawinround
        offset = sawinround
    saw.append(see)
    fixrock(chimney, rock, rockbottom)
    towerheight = max(towerheight, rockbottom + len(rock) - 1)
    heights.append(towerheight)
    round += 1

# printchimney(chimney)
if cyclefound:
    cycleheight = heights[reseeninround]-heights[sawinround]
    print(f'cycleheight: {cycleheight}, cyclesize: {cyclesize}')
    postcycleoffset = (ROUNDS - offset) % cyclesize
    print(f'postcycleoffset: {postcycleoffset}')
    print(heights[offset+postcycleoffset-1] +
          cycleheight * ((ROUNDS-offset) // cyclesize))
else:
    print(towerheight)
