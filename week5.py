# iteration
N = 875714
leader = 0


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


# undiscovered white 1, discovered grey 2, finished black 3
def dfs_loop(G, arr):
    global color, t, leader
    for ii in arr:
        color[ii] = 1
    t = 0
    for i in arr:
        leader = i
        if color[i] == 1:
            dfs(G, i)


def dfs(G, s):
    global SCC, f, color, leader, t
    S = [s]
    while len(S) > 0:
        v = S.pop()
        if color[v] != 3:
            S.append(v)
            if color[v] == 1:
                color[v] = 2
                t += 1

            all_adj = True
            for w in G[v]:
                if color[w] == 1:
                    S.append(w)
                    all_adj = False
            if all_adj:
                color[v] = 3
                t += 1
                f[v] = t
                SCC[leader].append(v)
                S.pop()


if __name__ == "__main__":
    g, gr = read_data("SCC.txt")

    stack_node = []
    i = N
    t = 0
    f = {}
    color = {}

    while i > 0:
        f[i] = None
        color[i] = None
        if len(gr[i]) > 0:
            stack_node.append(i)
        i -= 1


    # 1
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

    SCC = [[] for i in range(N + 1)]
    dfs_loop(g, arr2)
    SCC.sort(key=len, reverse=True)
    print(SCC[:5])
    scc_num = [len(SCC[i]) for i in range(5)]
    print(scc_num)


