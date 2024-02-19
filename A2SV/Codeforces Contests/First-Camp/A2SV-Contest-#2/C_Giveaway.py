from sys import stdin

input = stdin.readline

n, q = map(int, input().split())
p = list(map(int, input().split()))
p.sort(reverse=True)
d = p.copy()
for i in range(1, n):
    p[i] = p[i] + p[i-1]
for i in range(n-2, -1, -1):
    d[i] = d[i] + d[i+1]
for _ in range(q):
    x, y = map(int, input().split())
    if x == y:
        print(p[x-1])
    else:
        print(p[x-1] - p[x-y-1])