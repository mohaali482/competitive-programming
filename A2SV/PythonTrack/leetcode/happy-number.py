class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set()
        while n != 1 and n not in nums:
            _sum = 0
            for i in str(n):
                _sum += int(i)**2
            
            nums.add(n)
            n = _sum
        
        if n == 1:
            return True
        
        return False