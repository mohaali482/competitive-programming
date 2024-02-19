from math import comb
from collections import defaultdict

for _ in range(int(input())):
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    ax = a.copy()
    ay = a.copy()
    for i in range(n):
        ax[i] %= x
        ay[i] %= y
    
    _dict = defaultdict(int)
    for i in range(n):
        tup = (ax[i], ay[i])
        nee = ((x-ax[i])%x, (y - ay[i])%y)
        _dict[tuple(sorted([tup, nee]))] += 1
    ans = 0
    for i in _dict.values():
        ans += (i*i-1)//2
    
    print(ans)
