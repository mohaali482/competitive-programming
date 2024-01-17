n, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
def solution():
    if k == 0:
        if a[0] == 1:
            return -1
        else:
            return a[0] - 1 

    if k == n:
        return a[-1]
    elif k > n:
        return -1

    if a[k-1] == a[k]:
        return -1

    return a[k-1]

print(solution())