t = int(input())
for _ in range(t):
    a = [int(i) for i in input().split()]
    if a[0] + a[1] == a[2]:
        print("+")
    else:
        print("-")