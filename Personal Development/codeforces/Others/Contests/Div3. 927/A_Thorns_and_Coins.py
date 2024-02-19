from functools import cache
from sys import stdin

input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = input()
    ans = 0
    index = n
    if "**" in a:
        index = a.index("**")
    
    for i in range(n):
        if i == index:
            break
        if a[i] == "@":
            ans += 1

    
    print(ans)