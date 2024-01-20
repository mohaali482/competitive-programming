def sig(n):
    if n > 0:
        return 1
    
    return -1

def solution():
    n = int(input())
    a = list(map(int, input().split()))
    j = 0
    c = sig(a[0])
    temp = a[0]
    _sum = 0
    while j < n-1:
        if sig(a[j+1]) == c:
            if temp < a[j+1]:
                temp = a[j+1]
        else:
            _sum += temp
            temp = a[j+1]
            c = sig(a[j+1])
        j += 1
    
    _sum += temp
    print(_sum)

t = int(input())
for _ in range(t):
    solution()