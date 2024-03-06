class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low = 0
        high = len(letters)-1
        ans = 0
        while low <= high:
            mid = low + (high-low)//2
            if letters[mid] > target:
                ans = mid
                high = mid-1
            else:
                low = mid+1
        
        return letters[ans]