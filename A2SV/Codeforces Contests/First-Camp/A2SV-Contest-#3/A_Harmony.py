from collections import Counter
import sys, threading

input = lambda: sys.stdin.readline().strip()

def solution():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    input()
    a.sort()
    b.sort(reverse=True)
    for i in range(n):
        if a[i] + b[i] > x:
            return 'No'
    return "Yes"

for _ in range(int(input())):
    print(solution())