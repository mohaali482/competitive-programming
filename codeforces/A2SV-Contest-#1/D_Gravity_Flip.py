n = int(input())
a = [int(i) for i in input().split()]
def isSorted(a):
    for i in range(n-1):
        if a[i] > a[i+1]:
            return False
    
    return True

while not isSorted(a):
    for i in range(n-1, 0, -1):
        if a[i] < a[i-1]:
            diff = a[i-1] - a[i]
            a[i] += diff
            a[i-1] -= diff

print(*a)

# This approach works too.
# print(*a.sort())