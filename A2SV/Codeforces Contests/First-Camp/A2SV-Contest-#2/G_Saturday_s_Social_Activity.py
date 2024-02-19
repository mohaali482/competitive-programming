from collections import deque
from sys import stdin

input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ab = list(zip(a, b))
    ab.sort(key=lambda x: x[0] + x[1], reverse=True)
    totalA = 0
    totalB = 0
    turn = True
    for i in range(n):
        if turn:
            totalA += ab[i][0]-1
        else:
            totalB += ab[i][1]-1
        
        turn = not turn
    
    print(totalA-totalB)