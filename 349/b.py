from collections import defaultdict

s = input()

d = defaultdict(int)
res = defaultdict(int)
for c in s:
    d[c] += 1

flag = 0
for k, v in d.items():
    res[str(v)] += 1

for _, v in res.items():
    if v == 0 or v == 2:
        continue
    else:
        flag = 1
        break

if flag == 1:
    print("No")
else:
    print("Yes")
