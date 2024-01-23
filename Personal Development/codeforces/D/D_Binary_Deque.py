def solution():
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    _sum = sum(a)
    if _sum < s:
        print(-1)
        return
    
    if _sum == s:
        print(0)
        return
    
    window = 0
    ans = n
    i = 0
    j = 0
    while j < n:
        window += a[j]
        
        while window > s:
            window -= a[i]
            i += 1
        
        ans = min(ans, n - (j - i + 1))
        j += 1
    
    print(ans)




t = int(input())
for _ in range(t):
    solution()