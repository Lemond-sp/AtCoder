import itertools

n = int(input())
a = list(map(int, input().split()))


def f(a, b):
    k = str(a + b)
    if len(k) < 8:
        res = a + b
    else:
        res = int(k[len(k) - 8 :])

    return res


res = 0

for v in itertools.combinations(range(n), 2):
    res += f(a[v[0]], a[v[1]])

print(res)
# print(res)
# print((a[0] + a[1]) % pow(10, 8))
