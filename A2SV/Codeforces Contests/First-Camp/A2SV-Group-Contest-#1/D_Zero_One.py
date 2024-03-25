

import sys

input = lambda: sys.stdin.readline().strip()

def solution():
    n = int(input())
    s = input()
    p1 = 0
    p2 = n-1
    while p1<= p2:
        if (s[p1] == '0' and s[p2] == '1') or (s[p1] == '1' and s[p2] == '0'):
            p1+=1
            p2-=1
        else:
            return (p2-p1) +1
    return 0
        


for _ in range(int(input())):
    print(solution())

