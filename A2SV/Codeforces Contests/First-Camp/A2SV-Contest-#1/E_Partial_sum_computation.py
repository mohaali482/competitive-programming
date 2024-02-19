def solution():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    if arr[0] != 1:
        return "NO"
    
    s = 1
    for i in range(1, n):
        if s >= arr[i]:
            s+=arr[i]
        else:
            return "NO"
    
    return "YES"
for tc in range(int(input())):
    print(solution())
            
