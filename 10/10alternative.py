#!/usr/bin/env python

f = open("in.raw", "r")
lines = f.read().splitlines()

def signal(ops):
    value = 1
    for op in ops:
        if op == "noop":
            yield(value)
        else:
            yield(value)
            yield(value)
            value+=int(op.split(" ")[1])


# PART 1
interesting=[20,60,100,140,180,220]

print(sum(value*pos for pos, value in enumerate(signal(lines),1) if pos in interesting))

# PART 2
HSIZE=40
VSIZE=6

screen=[[" "]*HSIZE for _ in range(VSIZE)]
for pos, sprite in enumerate(signal(lines)):
    if sprite - 1 <= pos % HSIZE <= sprite + 1:
        screen[(pos // HSIZE) % VSIZE][pos % HSIZE] = "#"

for row in screen:
    print("".join(row))

