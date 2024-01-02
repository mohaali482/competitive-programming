class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        ans = -1
        j = 0
        for i in range(len(processorTime)):
            if ans == -1:
                ans = processorTime[i] + tasks[j]
            else:
                ans = max(processorTime[i] + tasks[j], ans)
            j += 4
        
        return ans
