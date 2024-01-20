from collections import Counter

def sol():
    input()
    inp = ''.join(input().split())
    counter = Counter(inp)
    odd = 0
    for v in counter.values():
        if v % 2 != 0:
            if odd > 0:
                return "No"
            else:
                odd += 1
    
    return "Yes"

t = int(input())
for _ in range(t):
    print(sol())