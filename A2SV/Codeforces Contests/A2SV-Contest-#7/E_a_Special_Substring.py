from collections import Counter
for _ in range(int(input())):
    n = int(input())
    s = input()
    a = []
    for i in range(len(s)):
        if s[i] == 'a':
            a.append(i)
    
    ans = float("inf")
    left = 0
    right = 1
    while right < len(a):
        while left < right and (((a[right] - a[left])+1)-((right-left)+1)) <= ((right-left)+1):
            ans = min(ans, (a[right] - a[left])+1)
            left += 1
        right += 1
        
    
    if ans == float("inf"):
        print(-1)
    
    else:
        print(ans)