n = int(input())

bin_str = format(n, "b")
ans = 0

if bin_str[-1] == "1":
    ans = 0
else:
    for i in range(len(bin_str) - 1, -1, -1):
        if bin_str[i] == "0":
            ans += 1
        else:
            break

print(ans)
