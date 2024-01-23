def solution():
    n, m = input().split()
    s = input()
    if m == "g":
        print(0)
        return
    ans = 0
    i = -1
    j = 0
    min_g = len(s)
    while j < len(s):
        if s[j] == m and i == -1:
            i = j
        elif s[j] == "g":
            if min_g == len(s):
                min_g = j
            if i != -1:
                ans = max(ans, j-i)
                i = -1
        j += 1

    if i != -1:
        ans = max(ans, (len(s) - i) + min_g)
    
    print(ans)



t = int(input())
for _ in range(t):
    solution()