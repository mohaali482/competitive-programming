t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    odd = []
    even = []
    for i in a:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    
    print(*[*odd, *even])