from collections import defaultdict, Counter
input()
a = list(map(int, input().split()))

c = Counter(a)
freq = defaultdict(list)
for i in c.keys():
    for j in range(1, c[i]+1):
        freq[j].append(i)

ans = 0
for v in freq.values():
    v.sort()
    if len(v) >= 2:
        c = 0
        for i in range(len(v)-1):
            if v[i] < v[i+1]:
                c += 1
        ans += c
print(freq)
print(ans)