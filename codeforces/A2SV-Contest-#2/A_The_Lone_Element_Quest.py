from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ca = Counter(a)
    for i in range(len(a)):
        if ca[a[i]] == 1:
            print(i+1)
            break