from collections import Counter
def solution():
    n = int(input())
    h = list(map(int, input().split()))
    cc = Counter(h)
    m = []
    for k, v in cc.items():
        for vv in range(v):
            m.append(k-vv)
    
    m.sort()
    for i in range(n-1):
        if m[i] >= m[i+1] or m[i] < 0:
            return "NO"
    
    return "YES"

t = int(input())
for _ in range(t):
    print(solution())