
from collections import defaultdict


def multi_dict(k):
    if k == 1:
        return defaultdict()
    else:
        return defaultdict(lambda: multi_dict(k-1))


def bellman_ford(edges, num_vertices, dist):
    dist[num_vertices + 1] = 0
    for i in range(num_vertices):
        for (src, des, weight) in edges:
            if (dist[src] != float("Inf")) and (dist[src]+weight < dist[des]):
                dist[des] = dist[src] + weight
    for u, v, w in edges:
        if dist[u] != float("inf") and dist[u] + w < dist[v]:
            print("graph contains negative weight cycle")
            return
    return dist


graph = multi_dict(2)
with open('g3.txt') as f:
    first_line = f.readline()
    num_of_vertices, num_of_edges = list(map(int, first_line.split()))
    edges = []
    data = f.readlines()
    for line in data:
        v = list(map(int, line.split()))
        edges.append(v)
        graph[v[0]][v[1]] = v[2]

f.close()
s = num_of_vertices + 1
dist = multi_dict(1)
for i in range(1, num_of_vertices + 1):
    graph[s][i] = 0
    edges.append([s, i, 0])
    dist[i] = float("inf")

modified_weight = bellman_ford(edges, num_of_vertices, dist)

L = []
for i in range(1, 1001):
    L.append(dist[i])
print(min(L))
