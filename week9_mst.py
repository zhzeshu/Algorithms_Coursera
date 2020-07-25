"""
This file describes an undirected graph with integer edge costs. It has the format
[number_of_nodes] [number_of_edges]
[one_node_of_edge_1] [other_node_of_edge_1] [edge_1_cost]
[one_node_of_edge_2] [other_node_of_edge_2] [edge_2_cost]
...

For example, the third line of the file is "2 3 -8874", indicating that there is an edge
connecting vertex #2 and vertex #3 that has cost -8874.

You should NOT assume that edge costs are positive, nor should you assume that
they are distinct.

Your task is to run Prim's minimum spanning tree algorithm on this graph. You should report
the overall cost of a minimum spanning tree --- an integer, which may or may not be negative
--- in the box below.

IMPLEMENTATION NOTES: This graph is small enough that the straightforward O(mn) time
implementation of Prim's algorithm should work fine. OPTIONAL: For those of you seeking
an additional challenge, try implementing a heap-based version. The simpler approach,
which should already give you a healthy speed-up, is to maintain relevant edges in a heap
(with keys = edge costs). The superior approach stores the unprocessed vertices in the heap,
 as described in lecture. Note this requires a heap that supports deletions,
 and you'll probably need to maintain some kind of mapping between vertices and their
 positions in the heap.
"""
from heapq import heappop, heappush, heapify
import random
# heap_vertices = []
# heapify(heap_vertices)

with open("edges.txt", "r") as f:
    f_file = f.readlines()
    first_line = [int(i) for i in f_file[0].split()]
    vertices = first_line[0]
    edges = first_line[1]
    graph = [[float("inf") for i in range(vertices+1)] for j in range(vertices+1)]
    V = set()
    for line in f_file[1:]:
        v1 = int(line.split()[0])
        v2 = int(line.split()[1])
        cost = int(line.split()[2])
        graph[v1][v2] = cost
        graph[v2][v1] = cost
        V.add(v1)
        V.add(v2)
# for i in range(vertices+1):
#     print((i, graph[i]))
# print(vertices)
# print(edges)
print(len(V))

# O(mn)
X = set()
s = random.choice(tuple(V))
X.add(s)
V.remove(s)
# print(X)
T = 0
edge_list = []

while len(V) > 0:
    cost = 99999
    for item in X:
        for v2 in V:
            # print((item, v2))
            if graph[item][v2] != "inf" and graph[item][v2] < cost:
                cost = graph[item][v2]
                cheapest_point = v2
    T += cost
    edge_list.append(cost)
    X.add(cheapest_point)
    V.remove(cheapest_point)


print(T)
# print(edge_list)


