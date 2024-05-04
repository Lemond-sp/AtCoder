S = input()
T = input()
res = []
j = 0  # 一致した文字列の番地

for i in range(len(T)):
    if S[j] == T[i]:
        res.append(i + 1)
        j += 1

print(*res)
