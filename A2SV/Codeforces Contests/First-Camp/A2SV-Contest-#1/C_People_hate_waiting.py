from sys import stdin
input = stdin.readline

n = int(input())
t = list(map(int, input().split()))
t.sort()
tot = t[0]
counter = 1
for i in range(1, n):
    if tot > t[i]:
        continue
    counter += 1
    tot += t[i]

print(counter)