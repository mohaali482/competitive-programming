from collections import Counter

n = int(input())
l = list(map(int, input().split()))
d = Counter(l)

print(max(d.values()), len(d))