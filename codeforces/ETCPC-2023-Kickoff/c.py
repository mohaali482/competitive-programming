from math import comb
from collections import defaultdict
n = int(input())
m = list(map(int, input().split()))
freq = defaultdict(int)
for i, v in enumerate(m):
    freq[v-(i+1)] += 1

ans = 0
for i in freq.values():
    if i > 1:
        ans += comb(i, 2)

print(ans*2)