def sol():
    n = int(input())
    arr = list(map(int, input().split()))
    found = False
    ptr = 0
    while ptr < n-1:
        if arr[ptr] == arr[ptr+1]:
            ptr += 1
            continue
        if arr[ptr] < arr[ptr+1] and not found:
            found = True
        elif arr[ptr] > arr[ptr+1] and found:
            return "NO"
        ptr += 1
    
    return "YES"

t = int(input())
for _ in range(t):
    print(sol())