N = int(input())

# (N,M)行列データ
scores = []
scores = [list(map(int, input().split())) for _ in range(N)]

x = 0
y = 0
for res in scores:
    x += res[0]
    y += res[1]

if x < y:
    print("Aoki")
elif y < x:
    print("Takahashi")
else:
    print("Draw")
