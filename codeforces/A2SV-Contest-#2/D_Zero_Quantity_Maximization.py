from math import gcd
from collections import defaultdict

def sig(a):
    if a < 0:
        return -1
    return 1

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = defaultdict(int)

both = 0

for i in range(n):
    if b[i] == 0 and a[i] == 0:
        both += 1
    if a[i] != 0:
        g = gcd(a[i], b[i])
        bb = b[i] // g
        aa = a[i] // g
        bb *= sig(aa)
        if aa < 0:
            aa *= -1
        key = f"{bb}/{aa}"
        c[key] += 1

if len(c) > 0:
    m = max(c.values())
else:
    m = 0
print(m + both)
