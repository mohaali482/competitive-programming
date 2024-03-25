

import sys

input = lambda: sys.stdin.readline().strip()

for _ in range(int(input())):
    n = int(input())
    ans = n
    while n > 1:
        n //= 2
        ans += n
    
    print(ans)