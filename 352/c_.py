N = int(input())
s, h = 0, 0

for _ in range(N):
    A, B = map(int, input().split())
    s += A
    h = max(h, B - A)  # 差分が一番大きいものを足す
print(s + h)
