from math import gcd, ceil

t = int(input())
for _ in range(t):
    x, n = map(int, input().split())
    m = x%n
    if m == 0:
        print(x//n)
    else:
        a = ((x-m) // n)
        b = (m) + a
        print(a, b)
        # print(gcd(a, b))

        # print(gcd(int(((x-m)/n)-m), ceil(x/n)))