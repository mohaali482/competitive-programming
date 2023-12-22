class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        small = []
        big = []
        eq = []
        for num in nums:
            if num > pivot:
                big.append(num)
            elif num < pivot:
                small.append(num)
            else:
                eq.append(num)
        
        return [*small, *eq, *big]