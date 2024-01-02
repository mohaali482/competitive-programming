n = int(input())
h = list(map(int, input().split()))
ans = h[0]
energy = 0
for i in range(n-1):
    if h[i] + energy < h[i+1]:
        ans += h[i+1] - (h[i] + energy)
        energy = 0
    else:
        energy += h[i] - h[i+1]

print(ans)