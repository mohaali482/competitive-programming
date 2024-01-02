n = int(input())
ans = []
i = 1
while n:
    if i * 2 < n:
        ans.append(i)
        n -= i
        i += 1
    else:
        ans.append(n)
        break

print(len(ans))
print(*ans)