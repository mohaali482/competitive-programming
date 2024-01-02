n, c = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(n-1):
    ans = max(a[i]-a[i+1]-c, ans)
print(ans)