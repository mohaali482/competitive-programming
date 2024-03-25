import sys, threading

input = lambda: sys.stdin.readline().strip()


s = input()
stack = []
for i in s:
    if stack and stack[-1] == i:
        stack.pop()
    else:
        stack.append(i)

print(''.join(stack))