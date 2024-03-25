from collections import deque
import sys, threading

input = lambda: sys.stdin.readline().strip()
n, q = map(int, input().split())
a = deque(map(int, input().split()))
d = {}
idx = a.index(max(a))
for i in range(idx+1):
    # print(i+1, a)
    d[i+1] = (a[0], a[1])
    x, y = a.popleft(), a.popleft()
    x, y = min(x, y), max(x, y)
    a.appendleft(y)
    a.append(x)
aa = [0] * (len(a)-1)
j = 0
_max = a.popleft()
while a:
    aa[j] = a.popleft()
    j += 1

# print(aa)

for _ in range(q):
    m = int(input())
    if m in d:
        print(*d[m])
    else:
        m -= idx+1
        m -= 1
        # m += len(aa)
        m %= len(aa)
        print(_max, aa[m])