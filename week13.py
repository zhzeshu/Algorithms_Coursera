from math import inf

def floyd_warshall(graph , n):
    book_keeper= []
    for i in range(n+1):
        book_keeper.append([])
        for j in range(n+1):
            book_keeper[i].append([])
            for k in range(2):
                book_keeper[i][j].append(0)
                if k == 0:
                    if i == j:
                        book_keeper[i][j][0] = 0
                    elif graph.get((i,j)) != None:
                        book_keeper[i][j][0] = graph[(i,j)]
                    else:
                        book_keeper[i][j][0] = inf
    shortest_path= inf
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                book_keeper[i][j][1] = min(book_keeper[i][j][0] , book_keeper[i][k][0] + book_keeper[k][j][0])
                if k == n:
                    if shortest_path > book_keeper[i][j][1]:
                        shortest_path = book_keeper[i][j][1]
                if i == j:
                   if book_keeper[i][j][1]<0:
                       return 'NULL'
                book_keeper[i][j][1] , book_keeper[i][j][0] = book_keeper[i][j][0] ,book_keeper[i][j][1]
    return shortest_path


graph = {}
with open('g3.txt') as f:
    first_line = f.readline()
    num_of_vertices , num_of_edges = list(map(int,first_line.split()))
    data = f.readlines()
    for line in data:
        elements = list(map(int,line.split()))
        if graph.get((elements[0],elements[1])) == None:
            graph[(elements[0],elements[1])] = elements[2]
        else:
            if graph[(elements[0],elements[1])] > elements[2]:
                graph[(elements[0],elements[1])] = elements[2]


f.close()

print(floyd_warshall(graph, num_of_vertices))