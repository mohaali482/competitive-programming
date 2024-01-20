t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    st = input()
    left = 0
    right = k-1
    white = 0
    ans = float("inf")
    for i in range(k-1):
        if st[i] == 'W':
            white += 1
    while right < n:
        if st[right] == 'W':
            white += 1
        
        ans = min(ans, white)
        if st[left] == 'W':
            white -= 1
        
        left += 1
        right += 1
    
    print(ans)
        
