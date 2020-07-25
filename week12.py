from collections import defaultdict
from timeit import default_timer as timer
import sys


# sys.setrecursionlimit(50000)
with open("knapsack1.txt", "r") as f:
    first_line = [int(i) for i in f.readline().split()]
    W = first_line[0]
    n = first_line[1]
    data = f.readlines()
    v = [0]
    w = [0]
    for line in data:
        l = [int(j) for j in line.split()]
        v.append(l[0])
        w.append(l[1])


def multi_dict(k):
    if k == 1:
        return defaultdict()
    else:
        return defaultdict(lambda: multi_dict(k-1))


# direct method
A = multi_dict(2)
for x in range(W+1):
    A[0][x] = 0
for i in range(1, n+1):
    if i > 1:
        del A[i-2]
    for x in range(0, W+1):
        if x-w[i] >= 0:
            A[i][x] = max(A[i-1][x], A[i-1][x-w[i]]+v[i])
        else:
            A[i][x] = A[i-1][x]

print(A[n][W])


# def knapSack(Wt, wt, vt, nt):
#     if nt == 0 or Wt == 0:
#         return 0
#     if wt[n-1] > Wt:
#         return knapSack(Wt, wt, vt, n-1)
#     else:
#         return max(
#             vt[n-1]+knapSack(Wt-wt[nt-1], wt, vt, n-1),
#             knapSack(Wt, wt, vt, n-1)
#         )
#
#
# print(knapSack(W, w, v, n))