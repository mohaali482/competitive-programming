n, m = map(int, input().split())
ans = n
while n >= m:
    ans += n // m
    extra = n // m
    n = n % m
    n += extra
print(ans)