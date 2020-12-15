
def validPalindrome(s):
    for i in range(len(s)):
        s_new = s[:i] + s[i+1:]
        if s_new == s[::-1]:
            return True
    return s == s[::-1]

# print(validPalindrome('aba'))


def isPalidrome(s, low, high):
    while low < high:
        if s[low] != s[high]:
            return False
        low += 1
        high -= 1
    return True


def validPalindrome2(s):
    low = 0
    high = len(s) - 1
    while low < high:
        if s[low] == s[high]:
            low += 1
            high -= 1
        else:
            return isPalidrome(s, low+1, high) or isPalidrome(s, low, high-1)
    return True


print(validPalindrome2('abcddcba'))

