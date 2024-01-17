n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
i = 0
ans = 0
while i < m:
    if a[i] < 0:
        ans += a[i]
    else:
        break
    i += 1
print(-ans)