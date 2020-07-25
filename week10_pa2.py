"""
1. read all lines and convert it to integers
 store them in a list, not a set
2. create a map(dict) mapping from number=>array of node IDs,
 mapping values is a set and not just an int
3. create an UnionFind instance with the nodes[0...n-1]
4. create an array of bit-masks for the distances. This can be done with with bit-shifts
 create bit-masks for Hamming distance 1 by shifting the 1 bit iteratively by 24 positions


"""
import numpy as np
from networkx.utils.union_find import UnionFind
import itertools
from timeit import default_timer as timer


def read_data():
    # read all line, convert the bit strings to integers
    bit_list = []
    with open("clustering_big.txt", "r") as f:
        first_line = [int(i) for i in f.readline().split()]
        vertices = first_line[0]
        bit_len = first_line[1]
        mask_list = [2**k for k in range(bit_len-1, -1, -1)]
        data = f.readlines()
        for line in data:
            # node = [int(i) for i in line.split()]
            # value = sum(np.array(node)*np.array(mask_list))
            value = int(line.replace(' ', ''), base=2)
            bit_list.append(value)
        f.close()
    # print(bit_list[:10])
    # print(len(bit_list))

    # create a map mapping from number to array of node IDs
    graph = {}
    i = 0
    for item in bit_list:
        if item not in graph:
            graph[item] = list()
            graph[item].append(i)
            i += 1
        else:
            graph[item].append(i)
            i += 1
    return graph, vertices, bit_len


# start = timer()
# g, v, l1 = read_data()
# print(g, v, l1)
# print(len(g))
# readend = timer()
# print("reading data:", readend-start)


def get_union_find_instance(ln):
    # create a UnionFind-instance with nodes[0...n-1]
    my_set = set([i for i in range(ln)])
    u_find = UnionFind(my_set)
    return u_find


def get_mask(bit_len):
    # create bit masks for Hamming distance 1 by shifting
    # 1 bit iteratively by 24 positions
    bitmask_1 = [1 << i for i in range(bit_len)]

    # create bit masks for Hamming distance 2 by combination of
    # 2 one shift
    bitmask_2_pair = list(itertools.combinations(range(bit_len), 2))
    # print(bitmask_2_pair)
    bitmask_2 = []
    for i in range(len(bitmask_2_pair)):
        v1 = bitmask_2_pair[i][0]
        v2 = bitmask_2_pair[i][1]
        b1 = 1 << v1
        b2 = 1 << v2
        b3 = b1 ^ b2
        bitmask_2.append(b3)
    bitmask = bitmask_1 + bitmask_2
    return sorted(bitmask)


# dict find is much faster than list
def union_graph(graph, bitmask, ln):
    my_set = set([i for i in range(ln)])
    u_find = UnionFind(my_set)

    for key in graph:
        l_list = list(graph[key])
        l_value = len(l_list)
        while l_value > 1:
            u_find.union(l_list[l_value-1], l_list[l_value-2])
            l_value -= 1

    for value in bitmask:
        for key1 in graph:
            key2 = key1 ^ value
            if key2 in graph:
                x1 = graph[key1]
                x2 = graph[key2]
                u_find.union(x1[0], x2[0])

    pointer_set = set(u_find[x] for x in my_set)
    num_clusters = len(pointer_set)
    return num_clusters


t0 = timer()
g, v, l1 = read_data()
t1 = timer()
print(t1-t0)
mask = get_mask(l1)
t2 = timer()
print(t2-t1)
num = union_graph(g, mask, v)
t3 = timer()
print(t3-t2)
print(num)