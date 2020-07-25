from math import *


def calculation(x, y):
    if x < 10 or y < 10:
        return x*y
    else:
        m = max(int(log10(x)+1), int(log10(y)+1))
        if m % 2 != 0:
            m -= 1
        m2 = int(m/2)

        a, b = x // (10**m2), x % (10**m2)
        c, d = y // (10**m2), y % (10**m2)
        ac = calculation(a, c)
        bd = calculation(b, d)
        ab_cd = calculation(a+b, c+d) - ac - bd
        prod = ac*(10**m) + ab_cd*(10**m2) + bd
        return prod


print(calculation(3141592653589793238462643383279502884197169399375105820974944592,
                 2718281828459045235360287471352662497757247093699959574966967627))
