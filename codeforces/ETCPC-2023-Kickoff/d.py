t = int(input())
for _ in range(t):
    a, b, k = map(int, input().split())
    p = b**k
    if p < a:
        print("Case 1")
    elif p == a:
        print("Case 2")
    else:
        print("Case 3")