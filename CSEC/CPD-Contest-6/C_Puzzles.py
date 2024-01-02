n, m = map(int, input().split())
f = list(map(int, input().split()))
f.sort()
ans = f[-1]
i = 0
j = n - 1
while j < m:
    ans = min(ans, f[j] - f[i])
    i += 1
    j += 1
print(ans)