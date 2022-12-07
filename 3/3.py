#!/usr/bin/env python

v = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

f = open("in.raw", "r")
lines = f.read().splitlines()


def lettervalue(letter):
    offset = 26 if letter.isupper() else 0
    m = letter.lower()
    return(ord(m) - ord('a') + 1) + offset


result = 0
for line in lines:
    l = len(line)//2
    l1 = line[:l]
    l2 = line[l:]
    match = ""
    for c in l1:
        if c in l2:
            match = c
    assert(len(match) == 1)
    val = lettervalue(match[0])
    # print(match,val)
    result += val
print(result)

result = 0
l = 0
while l < len(lines):
    letters = []
    for i in range(3):
        foundletters = set()
        for c in lines[l]:
            foundletters.add(c)
        l += 1
        letters.append(foundletters)
    c = letters[0].intersection(letters[1]).intersection(letters[2])
    assert(len(c) == 1)
    result += lettervalue(c.pop())
print(result)
