class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        ans = []
        m = 0
        temp = []
        intervals.sort()
        for i in range(len(intervals)*2):
            if len(temp) == 0:
                temp = intervals[0]
                intervals.pop(0)
                continue

            one, two = temp
            if intervals:
                th, fo = intervals[0]
                if two >= th and two <= fo:
                    temp = [min(one, th), max(fo, two)]
                    intervals.pop(0)
                elif fo <= two and th >= one:
                    temp = [min(one, th), max(fo, two)]
                    intervals.pop(0)
                else:
                    ans.append(temp)
                    temp = []
        if temp:
            ans.append(temp)
        return ans
