from operator import mul
from functools import reduce


n = int(input())
a = list(map(int, input().split()))


def cmb(n, r):
    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


def f(a, b):
    k = str(a + b)
    if len(k) < 8:
        res = a + b
    else:
        res = int(k[len(k) - 8 :])

    return res


res = 0
# 全要素に対して計算しておく。
#
a = cmb(n, 2)
print(a)
# for v in cmb(n, 2):
#     res += f(a[v[0]], a[v[1]])

# print(res)


# print(res)
# print((a[0] + a[1]) % pow(10, 8))
