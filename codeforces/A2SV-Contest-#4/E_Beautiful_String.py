n, k = map(int, input().split())
string = input()
left = 0
right = 1

a = 0
b = 0

ans = 0

if string[0] == 'a':
    a += 1
else:
    b += 1

while right < n:
    if string[right] == "a":
        a += 1
    else:
        b += 1

    while min(a, b) > k:
        if string[left] == "a":
            a -= 1
        else:
            b -= 1

        left += 1

    ans = max(ans, a + b)
    right += 1

ans = max(ans, a + b)
print(ans)