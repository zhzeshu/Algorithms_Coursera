import matplotlib.pyplot as plt
import itertools
from collections import defaultdict
import math


def multi_dict(k):
    if k == 1:
        return defaultdict()
    else:
        return defaultdict(lambda: multi_dict(k-1))


def powerset(iterable):
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r)
                                         for r in range(len(s)+1))


X = []
Y = []
with open("tsp.txt", "r") as f:
    vertices = int(f.readline())
    data = f.readlines()
    for line in data:
        X.append(float(list(line.split())[0]))
        Y.append(float(list(line.split())[1]))
# plt.scatter(X, Y)
# plt.show()
dist = multi_dict(2)
L = []
for i in range(vertices):
    L.append(i+1)
    for j in range(vertices):
        dist[i][j] = math.dist([X[i], Y[i]], [X[j], Y[j]])
        dist[j][i] = math.dist([X[i], Y[i]], [X[j], Y[j]])

k = powerset(L)
S = []
A = multi_dict(2)
for s in k:
    if 1 in s:
        S.append(s)
        A[s][1] = float("inf")


# A[{1}][1] = 0
# for s in S:
#     A[s][1] = float("inf")
# for m in range(2, vertices):
#     for s in S:
#         if len(s) == m:
#             for j in s:
#                 if j != 1:
#                     for k in s:
#                         if k != j:
#                             A[s][j] = min(A[s-{j}][k], dist[k][j])

