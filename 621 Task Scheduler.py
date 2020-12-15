
def leastInterval(tasks, n):
    frequences = [0]*26
    for letter in tasks:
        frequences[ord(letter) - ord('A')] += 1
    frequences.sort()

    f_max = frequences.pop()
    f_idel = (f_max-1)*n
    while frequences and f_idel > 0:
        f_idel -= min(f_max-1, frequences.pop())
    f_idel = max(0, f_idel)

    return f_idel + len(tasks)


def leastInterval2(tasks, n):
    frequences = [0] * 26
    for letter in tasks:
        frequences[ord(letter) - ord('A')] += 1

    f_max = max(frequences)
    n_max = frequences.count(f_max)

    return max(len(tasks), (f_max-1)*(n+1) + n_max)


print(leastInterval(["A","A","A","B","B","B"], 2))

