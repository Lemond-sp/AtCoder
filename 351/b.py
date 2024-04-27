n = int(input())
xy = [input().split() for _ in range(n * 2)]

for i in range(n):
    if xy[i][0] != xy[i + n][0]:
        for j in range(n):
            if xy[i][0][j] != xy[i + n][0][j]:
                print(f"{i+1} {j+1}")
