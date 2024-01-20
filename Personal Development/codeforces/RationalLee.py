t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    w = list(map(int, input().split()))
    a.sort()
    w.sort()
    tot = 0
    i, j = 0, n-1
    m = 0

    while m < k and w[m] == 1:
        tot += a[j]*2
        j -= 1
        m += 1
    
    if m == k:
        print(tot)
        continue

    mm = k - 1
    while m <= mm:
        tot += a[j] + a[i]
        j -= 1
        i += w[mm] - 1
        mm -= 1
    print(tot)