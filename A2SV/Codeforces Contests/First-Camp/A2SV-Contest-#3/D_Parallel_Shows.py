from collections import Counter
import sys, threading

input = lambda: sys.stdin.readline().strip()
arr = []
for _ in range(int(input())):
    l, r = map(int, input().split())
    arr.append((l, r))
arr.sort(key = lambda x: -x[1])
def solution():
    first = [float("inf"), float("inf")]
    second = [float("inf"), float("inf")]
    for i in range(len(arr)):
        if first[0] > arr[i][1]:
            first = arr[i] 
        elif second[0] > arr[i][1]:
            second = arr[i]
        else:
            return "NO"
    return "YES"
print(solution())
            