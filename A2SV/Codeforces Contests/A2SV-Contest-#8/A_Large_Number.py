###############################################################
#                                                             #
#                   Author: Mohammed Ali Fenta                #
#                   Date  : 2024-03-16 10:02:15               #
#                                                             #
###############################################################
from sys import stdin


input = lambda : stdin.readline().strip()

def lint():
    return list(map(int, input().split()))

def intp():
    return int(input())
    
def strp():
    return input()

def lstr():
    return list(input().split())

def solve():
    n, d = lint()
    d = str(d)
    s = strp()
    ans = n
    for i in range(n):
        if s[i] < d:
            ans = i
            break
    print(s[:ans]+d+s[ans:])


for _ in range(int(input())):
    solve()