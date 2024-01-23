from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    s = Counter(input())
    ans = 0
    for k, v in s.items():
        if (ord(k) - ord('A')) + 1 <= v:
            ans += 1
    
    print(ans)

