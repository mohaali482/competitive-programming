###############################################################
#                                                             #
#                   Author: Mohammed Ali Fenta                #
#                   Date  : 2024-03-16 10:27:45               #
#                                                             #
###############################################################
from sys import stdin
from bisect import bisect_right


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
    s, b = lint()
    a = lint()
    nums = []
    for _ in range(b):
        nums.append(lint())
    nums.sort()
    
    defe = [nums[0][0]]
    gold = [nums[0][1]]
    for i in range(1, b):
        defe.append(nums[i][0])
        gold.append(gold[-1] + nums[i][1])

    ans = []
    for i in range(s):
        index = bisect_right(defe, a[i])
        if index == 0:
            ans.append(0)
        else:
            ans.append(gold[index-1])

    print(*ans)


solve()