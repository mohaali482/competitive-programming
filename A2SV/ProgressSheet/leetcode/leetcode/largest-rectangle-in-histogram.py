class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = []
        for index, height in enumerate(heights):
            min_index = index
            while stack and stack[-1][1] >= height:
                ans = max(ans, (index - stack[-1][0]) * stack[-1][1])
                min_index = min(index, stack[-1][0])
                stack.pop()
            stack.append((min_index, height))
        index = len(heights)
        while stack:
            ans = max(ans, (len(heights) - stack[-1][0]) * stack[-1][1])
            stack.pop()
        return ans