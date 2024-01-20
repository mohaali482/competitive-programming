l, r, x, y, k = map(int, input().split())

f = False
for i in range(x, y+1):
    _mul = k * i
    if l <= _mul <= r:
        f = True
        break

if f:
    print("YES")
else:
    print("NO")