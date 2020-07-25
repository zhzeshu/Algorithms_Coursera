"""
In this programming problem and the next you'll code up the clustering algorithm from lecture
for computing a max-spacing kkk-clustering.

Download the text file below.
clustering1.txt

This file describes a distance function (equivalently, a complete graph with edge costs).
It has the following format:

[number_of_nodes]

[edge 1 node 1] [edge 1 node 2] [edge 1 cost]

[edge 2 node 1] [edge 2 node 2] [edge 2 cost]

...

There is one edge (i,j)(i,j)(i,j) for each choice of 1≤i<j≤n1 \leq i \lt j \leq n1≤i<j≤n,
where nnn is the number of nodes.

For example, the third line of the file is "1 3 5250", indicating that the distance between nodes
1 and 3 (equivalently, the cost of the edge (1,3)) is 5250. You can assume that distances
are positive, but you should NOT assume that they are distinct.

Your task in this problem is to run the clustering algorithm from lecture on this data set,
 where the target number kkk of clusters is set to 4. What is the maximum spacing of a 4-clustering?

ADVICE: If you're not getting the correct answer, try debugging your algorithm using some
small test cases. And then post them to the discussion forum!

"""


def cluster(edges, k, vertices):
    clusters = []
    for i in range(1, vertices+1):
        clusters.append({i})
    while len(clusters) != k:
        edge = edges.pop(0)
        first_flag = False
        second_flag = False
        for i in range(len(clusters)):
            if edge[0] in clusters[i]:
                first_index = i
                first_flag = True
            if edge[1] in clusters[i]:
                second_index = i
                second_flag = True
            if first_flag and second_flag:
                break
        if first_index != second_index:
            if first_index < second_index:
                clusters.append(clusters.pop(first_index).union(clusters.pop(second_index-1)))
            else:
                clusters.append(clusters.pop(first_index).union(clusters.pop(second_index)))

    same_cluster = True
    while same_cluster:
        edge = edges.pop(0)
        for j in range(k):
            if (edge[0] in clusters[j]) and (edge[1] not in clusters[j]):
                ans = edge[2]
                same_cluster = False
    return ans


edges = []
with open("clustering1.txt", "r") as f:
    vertices = int(f.readline())
    data = f.readlines()
    for line in data:
        edge = list(map(int, line.split()))
        edges.append(edge)
    f.close()

edges.sort(key=lambda x: x[2])
print(cluster(edges, 4, vertices))
# print(edges)
# print(len(edges))
# print(nodes)
# print(edge_num)
