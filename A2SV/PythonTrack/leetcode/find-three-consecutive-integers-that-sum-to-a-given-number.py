class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num == 0:
            return [-1, 0, 1]
        left = 0
        right = num
        while left < right:
            mid = (left + right) // 2
            _sum = mid*3 + 3
            if _sum == num:
                return [mid, mid+1, mid+2]
            
            if _sum > num:
                right = mid
            else:
                left = mid + 1
        
        mid = (left + right) // 2
        _sum = mid*3 + 3
        if _sum == num:
            return [mid, mid+1, mid+2]
        
        return []