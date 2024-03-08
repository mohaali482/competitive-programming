class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        positions = {intervals[i][0]: i for i in range(len(intervals))}
        arr = list(sorted(positions.keys()))
        ans = [-1] * len(intervals)
        for start, end in intervals:
            index = bisect_left(arr, end)
            if index == len(arr):
                ans[positions[start]] = -1
            else:
                ans[positions[start]] = positions[arr[index]]
        
        return ans