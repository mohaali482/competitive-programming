t = int(input())
tot = [0, 0, 0]
for _ in range(t):
    x, y, z = map(int, input().split())
    tot = [tot[0] + x, tot[1]+y, tot[2]+z]

if tot[0] == tot[1] == tot[2] == 0:
    print("YES")
else:
    print("NO")
