from sys import stdin
input = stdin.readline
s = input()
arr = [0] * (len(s)+1)
tot = 0
pos = 1
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        tot += 1
    
    arr[pos] = tot
    pos += 1

m = int(input())
for _ in range(m):
    l, r = map(int, input().split())
    print(arr[r-1] - arr[l-1])