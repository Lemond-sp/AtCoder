n = int(input())

h = list(map(int, input().split()))
flag = 1

for i in range(n):
    if h[0] < h[i]:
        print(i + 1)
        flag = 0
        break

if flag == 1:
    print(-1)
