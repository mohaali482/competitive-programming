t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = [1]
    a.extend(list(map(int, input().split())))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    ai = 0
    aj = n
    bi = 0
    while ai < aj and bi < n:
        if a[ai] >= b[bi]:
            aj -= 1
            bi += 1
            continue
        ai += 1
        bi += 1

    print(n - aj)

    