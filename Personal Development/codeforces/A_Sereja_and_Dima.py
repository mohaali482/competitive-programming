n = int(input())
a = list(map(int, input().split()))
i = 0
j = n - 1
s, d = 0, 0
t = 0
while i <= j:
    if a[i] > a[j]:
        if t == 0:
            s += a[i]
            t = 1
        else:
            d += a[i]
            t = 0
        i += 1
    else:
        if t == 0:
            s += a[j]
            t = 1
        else:
            d += a[j]
            t = 0
        j -= 1

print(s, d)