a = list(map(int, input().split()))

if a[3] <= a[1] and a[3] >= a[2]:
    print("Yes")
elif a[3] >= a[1] and a[3] <= a[2]:
    print("Yes")
else:
    print("No")
