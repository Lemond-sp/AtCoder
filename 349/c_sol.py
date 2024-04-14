"""
Tの最後の文字がXでない場合、TがSの部分列だとよい
Tの最後の文字がXである場合、Tの最初の２文字がSの部分列だとよい
判定は貪欲法でよい
"""


def check(S, T):
    # 読み込み位置をiで保持する
    i = 0
    for t in T:
        while i < len(S) and S[i] != t:
            i += 1
        if i == len(S):
            return False
        i += 1
    return True


S = input().upper()
T = input()
print("Yes" if check(S, T if T[-1] != "X" else T[:-1]) else "No")
