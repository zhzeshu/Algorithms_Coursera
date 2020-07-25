import random


def get_data():
    graph = {}
    data = open("kargerMinCut.txt", "r")
    for line in data:
        new_list = [int(x) for x in line.split()]
        graph[new_list[0]] = new_list[1:]
    data.close()
    return graph


def print_graph(graph):
    for key in graph.keys():
        print("{}:{}".format(key, graph[key]))


def random_vertex(graph):
    v1 = random.choice(list(graph.keys()))
    v2 = random.choice(list(graph[v1]))
    return v1, v2


def find_min_cut(graph):
    length = []
    while len(graph.keys()) > 2:
        v1, v2 = random_vertex(graph)
        graph[v1].extend(graph[v2])
        for x in graph[v2]:
            graph[x].remove(v2)
            graph[x].append(v1)
        graph[v1] = [x for x in graph[v1] if x != v1]
        graph.pop(v2)

    for vertex in graph.keys():
        length.append(len(graph[vertex]))
    return length[0]


def random_find_min_cut(num):
    graph = get_data()
    min_cut = find_min_cut(graph)
    for i in range(num):
        graph = get_data()
        out = find_min_cut(graph)
        if min_cut > out:
            min_cut = out
    return min_cut


print(random_find_min_cut(100))

# graph, super_graph = get_data()
# print_graph(graph)
