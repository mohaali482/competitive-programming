from collections import Counter
n, k = map(int, input().split())
s = input()
d = Counter(s)

def solution():
    j = 0
    opened = set()
    while j < len(s):
        opened.add(s[j])
        if len(opened) > k:
            return False
        d[s[j]] -= 1
        if d[s[j]] == 0:
            opened.remove(s[j])
        
        j += 1
    
    return True

ans = solution()
if ans:
    print("NO")
else:
    print("YES")


        