from collections import Counter

def solution():
    n = int(input())
    word = input()
    c = Counter(word)
    if len(c) == len(word):
        return 0 if len(word) % 2 == 0 else 1
    
    tot = 0
    most = c.most_common(1)[0][1]
    other = n - most
    if most - other < 0:
        return 0 if len(word) % 2 == 0 else 1
    
    return most - other


t = int(input())
for _ in range(t):
    print(solution())