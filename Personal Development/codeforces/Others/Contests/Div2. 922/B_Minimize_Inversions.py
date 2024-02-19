for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [(a[i], i) for i in range(n)]
    c.sort()
    ans1 = [0] * n
    ans2 = [0] * n
    for i in range(n):
        ans1[i] = c[i][0]
        ans2[i] = b[c[i][1]]
    print(*ans1)
    print(*ans2)