import sys
from functools import cache

sys.setrecursionlimit(10 ** 6)

t = int(input())


for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    i = 0
    j = 1
    def findMaxSum(start, end, arr):
        while start < end and arr[start] < 0:
            start += 1
        answers = []
        _sum = 0
        _max = -1
        for k in range(start, end+1):
            _sum += arr[k]
            _max = max(_sum, _max)
            if arr[k] < 0:
                answers.append(_sum-arr[k])
        
        print(start, end, answers)

        return max(_max, max(answers))

    _sum = arr[0]
    ans = _sum
    while j < n:
        if arr[j] % 2 == arr[j - 1] % 2:
            ans = max(ans, findMaxSum(i, j, arr))
            i = j
        j += 1
    # ans = max(ans, findMaxSum(i, j-1, arr))
    print(ans)
