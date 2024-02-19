from math import ceil
from sys import stdin

input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    current = a[0]
    for i in range(1, n):
        if current < a[i]:
            current = a[i]
        else:
            m = ceil((current+1)/a[i])
            current = m * a[i]
    
    print(current)
