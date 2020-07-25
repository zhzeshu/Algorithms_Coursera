
def sort1(arr):
    sort2(arr, 0, len(arr)-1)


def sort2(arr, lo, hi):
    if lo < hi:
        mid = (lo + hi)//2
        sort2(arr, lo, mid)
        sort2(arr, mid+1, hi)
        merge2(arr, lo, mid, hi)


def merge2(arr, lo, mid, hi):
    global inversion
    temp = [0]*(hi - lo + 1)
    i, j, k = lo, mid+1, 0
    while i <= mid and j <= hi:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            k += 1
            i += 1
        else:
            temp[k] = arr[j]
            k += 1
            j += 1
            inversion += mid - i + 1

    while i <= mid:
        temp[k] = arr[i]
        k += 1
        i += 1
    while j <= hi:
        temp[k] = arr[j]
        k += 1
        j += 1

    for m in range(lo, hi+1):
        arr[m] = temp[m - lo]


def printlist(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


with open("IntegerArray.txt") as f:
    arr = [int(line.rstrip()) for line in f]
inversion = 0
sort1(arr)
print(inversion)
