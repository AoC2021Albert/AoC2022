from sys import stdin
from math import sqrt

sgn = lambda x: x/abs(x) if x != 0 else 0
vectorlen = lambda v: sqrt(v[X]**2 + v[Y]**2)

X=0 # First element is the X coordinate
Y=1 # Second element is the Y coordinate

def step(knots, dz):
    headknot = knots[0]
    headknot[X] += dz[X]
    headknot[Y] += dz[Y]
    for i in range(1, len(knots)):
        dv = [knots[i-1][X] - knots[i][X],
              knots[i-1][Y] - knots[i][Y]]
        if vectorlen(dv) > sqrt(2):
            knots[i][X] += sgn(dv[X])
            knots[i][Y] += sgn(dv[Y])

direction = { 'R': [1,0], 'U': [0,1], 'L': [-1,0], 'D': [0,-1] }
knots = [[0,0] for _ in range(10)]
visited = [{} for _ in range(10)]

for line in stdin.readlines():
    d, n = line.split()
    for _ in range(int(n)):
        step(knots, direction[d])
        for i in range(10):
            visited[i][(knots[i][X],knots[i][Y])] = True

print(len(visited[1]))
print(len(visited[9]))
