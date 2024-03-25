from collections import Counter
import sys, threading

input = lambda: sys.stdin.readline().strip()
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    stack = []
    ans = 0
    for i in arr:
        while stack and stack[-1] > i:
            ans += 1
            stack.pop()
        stack.append(i)
    
    print(ans)