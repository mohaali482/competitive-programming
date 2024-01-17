from collections import Counter
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ca = Counter(a)
    cv = {}
    ccv = sorted(ca.values(), reverse=True)
    for i in range(len(ccv)):
        cv[ccv[i]] = i+1
    min_ = n
    for i in cv:
        min_ = min(min_, n-(i*cv[i]))
    
    print(min_)