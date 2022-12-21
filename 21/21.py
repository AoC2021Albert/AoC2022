#!/usr/bin/env python
from collections import defaultdict
from copy import deepcopy
from functools import cache
from sys import stdin
from pprint import pprint
import re
f = open("in.raw", "r")
lines = f.read().splitlines()

# PART 1
def solve(monkey):
    global monkeys
    if monkeys[monkey][0] in "0123456789":
        return(int(monkeys[monkey]))
    else:
        a,op,b = monkeys[monkey].split(' ')
        if op == "+":
            return(solve(a) + solve(b))
        elif op == "-":
            return(solve(a) - solve(b))
        elif op == "*":
            return(solve(a) * solve(b))
        elif op == "/":
            return(solve(a) / solve(b))
    raise Exception("HUMAN")

monkeys={}
for line in lines:
    m = re.match('(....): (.*)',line)
    name, value = m.groups()
    monkeys[name] = value    

print(solve('root'))

# PART 2
def solve2(monkey, goal):
    global monkeys
    if monkey=='humn':
        return(goal)
    if monkeys[monkey][0] in "0123456789":
        return(int(monkeys[monkey]))
    else:
        a,op,b = monkeys[monkey].split(' ')
        try:
            known = solve(a)
        except:
            aneedssolve = True
        try:
            known = solve(b)
        except:
            aneedssolve = False
        if op == "+":
            if aneedssolve:
                return(solve2(a, goal - known))
            else:
                return(solve2(b, goal - known))
        elif op == "-":
            if aneedssolve:
                return(solve2(a, goal + known))
            else:
                return(solve2(b, known - goal))
        elif op == "*":
            if aneedssolve:
                return(solve2(a, goal / known))
            else:
                return(solve2(b, goal / known))
        elif op == "/":
            if aneedssolve:
                return(solve2(a, goal * known))
            else:
                return(solve2(b, known / goal))
    print("FAIL")
    exit()

root = monkeys['root'].split(' ')

monkeys['root'] = root[0]+" - "+root[2]
monkeys['humn'] = "0 x 0" # will raise exception
print(solve2('root', 0))

