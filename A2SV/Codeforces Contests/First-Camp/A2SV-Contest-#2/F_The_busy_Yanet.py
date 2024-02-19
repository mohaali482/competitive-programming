from collections import deque
from sys import stdin

input = stdin.readline

def sol():
    input()
    a = list(map(int, input().split()))
    item = min(a)
    queue = deque()
    count = 0
    for i in a:
        while queue and i < queue[-1]:
            queue.pop()
        
        queue.append(i)
        if queue[0] != item:
            count += 1

    if len(a) - count == len(queue):
        return count
    return -1

for _ in range(int(input())):
    print(sol())