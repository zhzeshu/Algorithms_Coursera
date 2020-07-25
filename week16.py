
def dfs(graph, s, visited, st):
    st2 = [s]
    startTimes = set()
    while len(st2):
        v = st2[-1]
        if v not in startTimes:
            visited.add(v)
            if v in graph:
                for v2 in graph[v]:
                    if v2 not in visited:
                        st2.append(v2)
            startTimes.add(v)
        else:
            st.append(v)
            st2.pop()


FILE_NAMES = ["2sat1.txt", "2sat2.txt", "2sat3.txt", "2sat4.txt", "2sat5.txt", "2sat6.txt"]

for fname in FILE_NAMES:
    sat = True
    f = open(fname)
    nVar = int(f.readline())
    lines = f.readlines()
    f.close()
    graph = {}
    for line in lines:
        v1, v2 = map(int, line.split())  # A v B
        # ^A => B
        if -v1 in graph:
            graph[-v1].append(v2)
        else:
            graph[-v1] = [v2]
        # ^B => A
        if -v2 in graph:
            graph[-v2].append(v1)
        else:
            graph[-v2] = [v1]

# st: dfs finish time for all vertices
    visited = set()
    st = []
    for v in graph:
        if v not in visited:
            dfs(graph, v, visited, st)

    # graph reverse
    tGraph = {}
    for v1 in graph:
        for v2 in graph[v1]:
            if v2 in tGraph:
                tGraph[v2].append(v1)
            else:
                tGraph[v2] = [v1]

    visited = set()
    while len(st):
        v = st.pop()
        if v not in visited:
            scc = []
            dfs(tGraph, v, visited, scc)
            scc = set(scc)
            for v in scc:
                if -v in scc:
                    sat = False
    print(sat)