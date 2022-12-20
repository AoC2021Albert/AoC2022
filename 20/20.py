#!/usr/bin/env python
from collections import defaultdict
from copy import deepcopy
from functools import cache
from sys import stdin
from pprint import pprint

class Dll:
    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None

    def __repr__(self):
        return(f'{self.prev.value}<{self.value}>{self.next.value}')

    def moveforward(self, n):
        for _ in range(n):
            mynext = self.next
            myprev = self.prev
            mynextnext = self.next.next
            myprev.next = mynext
            self.prev = mynext
            mynext.prev = myprev
            self.next = mynextnext
            mynextnext.prev = self
            mynext.next = self
            
    def movebackward(self, n):
        for _ in range(n):
            mynext = self.next
            myprev = self.prev
            myprevprev = self.prev.prev
            mynext.prev = myprev
            self.next = myprev
            myprev.next = mynext
            self.prev = myprevprev
            myprevprev.next = self
            myprev.prev = self
            


f = open("in.raw", "r")
lines = f.read().splitlines()

# PART 1
result = 0
l = []
v0 = None
for line in lines:
    value = int(line)
    v = Dll(value)
    l.append(v)
    if value==0: 
        v0 = v

for i in range(len(l)):
    l[i].prev=l[(i-1) % len(l)]
    l[i].next=l[(i+1 )% len(l)]
    
for v in l:
    if v.value > 0 :
        v.moveforward(v.value)
    if v.value < 0 :
        v.movebackward(-v.value)

newl = [0]
curv = v0.next
while curv.value != 0:
    newl.append(curv.value)
    curv = curv.next

for k in 1000, 2000, 3000:
    num = newl[k % len(newl)]
    print(num)
    result+=num
print(result)

# PART 2
result = 0
for line in lines:
    ...
print(result)
