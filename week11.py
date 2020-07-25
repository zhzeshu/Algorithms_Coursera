
import heapq
import os
from collections import defaultdict

# class Node:
#     def __init__(self,cost):
#         self.cost = cost
#         self.left = None
#         self.right = None
#     # Add the relevant things like cost and left and right children
#     # In this way keeping only track of the root keeps the track of the
#     # whole tree
#
#     def __lt__(self,node):
#         return self.cost > node.cost
#     # Operate overload and compare on basis of cost
#
# def Merge(node1,node2):
#
#   # Merge two trees and return the root of the merged tree
#   # Keep note of the things you want to have in your merged tree like
#   # the freq should be sum of frequencies of node1 and node2
# def DFS(root):
# # Apply DFS to find the depths of leaves of the tree and in this way
# # find max and min depths
# class Heap:
#   # Create a Binary min heap

with open("huffman.txt", "r") as f:
    symbols_num = int(f.readline())
    data = f.readlines()
    heap = []
    i = 0
    for line in data:
        heap.append((int(line), [i]))
        i += 1
    f.close()
print(heap)

code = defaultdict(list)

heapq.heapify(heap)
while len(heap) > 1:
    freq0, letters0 = heapq.heappop(heap)
    for letter in letters0:
        code[letter].insert(0, "0")
    freq1, letters1 = heapq.heappop(heap)
    for letter in letters1:
        code[letter].insert(0, "1")
    heapq.heappush(heap, (freq0+freq1, letters0+letters1))

for k, v in code.items():
    code[k] = ''.join(v)
# sorted(code.items())
print(code.items())
print(list(code.items())[-1])
print(list(code.items())[0])
