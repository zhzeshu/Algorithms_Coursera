# recursive
N = 875714
# s = 0
# t = 0


def read_data(file_name):
    graph = [[] for i in range(N + 1)]
    graph_reverse = [[] for i in range(N + 1)]

    with open(file_name, "r") as data:
        for line in data:
            new_list = [int(x) for x in line.split() if x != "\n"]
            v1 = new_list[0]
            v2 = new_list[1]
            graph[v1].append(v2)
            graph_reverse[v2].append(v1)
    return graph, graph_reverse


def dfs_loop(G, arr):
    global s, visited, t
    for i in arr:
        if visited[i] == 0:
            s = i
            dfs(G, i)


def dfs(G, i):
    global visited, SCC, s, f, t
    visited[i] = 1
    SCC[s].append(i)
    for j in G[i]:
        if visited[j] == 0:
            dfs(G, j)
    t += 1
    f[i] = t


if __name__ == "__main__":
    g, gr = read_data("data4.txt")

    stack_node = []
    i = N
    t = 0
    f = {}

    while i > 0:
        f[i] = None
        if len(gr[i]) > 0:
            stack_node.append(i)
        i -= 1


    # 1
    visited = [0] * (N + 1)
    SCC = [[] for i in range(N + 1)]
    dfs_loop(gr, stack_node)

    SCC.sort(key=len, reverse=True)
    print(SCC[:5])
    scc_num = [len(SCC[i]) for i in range(5)]
    print(scc_num)

    # 2
    f1 = {}
    arr2 = []
    for i in range(1, N + 1):
        if f[i] is not None:
            if f[i] not in f1.keys():
                f1[f[i]] = []
            f1[f[i]] = i
    alist = [int(x) for x in f1.keys()]
    alist.sort(reverse=True)
    for j in alist:
        arr2.append(f1[j])

    visited = [0] * (N + 1)
    SCC = [[] for i in range(N + 1)]
    dfs_loop(g, arr2)
    SCC.sort(key=len, reverse=True)
    print(SCC[:5])
    scc_num = [len(SCC[i]) for i in range(5)]
    print(scc_num)


