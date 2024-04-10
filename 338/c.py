n = int(input())
q = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

delta = 1e-6
if q[0] < max(a[0], b[0]) or q[1] < max(a[1], b[1]):
    print(0)
else:
    # 処理
    if min(q[0] // (a[0] + delta), q[1] // (a[1] + delta)) < min(
        q[0] // (b[0] + delta), q[1] // (b[1] + delta)
    ):
        print("b")

    else:
        print("a")

    # 片方の処理
