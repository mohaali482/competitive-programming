###############################################################
#                                                             #
#                   Author: Mohammed Ali Fenta                #
#                   Date  : 2024-03-23 09:21:01               #
#                                                             #
###############################################################
from sys import stdin
from math import ceil


input = lambda : stdin.readline().strip()

def lint():
    return list(map(int, input().split()))

def intp():
    return int(input())
    
def strp():
    return input()

def lstr():
    return list(input().split())

MAX = 10**18

def solve():
    n, k = lint()
    d = lint()
    a = lint()

    def check(wagon):
        time = 0
        for i in range(n):
            time += a[i] * ceil(d[i]/wagon)
        
        return time
    
    left = 1
    right = MAX
    ans = float("inf")
    while left <= right:
        mid = left + (right-left)//2

        if check(mid) <= k:
            ans = min(ans, mid)
            right = mid-1
        else:
            left = mid+1
    if ans == float("inf"):
        print(-1)
    else:
        print(ans)


for _ in range(int(input())):
    solve()