###############################################################
#                                                             #
#                   Author: Mohammed Ali Fenta                #
#                   Date  : 2024-03-23 09:44:26               #
#                                                             #
###############################################################
from sys import stdin
from string import ascii_lowercase as asc
from itertools import accumulate

indexes = {asc[i]: (i+1) for i in range(len(asc))}

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
    n, m = lint()
    s = strp()
    w = strp()
    s_in = [indexes[i] for i in s]
    if m > n:
        print("NO")
        return

    tot = 0
    for i in w:
        tot += indexes[i]
    pre_s = [0] + list(accumulate(s_in))
    
    left = 0
    right = len(w)
    while right < len(pre_s):
        if pre_s[right] - pre_s[left] == tot:
            print("YES")
            return
        left += 1
        right += 1
    
    print("NO")





for _ in range(int(input())):
    solve()