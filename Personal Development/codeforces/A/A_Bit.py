n = int(input())
ans = 0
for i in range(n):
    a = input()
    if "+" in a:
        ans += 1
    else:
        ans -= 1

print(ans)