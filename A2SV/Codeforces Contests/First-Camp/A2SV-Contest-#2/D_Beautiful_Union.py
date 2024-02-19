from collections import defaultdict
from sys import stdin

input = stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_count = defaultdict(int)
    current = a[0]
    count = 1
    for i in range(1, n):
        if a[i] == current:
            count += 1
        else:
            a_count[current] = max(count, a_count[current])
            current = a[i]
            count = 1

    a_count[current] = max(count, a_count[current])

    b_count = defaultdict(int)
    current = b[0]
    count = 1
    for i in range(1, n):
        if b[i] == current:
            count += 1
        else:
            b_count[current] = max(count, b_count[current])
            current = b[i]
            count = 1
    b_count[current] = max(count, b_count[current])


    ans = 0
    for i in set(a_count.keys()).union(set(b_count.keys())):
        ans = max(a_count[i] + b_count[i], ans)
    
    print(ans)
                
            
