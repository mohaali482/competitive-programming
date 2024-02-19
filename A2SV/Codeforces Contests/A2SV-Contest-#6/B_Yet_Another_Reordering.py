n = int(input())
a = list(map(int, input().split()))
a.sort()
i = 0
j = 0
while j < n:
    if a[j] > a[i]:
        break
    j += 1
ans = 0
while j < n:
    if a[i] < a[j]:
        ans += 1
        i += 1
        j += 1
    elif a[j] == a[i]:
        j += 1
print(ans)