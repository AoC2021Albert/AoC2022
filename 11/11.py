#!/usr/bin/env python
from copy import deepcopy
import re

op = {"+": lambda a, b: a + b,
      "*": lambda a, b: a * b}


def solver11(ROUNDS, worryreductor, monkeys):
    totalitems = [0] * len(monkeys)
    for round in range(ROUNDS):
        for i, monkey in enumerate(monkeys):
            totalitems[i] += len(monkey["items"])
            for item in monkey["items"]:
                if monkey["val"] == "old":
                    val = item
                else:
                    val = int(monkey["val"])
                item = op[monkey["op"]](item, val)
                item = worryreductor(item)
                destmonkey = monkey[item % monkey["div"] == 0]
                monkeys[destmonkey]["items"].append(item)
            monkey["items"] = []

    totalitems.sort()
    return (totalitems[-1]*totalitems[-2])


f = open("in.raw", "r")

monkeys = []
mul = 1
while line := f.readline():
    _ = re.search('Monkey ([0-9]*):', line).group(1)
    monkey = {}
    monkey["items"] = [int(item) for item in re.search(
        'Starting items: ([0-9, ]*)$', f.readline()).group(1).split(",")]
    opval = re.search('Operation: new = old ([+*]) ([0-9old]*)', f.readline())
    monkey["op"] = opval.group(1)
    monkey["val"] = opval.group(2)
    monkey["div"] = int(
        re.search('Test: divisible by ([0-9]*)', f.readline()).group(1))
    mul *= monkey["div"]
    monkey[True] = int(
        re.search('If true: throw to monkey ([0-9]*)', f.readline()).group(1))
    monkey[False] = int(
        re.search('If false: throw to monkey ([0-9]*)', f.readline()).group(1))
    monkeys.append(monkey)
    f.readline()

# part 1
print(solver11(20, lambda x: x // 3, deepcopy(monkeys)))

# part 2
print(solver11(10000, lambda x: x % mul, deepcopy(monkeys)))
