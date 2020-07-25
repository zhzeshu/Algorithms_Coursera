from collections import defaultdict

A = defaultdict()
W = defaultdict()
with open("mwis.txt", "r") as f:
    f_length = int(f.readline())
    A[0] = 0
    # W[0] = 0
    W[1] = int(f.readline())
    A[1] = W[1]
    data = f.readlines()
    i = 2
    for line in data:
        W[i] = int(line)
        A[i] = max(A[i-1], A[i-2]+W[i])
        i += 1
    f.close()
# for i in range(10):
#     print(A[i])
S = []
i -= 1
while i >= 2:
    if A[i-1] >= (A[i-2] + W[i]):
        i -= 1
    else:
        S.append(i)
        i -= 2
S.append(1)

T1 = [1, 2, 3, 4, 17, 117, 517, 997]
R = []
for j in T1:
    if j in S:
        R.append(1)
    else:
        R.append(0)
print(R)

