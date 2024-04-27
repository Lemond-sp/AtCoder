N = int(input())
A = list(map(int, input().split()))

s = []

# append(ok)
for i in range(N):
    s.append(A[i])
    while len(s) > 1:
        if s[-1] == s[-2]:
            s.append(s[-1] + 1)
            del s[-3:-1]
        else:
            break

print(len(s))
