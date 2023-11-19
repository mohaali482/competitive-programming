def solution():
    n = int(input())
    a = list(map(int, input().split()))
    j = 0
    found = False
    while j < n-1:
        if a[j] == a[j+1]:
            j += 1
            continue
        if a[j] < a[j+1] and not found:
            found = True
        elif a[j] > a[j+1] and found:
            print("NO")
            return
        j += 1
    
    print("YES")
        


t = int(input())
for _ in range(t):
    solution()