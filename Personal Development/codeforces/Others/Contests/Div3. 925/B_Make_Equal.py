def sol():
    n = int(input())
    a = list(map(int, input().split()))
    avg = sum(a) // n
    need = [0] * n
    for i in range(n):
        need[i] = a[i] - avg
    
    for i in range(1, n):
        need[i] = need[i] + need[i-1]
    for i in range(n):
        if need[i] < 0:
            return "NO"
    
    return "YES"

for _ in range(int(input())):
    print(sol())

