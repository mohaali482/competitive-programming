# from sys import stdin

# input = stdin.readline

# def solution():
#     n = int(input())
#     a = list(map(int, input().split()))

#     prefix = [0] * (n+1)
#     tot = 0
#     pos = 1

#     for i in range(n):
#         tot += a[i]
#         prefix[pos] = tot
#         pos += 1


#     low = 0
#     for i in range(1, n):
#         wanted = prefix[i] - tot
        
#         if wanted >= low:
#             return "NO"

#         low = min(low, prefix[i])
    
        
#     low = prefix[1]
#     for i in range(2, n+1):
#         wanted = prefix[i] - tot
        
#         if wanted >= low:
#             return "NO"

#         low = min(low, prefix[i])
    
#     return "YES"

# for _ in range(int(input())):
#     print(solution())



from functools import cache
from sys import stdin
 
input = stdin.readline
 
class Solution:
    def solve(self):
        self.n = int(input())
        self.a = list(map(int, input().split()))
        self.sum = sum(self.a)
        
        @cache
        def find(i):
            if i == self.n - 2:
                return self.a[i]
            
            return max(self.a[i], self.a[i] + find(i+1))
        
        @cache
        def find2(i):
            if i == self.n - 1:
                return self.a[i]
            
            return max(self.a[i], self.a[i] + find2(i+1))
 
        
        if self.sum <= find(0) or self.sum <= find2(1):
            return "NO"
        else:
            return "YES"
 
    
 
for _ in range(int(input())):
    print(Solution().solve())