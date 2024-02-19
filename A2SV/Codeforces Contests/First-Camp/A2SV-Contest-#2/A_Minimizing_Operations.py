from collections import Counter
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ca = Counter(a)
    ca_keys = sorted(list(ca.keys()))
    ans = 0
    for i in range(len(ca_keys)-1):
        ans += (ca_keys[i+1]) - ca_keys[i]
    
    print(ans)