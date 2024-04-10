from collections import defaultdict

cnt_dict = defaultdict(int)

s = input()

for c in s:
    cnt_dict[c] += 1
# print(cnt_dict)

sorted_cnt = dict(sorted(cnt_dict.items(), key=lambda i: i[1], reverse=True))

# print(sorted_cnt)

ans = [k[0] for k in sorted_cnt.items() if k[1] == max(sorted_cnt.values())]

print(sorted(ans)[0])
