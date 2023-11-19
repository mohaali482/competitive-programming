def solution():
    n = int(input())
    a = list(map(int, input().split()))
    b = [i for i in a]
    b.sort()
    i = 0
    while i < n:
        ae = a[i] % 2 == 0
        be = b[i] % 2 == 0
        if ae != be:
            print("NO")
            return
        i += 1
    
    print("YES")

t = int(input())
for _ in range(t):
    solution()