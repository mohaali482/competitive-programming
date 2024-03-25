import sys

input = lambda: sys.stdin.readline().strip()

def solution():
    e = input()
    s = input()
    dest = 0
    left = 0
    right = 0
    for i in range(len(s)):
        if e[i] == '+':
            dest += 1
        else:
            dest -= 1
        if s[i] == '+':
            left+=1
            right+=1
        elif s[i] == '-':
            left-=1
            right-=1
        else:
            left-=1
            right+=1
    if dest == left == right:
        return 1
    elif left <= dest <= right:
        return 0.5
    return 0.00
print(solution())

