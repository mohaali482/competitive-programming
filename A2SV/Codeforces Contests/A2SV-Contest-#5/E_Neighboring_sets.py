from math import comb

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        print(0)
        continue
    a.sort()
    left = 0
    right = 0
    ans = 0
    while right < n-1:
        while a[right+1] - a[left] > 2 and right - left >= 1:
            ans += comb((right-left), 2)
            left += 1
            continue
        else:
            right += 1
    
    while a[right] - a[left] <= 2 and right - left >= 1:
        ans += comb((right-left), 2)
        left += 1
    print(ans)