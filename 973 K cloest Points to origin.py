import math
from heapq import heappush, heappop


def kClosest(points, K):
    points.sort(key=lambda p: p[0]**2 + p[1]**2)
    return points[:K]





