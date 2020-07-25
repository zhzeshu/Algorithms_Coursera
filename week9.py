# greedy algorithm
# 1
"""
Your task in this problem is to run the greedy algorithm that schedules jobs in decreasing
order of the difference (weight - length).
Recall from lecture that this algorithm is not always optimal. IMPORTANT:
if two jobs have equal difference (weight - length), you should schedule
the job with higher weight first.

Your task now is to run the greedy algorithm that schedules jobs (optimally) in decreasing
order of the ratio (weight/length). In this algorithm, it does not matter how you break ties.
You should report the sum of weighted completion times of the resulting schedule ---
a positive integer --- in the box below.
"""


def sum_weight_time(job):
    leng, w, wct = 0, 0, 0
    for i in range(n):
        w = job[i][1]
        leng += job[i][2]
        wct += w*leng
    return wct


jobs = []
jobs2 = []
weight, length = 0, 0
with open("jobs.txt", 'r') as f:
    n = int(f.readline())
    for line in f:
        weight = int(line.split()[0])
        length = int(line.split()[1])
        jobs.append([weight-length, weight, length])
        jobs2.append([weight/length, weight, length])

# print(len(jobs))
jobs = sorted(jobs, key=lambda x: (x[0], x[1]), reverse=True)
jobs2 = sorted(jobs2, key=lambda x: (x[0], x[1]), reverse=True)
# print(jobs[:10])
# print(len(jobs))

print(sum_weight_time(jobs))
print(sum_weight_time(jobs2))
