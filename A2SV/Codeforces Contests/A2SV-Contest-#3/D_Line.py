def solution():
    n = int(input())
    s = list(input())
    _sum = 0
    for i in range(n):
        if s[i] == "R":
            _sum += n-i-1
        else:
            _sum += i
    ans = []
    t = True
    i = 0
    j = n - 1
    while i <= j:
        if t:
            if s[i] == "L":
                _sum -= i
                _sum += n-i-1
                ans.append(_sum)
            i+=1
        else:
            if s[j] == "R":
                _sum -= n-j-1
                _sum += j
                ans.append(_sum)
            j-=1 
        t = not t
    m = n - len(ans)
    for i in range(m):
        ans.append(_sum)
    print(*ans)

t = int(input())
for _ in range(t):
    solution()
