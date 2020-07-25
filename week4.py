import random
from random import randint
from math import log
random.seed(3)


class find_mincut():
    def __init__(self, filename):
        self.graph = {}
        self.total_edge = 0
        self.vertex_count = 0
        with open(filename, "r") as graph_file:
            for line in graph_file:
                new_line = [int(x) for x in line.split() if x != '\n']
                vertex = new_line[0]
                vertex_edge = new_line[1:]
                self.graph[vertex] = vertex_edge
                self.total_edge += len(vertex_edge)
                self.vertex_count += 1
        self.supervertices = {}
        for key in self.graph:
            self.supervertices[key] = [key]

    def random_edge(self):
        from_vertex = random.choice(list(self.graph.keys()))
        to_vertex = random.choice(list(self.graph[from_vertex]))
        return from_vertex, to_vertex

    def find_cut(self):
        min_cut = 0
        while len(self.graph) > 2:
            v1, v2 = self.random_edge()
            self.total_edge -= len(self.graph[v1])
            self.total_edge -= len(self.graph[v2])
            self.graph[v1].extend(self.graph[v2])
            for vertex in self.graph[v2]:
                self.graph[vertex].remove(v2)
                self.graph[vertex].append(v1)
            self.graph[v1] = [x for x in self.graph[v1] if x != v1]
            self.total_edge += len(self.graph[v1])
            self.graph.pop(v2)
            self.supervertices[v1].extend(self.supervertices.pop(v2))
        for edges in self.graph.values():
            min_cut = len(edges)
        return min_cut, self.supervertices

    def print_graph(self):
        for key in self.graph:
            print("{}:{}".format(key, self.graph[key]))


# graph = find_mincut("data1.txt")
# graph.print_graph()
# out = graph.find_cut()
# print("min_cut: {}\nsupervertices: {}".format(out[0], out[1]))

def full_karger(iterations):
    graph = find_mincut("kargerMinCut.txt")
    out = graph.find_cut()
    min_cut = out[0]
    supervertices = out[1]

    for i in range(iterations):
        graph = find_mincut("kargerMinCut.txt")
        out = graph.find_cut()
        if out[0] < min_cut:
            min_cut = out[0]
            supervertices = out[1]

    return min_cut, supervertices


out = full_karger(400)
print("min_cut: {}\nsupervertices: {}".format(out[0], out[1]))



