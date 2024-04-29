n = int(input())

A = list(map(int, input().split()))


def find_list(i, x):
    if x in i:
        return True
    else:
        return False


lists = range(1, len(A) + 1)

bins = [-1 if l == a else 1 for l, a in zip(lists, A)]

res_list = []

while find_list(bins, 1):  # 1が残っている間
    print(bins)
    a = [i for i, x in enumerate(bins) if x == 1]
    if len(a) > 1:
        n = a[1]
        res_list.append([a[0], a[1]])
    else:
        n = a[1] - 1 if a[1] != 0 else a[1] + 1
        res_list.append([a[0], n])
    N = A[n]
    A[n] = A[a[0]]
    A[a[0]] = N
    bins = [-1 if l == a else 1 for l, a in zip(lists, A)]

print(len(res_list))

for i in res_list:
    i = sorted(i)
    print(f"{i[0] + 1} {i[1] + 1}")
