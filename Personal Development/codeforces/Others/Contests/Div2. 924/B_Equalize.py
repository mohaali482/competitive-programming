from sys import stdin
input = stdin.readline

def solution():
    n = int(input())
    a = list(set(map(int, input().split())))
    a.sort()
    ans = 1
    left = 0
    right = 1
    while right < len(a):
        while a[right] - a[left] >= n:
            left += 1
        
        ans = max(ans, right - left + 1)
    
        right += 1
    
    return ans

for _ in range(int(input())):
    print(solution())