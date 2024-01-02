class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i < j:
            _sum = numbers[i] + numbers[j]
            if _sum == target:
                return i+1, j+1
            elif _sum < target:
                i += 1
            else:
                j -= 1
        return i+1, j+1