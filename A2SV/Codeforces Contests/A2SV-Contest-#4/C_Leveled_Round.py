t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort()
    
    left = 0
    right = 1
    ans = 1
    
    while right < n:
        if a[right] - a[right-1] > k:
            ans = max(ans, (right - left))
            left = right
        right += 1
    
    ans = max(ans, (right - left))
    
    print(n - ans)