###############################################################
#                                                             #
#                   Author: Mohammed Ali Fenta                #
#                   Date  : 2024-03-16 10:13:55               #
#                                                             #
###############################################################
from sys import stdin
from itertools import accumulate
from bisect import bisect_left


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
    n = intp()
    a = lint()
    m = intp()
    q = lint()
    prefix = list(accumulate(a))
    for _ in range(m):
        pos = bisect_left(prefix, q[_])
        print(pos+1)    
    

solve()