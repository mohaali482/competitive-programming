n = int(input())
m = int(input())
a = [int(input()) for _ in range(n)]

a.sort(reverse=True)
_sum = 0
for i in range(n):
    _sum += a[i]
    if _sum >= m:
        break

print(i+1)
