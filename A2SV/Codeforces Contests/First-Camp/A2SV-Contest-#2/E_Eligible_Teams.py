from sys import stdin

input = stdin.readline

for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    count = 0
    _min = 0
    i = n-1
    while i > -1:
        count += 1
        _min = a[i]
        if _min * count >= x:
            ans += 1
            count = 0
            _min = 0
        
        i -= 1
    print(ans)
