from sys import stdin
input = lambda : stdin.readline().strip()

def solve():
    n, x = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()
    for i in range(n):
        if nums[i] + x > nums[i+n]:
            return "NO"
    
    return "YES"

for _ in range(int(input())):
    print(solve())