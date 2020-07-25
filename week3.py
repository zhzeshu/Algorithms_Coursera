import statistics

def quicksort(a):
    quicksort1(a, 0, len(a)-1)


def quicksort1(a, l, r):
    global comparisons
    if l < r:
        comparisons += (r - l)
        # a[l], a[r] = a[r], a[l]

        if (r - l + 1) % 2 == 0:
            pi = (r - l + 1)//2 + l - 1
        else:
            pi = (r - l + 1) // 2 + l
        pindex = a.index(statistics.median([a[l], a[r], a[pi]]))
        a[l], a[pindex] = a[pindex], a[l]

        p = Partition1(a, l, r)
        quicksort1(a, l, p-1)
        quicksort1(a, p+1, r)


# first element as pivot
def Partition1(a, l, r):
    pivot = a[l]
    i = l + 1
    for j in range(l+1, r+1):
        if a[j] < pivot:
            a[j], a[i] = a[i], a[j]
            i += 1
    a[l], a[i-1] = a[i-1], a[l]
    return i-1


# last element as pivot
def Partition2(a, l, r):
    pivot = a[r]
    i = l
    for j in range(l, r):
        if a[j] < pivot:
            a[j], a[i] = a[i], a[j]
            i += 1
    a[i], a[r] = a[r], a[i]
    return i


# middle element as pivot
def Partition22(a, l, r):
    pivot = a[l]
    i = l
    for j in range(l, r):
        if a[j] < pivot:
            a[j], a[i] = a[i], a[j]
            i += 1
    a[i], a[r] = a[r], a[i]
    return i


def Partition3(a, l, r):
    if (r-l+1)%2 == 0:
        pi = (r-l+1)//2 + l - 1
    else:
        pi = (r-l+2)//2 + l - 1
    pivot = a[pi]
    a[l], a[pi] = a[pi], a[l]
    i = l + 1
    for j in range(l+1, r+1):
        if a[j] < pivot:
            a[j], a[i] = a[i], a[j]
            i += 1
    a[l], a[i-1] = a[i-1], a[l]
    return i - 1


with open("QuickSort.txt") as f:
    a = [int(line.rstrip()) for line in f]
# a=[2, 20, 1, 15, 3, 11, 13, 6, 16, 10, 19, 5, 4, 9, 8, 14, 18, 17, 7, 12]
comparisons = 0
quicksort(a)
print(comparisons)
print(a)


