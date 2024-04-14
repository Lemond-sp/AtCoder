s = input()
t = input()
s = s.upper()

s_set = set(s)
s_set2 = set(s)
s_set.add("X")
flag = 0
for c in t:
    if c not in s_set:
        flag = 1
        print("No")
        break

# 条件１
flag2 = 0
res_list = []
i = 0
j = -1
if flag == 0:
    for c in s[j + 1 :]:
        print(c)
        print(s[j + 1 :])
        for k in t:  # 空港コードにマッチするか
            if c == k:
                j = i
                print(i)
                res_list.append(k)
                break
        if len(res_list) == 2:
            res = "".join(res_list)
            res += "X"
            if res == t:
                flag2 = 1
                print("Yes")
                break
        elif len(res_list) == 3:
            flag2 = 1
            print("Yes")
            break
        i += 1

if flag2 == 0 and flag == 0:
    print("No")
