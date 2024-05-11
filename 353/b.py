N, K = map(int, input().split())
A = list(map(int, input().split()))

tmp = 0
res = 0
i = 0

while i < N:
    tmp = 0
    res += 1
    while tmp + A[i] <= K:
        tmp += A[i]
        i += 1
        if i == N:
            break

print(res)
