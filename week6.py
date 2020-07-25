import collections
import heapq
N = 200


def get_data():
    graph = [[0 for i in range(N + 1)] for j in range(N + 1)]
    data = open("dijkstraData.txt", "r")
    for line in data:
        line = line.split()
        row = int(line[0])
        for column in range(1, len(line)):
            node = [int(x) for x in line[column].split(',')]
            graph[row][node[0]] = node[1]
    return graph


# Dijkstra's algorithm, O(mn)
def dij(G):
    s = 1
    X = [s]
    A = [0 for i in range(N + 1)]
    A[s] = 0

    V = [i for i in range(1, N + 1)]
    V.remove(s)

    while len(V) > 0:
        B = dict()
        for row in X:
            for column in V:
                if G[row][column] != 0:
                    tot_value = A[row] + G[row][column]
                    if tot_value not in B.keys():
                        B[tot_value] = [row, column]

        min_key = min([int(x) for x in B.keys()])

        # print(key)
        column_min = B[min_key][1]
        # print(column_min)
        A[column_min] = min_key
        X.append(column_min)
        V.remove(column_min)

    return A


def get_dict_data(file_name):
    graph = collections.defaultdict(dict)
    data = open(file_name, "r")
    for line in data:
        line = line.split()
        v1 = int(line[0])
        for v2 in range(1, len(line)):
            nod1 = [int(x) for x in line[v2].split(',')]
            graph[v1][nod1[0]] = nod1[1]

    return graph


# mlog(n)
def dji_heap(G, v1):
    distances = {i: float("inf") for i in range(1, N + 1)}
    distances[v1] = 0
    min_dist = [(0, v1)]
    visited = set()

    while min_dist:
        cur_dist, cur = heapq.heappop(min_dist)
        if cur in visited:
            continue
        visited.add(cur)

        for neighbor in G[cur]:
            if neighbor in visited:
                continue
            this_dist = cur_dist + G[cur][neighbor]
            if this_dist < distances[neighbor]:
                distances[neighbor] = this_dist
                heapq.heappush(min_dist, (this_dist, neighbor))

    return distances


# G = get_dict_data("dijkstraData.txt")
# alist = dji_heap(G, 1)
# print(alist)

G = get_data()
alist = dij(G)

P = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
arr = []
for x in P:
    arr.append(alist[x])
print(arr)

# print(G)
# print(dij(G))
# print(alist)
