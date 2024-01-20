t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    _sum = 0
    for i in arr:
        _sum += abs(i)
    
    ans = 0
    left = 0
    right = 0
    neg = 0
    if arr[right] < 0:
        right += 1
        neg += 1

    while right < n:
        if arr[right] > 0 and neg > 0:
            ans += 1
            left = right
            neg = 0
        elif arr[right] < 0:
            neg += 1
    
        right += 1
    
    if neg:
        ans += 1
    print(_sum, ans)