n, q = map(int, input().split())
t = input().split()

lists = [1] * n
print(len(lists))

for i in t:
    res = lists[int(i) - 1]
    if res == 0:
        res = 1
    else:
        res = 0
    lists[int(i) - 1] = res

print(sum(lists))
