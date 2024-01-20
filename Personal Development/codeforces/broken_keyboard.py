from collections import defaultdict
def solution():
    a = input()
    j = 0
    counter = defaultdict(int)
    broken = set()
    while j < len(a):
        counter[a[j]] += 1
        while j+1 < len(a) and a[j+1] == a[j]:
            counter[a[j]] += 1
            j += 1
        
        if counter[a[j]] % 2 != 0:
            broken.add(a[j])
        
        j += 1

    broken = list(broken)
    broken.sort()
    print(''.join(broken))

    




t = int(input())
for _ in range(t):
    solution()