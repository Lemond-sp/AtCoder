N = int(input())
xy = [map(int, input().split()) for _ in range(N)]
x, y = [list(i) for i in zip(*xy)]
res = []

for i in range(N):
    res.append(y[i] - x[i])


print(max(res) + sum(x))
