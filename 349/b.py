from collections import defaultdict

s = input()

d = defaultdict(int)
res = defaultdict(int)

# ある文字の出現頻度の計算
for c in s:
    d[c] += 1

# i回現れている文字の種類数
for k, v in d.items():
    res[str(v)] += 1

# 条件
flag = 0
for _, v in res.items():
    if v == 0 or v == 2:
        continue
    else:
        flag = 1
        break

if flag:
    print("No")
else:
    print("Yes")
