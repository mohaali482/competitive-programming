from collections import Counter
k = int(input())
s = input()
cs = Counter(s)
def solution():
    for i in cs:
        if cs[i] % k != 0:
            return "-1"
    
    ans = [i*(cs[i]//k) for i in cs]
    ans = ''.join(ans) * k

    return ans

print(solution())