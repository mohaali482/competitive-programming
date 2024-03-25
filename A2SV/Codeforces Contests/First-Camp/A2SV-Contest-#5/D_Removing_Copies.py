from math import ceil

from sys import stdin
from collections import Counter


input = lambda : stdin.readline().strip()

n, k = map(int, input().split())
a = list(map(int, input().split()))

ca = Counter(a)
print(ca.most_common())


def validate(freq):
    arr = 0
    for i in ca:
        if arr+ca[i]//freq<k:
            arr+=ca[i]//freq

    return (arr, len(a)-(arr*freq))

left = 1
right = ca.most_common(1)[0][1]
ans = 1
remaining_ans = float("inf")

while left <= right:
    mid = left + (right-left)//2
    size, remaining_size = validate(mid)
    print(mid, size, remaining_size)

    if size >= k:
        if remaining_size < remaining_ans:
            ans = mid
            remaining_ans = remaining_size
        left = mid+1
    else:
        right = mid-1
print("Found", ans)

# arr = []
# for i in ca:
#     if ca[i] >= ans:
#         arr.extend([i] * (ca[i]//ans))
# print(*arr) 