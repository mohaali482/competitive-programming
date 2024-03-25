import sys

input = lambda: sys.stdin.readline().strip()

def solution():
    n = int(input())
    a = list(map(int, input().split()))
    stack = []
    for i in range(n-1, -1, -1):
        if len(stack) > 1 and a[i] < stack[-1][1]:
            print("YES")
            print(i+1, stack[-1][0]+1, stack[-2][0]+1)
            return
        while stack and stack[-1][1] > a[i]:
            stack.pop()
        stack.append([i, a[i]])
    
    print("NO")

for _ in range(int(input())):
    solution()