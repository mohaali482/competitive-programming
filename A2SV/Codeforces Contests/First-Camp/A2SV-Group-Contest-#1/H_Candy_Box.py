from collections import Counter, defaultdict

import sys

input = lambda: sys.stdin.readline().strip()

def solution():
    n = int(input())
    l = list(map(int, input().split()))
    x = Counter(l)
    a = list(x.values())
    a.sort(reverse=True)

    nn = len(a)
    ans = a[0]
    d = set([a[0]])
    for i in range(1,nn):
        while a[i] in d and a[i] > 0:
            a[i] -= 1
        ans += a[i]
        d.add(a[i])
    return ans


for _ in range(int(input())):
    print(solution())   
