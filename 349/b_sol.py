"""
アルファベットは26種類
長さ26の配列を用意、要素をi番目の文字が文字列中に現れる回数とする

"""

s = input()
cnt = [0] * 26

# ord関数でunicodeの整数値を返す
for c in s:
    cnt[ord(c) - ord("a")] += 1

# cnt2 : 文字列にちょうどi回現れる文字の種類数
cnt2 = [0] * 101
for c in cnt:
    if c > 0:
        cnt2[c] += 1

print("Yes" if all(c in (0, 2) for c in cnt2) else "No")
