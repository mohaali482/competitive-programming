class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        maximum = -1
        while i < j:
            current = min(height[i], height[j]) * (j - i)
            if (current > maximum):
                maximum = current
            if (height[i] >= height[j]):
                j -= 1
            elif height[j] > height[i]:
                i += 1
        return maximum
