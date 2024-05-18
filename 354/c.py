N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]
# a:強さ、c：コスト
a_d = {i[1]: i[0] for i in xy}
a_ans = {i[1]: j for j, i in enumerate(xy)}

a_dict = dict(sorted(a_d.items(), key=lambda x: x[1], reverse=True))

i = 0
ans_key = []

for _ in range(N):
    a = list(a_dict.values())
    c = list(a_dict.keys())
    if c == list(sorted(c, reverse=True)) or c == min(c):
        break
    for j, k in enumerate(c[i + 1 :]):
        if c[i] < k:
            del a_dict[k]
    i += 1

print(len(a_dict))
ans = sorted([a_ans[x] + 1 for x in a_dict.keys()])
print(*ans)
