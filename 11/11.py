#!/usr/bin/env python
from collections import defaultdict
from copy import deepcopy
from functools import cache
from sys import stdin
from pprint import pprint
import re

f = open("test.raw", "r")

op = { "+" : lambda a, b : a + b ,
       "*" : lambda a, b : a * b}
# PART 1
ROUNDS=20
result = 0
monkeys = []
while line := f.readline():
    _ = re.search('Monkey ([0-9]*):',line).group(1)
    monkey = {}
    monkey["items"] = [int(item) for item in re.search('Starting items: ([0-9, ]*)$',f.readline()).group(1).split(",")]
    opval = re.search('Operation: new = old ([+*]) ([0-9old]*)',f.readline())
    monkey["op"] = opval.group(1)
    monkey["val"] = opval.group(2)
    monkey["div"] = int(re.search('Test: divisible by ([0-9]*)',f.readline()).group(1))
    monkey[True] = int(re.search('If true: throw to monkey ([0-9]*)',f.readline()).group(1))
    monkey[False] = int(re.search('If false: throw to monkey ([0-9]*)',f.readline()).group(1))
    print(monkey)
    monkeys.append(monkey)
    f.readline()

totalitems=[0] * len(monkeys)
for round in range(ROUNDS):
    for i, monkey in enumerate(monkeys):
        totalitems[i] += len(monkey["items"])
        for item in monkey["items"]:
            if monkey["val"] == "old":
                val = item
            else:
                val = int(monkey["val"])    
            item = op[monkey["op"]](item, val)
            item = item // 3
            destmonkey = monkey[item % monkey["div"] == 0]
            monkeys[destmonkey]["items"].append(item)
            print(f'pass to {destmonkey} with value {item}')
        monkey["items"] = []
    # end of round
    for i, monkey in enumerate(monkeys):
        print(f'Monkey {i}: {monkey["items"]}')
    print(totalitems)


totalitems.sort()
print(totalitems[-1]*totalitems[-2])

# PART 2
f = open("in.raw", "r")
ROUNDS=10000
result = 0
monkeys = []
mul = 1
while line := f.readline():
    _ = re.search('Monkey ([0-9]*):',line).group(1)
    monkey = {}
    monkey["items"] = [int(item) for item in re.search('Starting items: ([0-9, ]*)$',f.readline()).group(1).split(",")]
    opval = re.search('Operation: new = old ([+*]) ([0-9old]*)',f.readline())
    monkey["op"] = opval.group(1)
    monkey["val"] = opval.group(2)
    monkey["div"] = int(re.search('Test: divisible by ([0-9]*)',f.readline()).group(1))
    mul *= monkey["div"]
    monkey[True] = int(re.search('If true: throw to monkey ([0-9]*)',f.readline()).group(1))
    monkey[False] = int(re.search('If false: throw to monkey ([0-9]*)',f.readline()).group(1))
    print(monkey)
    monkeys.append(monkey)
    f.readline()

totalitems=[0] * len(monkeys)
for round in range(ROUNDS):
    for i, monkey in enumerate(monkeys):
        totalitems[i] += len(monkey["items"])
        for item in monkey["items"]:
            if monkey["val"] == "old":
                val = item
            else:
                val = int(monkey["val"])    
            item = op[monkey["op"]](item, val)
            item = item % mul
            destmonkey = monkey[item % monkey["div"] == 0]
            monkeys[destmonkey]["items"].append(item)
            print(f'pass to {destmonkey} with value {item}')
        monkey["items"] = []
    # end of round
    for i, monkey in enumerate(monkeys):
        print(f'Monkey {i}: {monkey["items"]}')
    print(totalitems)


totalitems.sort()
print(totalitems[-1]*totalitems[-2])

