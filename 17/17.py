#!/usr/bin/env python
from collections import defaultdict
from copy import deepcopy
from functools import cache
from sys import stdin
from pprint import pprint

f = open("in.raw", "r")
jetpattern = f.read().splitlines()[0]

#Upside down as i want [0] to be the bottom
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

# PART 1
ROUNDS=2022
MAXH = 2022*5 # plenty of room for 2022 pieces
chimney = [0] * MAXH

def rockfits(chimney, rock, rockbottom):
    fits = True
    for i, segment in enumerate(rock):
        if chimney[rockbottom + i] & segment != 0:
            fits = False
    return(fits)

def rockcangodown(chimney, rock, rockbottom):
    return(rockfits(chimney, rock, rockbottom-1))

def blowrockright(chimney, rock, rockbottom):
    if all((segment % 2 == 0 for segment in rock)):
        #not hitting a wall, let's check if we hit something else
        newrock = [segment // 2 for segment in rock]
        if rockfits(chimney, newrock, rockbottom):
            return(newrock)
    return(rock)

def blowrockleft(chimney, rock, rockbottom):
    if all((segment < 2**6 for segment in rock)):
        #not hitting a wall, let's check if we hit something else
        newrock = [segment * 2 for segment in rock]
        if rockfits(chimney, newrock, rockbottom):
            return(newrock)
    return(rock)

def fixrock(chimney, rock, rockbottom):
    for i in range(len(rock)):
        chimney[rockbottom + i] |= rock[i]


# The "chimney" starts with solid ground on 
# chimney[0] and it goes up from there
chimney[0] = 0b1111111
towerheight = 0
jet=0
for round in range(ROUNDS):
    # Create a new copy of the rockshape
    rock = rockshapes[round % len(rockshapes)][:]
    # We start one higher than specified as we loop like:
    # while can move down
    #   movedown
    #   jets
    rockbottom = towerheight + 5
    while rockcangodown (chimney, rock, rockbottom):
        rockbottom-=1
        if jetpattern[jet] == ">":
            rock = blowrockright(chimney, rock, rockbottom)
        else:
            rock = blowrockleft(chimney, rock, rockbottom)
        jet += 1
        jet %= len(jetpattern)
    fixrock (chimney, rock, rockbottom)
    towerheight = max(towerheight, rockbottom + len(rock) - 1)
    
#    print()
#    for row in chimney[towerheight:0:-1]:
#        print('{:07b}'.format(row))
#    print()
print(towerheight)

# PART 2
result = 0
print(result)
