from math import ceil
n, m, a = map(int, input().split())
b = ceil(n/a)
c = ceil(m/a)
print(b*c)
