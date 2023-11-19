t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    stack = []
    for i in range(n-1, -1, -1):
        if stack and a[i] > stack[-1]:
            ans += 1
            continue
        
        stack.append(a[i])

    print(ans)