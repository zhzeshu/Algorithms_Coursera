import math
import numpy as np
import time

def getDist(p1, p2):
    a = p1[0] - p2[0]
    b = p1[1] - p2[1]
    return math.sqrt(a*a + b*b)


f = open("nn.txt")
nCities = int(f.readline())
lines = f.readlines()
f.close()
cities = []
for line in lines:
    idx, x, y = map(float, line.split())
    cities.append([x, y])

visited = [False for i in range(nCities)]
currCity = 0
visited[0] = True
nVisited = 1
cost = 0.0

start_time = time.time()
while nVisited < nCities:
    # print(nVisited)
    nextCity = -1
    minDist = float('inf')
    for c in range(nCities):
        if visited[c]:  continue
        eclDist = getDist(cities[currCity], cities[c])
        if eclDist < minDist:
            nextCity = c
            minDist = eclDist
    currCity = nextCity
    cost += minDist
    nVisited += 1
    visited[nextCity] = True
    if nVisited%1000 == 0:
        print(nVisited, time.time()-start_time)
cost += getDist(cities[currCity], cities[0])
print(cost)