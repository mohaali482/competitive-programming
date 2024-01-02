n = int(input())
nums = list(map(int, input().split()))

def solution(n):
    i = 0
    while n > 0:
        n -= nums[i]
        if n <= 0:
            return i + 1
        i += 1
        if i == len(nums):
            i = 0
    
    return i+1

print(solution(n))
