N = int(input())
xy = [input().split() for _ in range(N)]
s, c = [list(i) for i in zip(*xy)]
s_sorted = sorted(s)

ans = 0
for i in c:
    ans += int(i)

print(s_sorted[ans % len(s)])
