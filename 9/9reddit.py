from sys import stdin
from pprint import pprint

sgn = lambda x: x/abs(x) if x != 0 else 0

def step(knots, dz):
    knots[0] += dz
    for i in range(1, len(knots)):
        dv = knots[i-1] - knots[i]
        if abs(dv) > 1.5:
            knots[i] += sgn(dv.real) + 1j * sgn(dv.imag)

direction = { 'R': 1, 'U': 1j, 'L': -1, 'D': -1j }
knots = [0] * 10
visited = [{} for _ in range(10)]

for line in open("test.raw", "r").readlines():
    d, n = line.split()
    for _ in range(int(n)):
        step(knots, direction[d])
        for i in range(10):
            visited[i][knots[i]] = True

pprint(visited)
print(len(visited[1]))
print(len(visited[9]))
