n, k = map(int, input().split())
mx = float("-inf")
for _ in range(n):
    f, t = map(int, input().split())
    if t > k:
        c = f - (t - k)
    else:
        c = f
    mx = max(mx, c)

print(mx)
    