# distinct number pairs wherein x != y
# as soon as you find a pair of distinct(x, y), increase the count
# 2-sum problem: insert elements A into hash table, for each x in A, lookup t - x
import collections
from heapq import heappush, heappop, heapify


def hash_2sum(arr):
    hashtable = {}
    num_hash = {}
    for i in range(len(arr)):
        hashtable[arr[i]] = arr[i]

    alist = []
    for x in hashtable.keys():
        for k in range(-1000-x, 1000-x+1):
            if k in hashtable and k != x:
                num_hash[x+k] = [x, k]
                alist.append([x, k])
    # return total_num//2
    return num_hash


def list_2sum(arr):
    len_arr = len(arr)
    graph = {}
    for x in arr:
        p = binary_search(arr, 0, len_arr-1, -10000-x)
        q = binary_search(arr, p, len_arr-1, 10000-x)
        # if p == q:
        #     continue
        for i in range(p, q+1):
            if -10000 <= arr[i] + x <= 10000:
                graph[arr[i] + x] = [arr[i], x]
    return graph

    # return graph


def binary_search(arra, low, high, x):
    if high == low:
        return low
    if high > low:
        mid = (high+low)//2
        if arra[mid] == x:
            return mid
        elif arra[mid] > x > arra[mid - 1]:
            return mid-1
        elif arra[mid] < x < arra[mid + 1]:
            return mid
        elif arra[mid] > x:
            return binary_search(arra, low, mid-1, x)
        else:
            return binary_search(arra, mid+1, high, x)
    else:
        return -1


with open("2sum.txt") as f:
    arr = [int(line.rstrip()) for line in f]
arr = list(set(list(arr)))
arr.sort()

print(len(list_2sum(arr)))
# print(binary_search(arr, 0, len(arr), 6.5))



# print()




