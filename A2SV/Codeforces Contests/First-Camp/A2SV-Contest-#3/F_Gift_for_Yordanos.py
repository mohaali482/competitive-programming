import heapq
from collections import deque, Counter
import sys, threading

input = lambda: sys.stdin.readline().strip()
s = input()
t = []
u = []
arr = [0] * 26
for i in s:
    arr[ord(i)-97] += 1

for i in s:
    t.append(i)
    arr[ord(i)-97] -= 1
    while t and sum(arr[:ord(t[-1])-97]) == 0:
        u.append(t.pop())
while t:
    u.append(t.pop())
    

print("".join(u))
    
