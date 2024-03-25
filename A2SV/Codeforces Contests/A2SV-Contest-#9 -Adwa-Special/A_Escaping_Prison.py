###############################################################
#                                                             #
#                   Author: Mohammed Ali Fenta                #
#                   Date  : 2024-03-23 09:16:14               #
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
    n, h = lint()
    tot = 0
    for _ in range(n):
        tot += max(lint())
    
    if tot >= h:
        print("YES")
    else:
        print("NO")

for _ in range(int(input())):
    solve()