n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = []
i = 0
j = n - 1
t = True
while i <= j:
    if t:
        ans.append(a[i])
        i += 1
    else:
        ans.append(a[j])
        j -= 1
    
    t = not t

print(*ans)