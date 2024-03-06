class Solution:
    def hIndex(self, citations: List[int]) -> int:
        low = 0
        high = len(citations)-1
        best = 0
        while low <= high:
            mid = low + (high-low)//2
            if citations[mid] >= (len(citations)-mid):
                high = mid-1
                best = max(best, len(citations)-mid)
            else:
                low = mid+1
        
        return best