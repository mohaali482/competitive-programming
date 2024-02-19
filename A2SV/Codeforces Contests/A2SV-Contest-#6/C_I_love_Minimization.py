t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    b.sort()
    i = 0
    a = [0] * n
    k = 0
    i = 0
    m = n-1
    while i < len(b):
        a[k] = b[i]
        i += m
        m -= 1
        k += 1
    a[k] = b[-1]
    print(*a)
