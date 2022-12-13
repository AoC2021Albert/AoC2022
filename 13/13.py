#!/usr/bin/env python
from functools import cmp_to_key


def sign(x):
    if x > 0:
        return (1)
    elif x < 0:
        return (-1)
    else:
        return (0)


def order(l, r):
    lint = isinstance(l, int)
    rint = isinstance(r, int)
    if lint and rint:
        return (sign(l-r))
    if lint and not rint:
        return (order([l], r))
    if not lint and rint:
        return (order(l, [r]))
    # not lint and not rint:
    i = 0
    while i < len(l):  # l has elements
        if i >= len(r):  # r has no elements, is shorter
            return (1)
        s = order(l[i], r[i])
        if s != 0:
            return (s)
        # Things are equal so far, loop
        i += 1
    # We exhausted l
    if i < len(r):  # r has elements
        return (-1)
    else:  # r has no elements, l and r are the same
        return (0)


# for part1
exprpair = []
# for part2
allexpr = []

f = open("in.raw", "r")
while line := f.readline():
    # Nice! each line is a valid python expresion, we can eval()
    left = eval(line)
    right = eval(f.readline())
    # Get rid of separator line
    f.readline()
    exprpair.append((left, right))
    allexpr.append(left)
    allexpr.append(right)

# part1
result = 0
for i, pair in enumerate(exprpair, 1):
    left = pair[0]
    right = pair[1]
    if order(left, right) == -1:
        result += i

print("Part1:", result)

# part2
allexpr.append([[2]])
allexpr.append([[6]])
allexpr.sort(key=cmp_to_key(order))
print("Part2:", (allexpr.index([[2]])+1) * (1 + allexpr.index([[6]])))
