#!/usr/bin/env python
from collections import defaultdict
from copy import deepcopy
from functools import cache
from sys import stdin
from pprint import pprint

f = open("in.raw", "r")
lines = f.read().splitlines()
VAL={
    "2":2,
    "1":1,
    "0":0,
    "-":-1,
    "=":-2
}
def b5tonum(number):
    value = 0
    for digit in number:
        value *= 5
        value += VAL[digit]
    return(value)

def numtob5(num):
    # I check by boundaries (there has to be a math way)
    # First see how many digits it needs to be
    power=1
    while b5tonum("2"*power) <= num:
        power+=1
    # Start with leftmost digit
    s=""
    while power > 0:
        power-=1
        inbounds = False
        VALS= "=-012"
        i = 0
        # Try each possible digit and see if the maximum
        # And minimus with this digit is within bounds
        while not( b5tonum(s+VALS[i]+"2"*power) >= num and
                   b5tonum(s+VALS[i]+"="*power) <= num):
            i+=1
        s+=VALS[i]
    return(s)

# PART 1
result = 0
numbers=[]
for b5number in lines:
    result+=b5tonum(b5number)

print(numtob5(result))
