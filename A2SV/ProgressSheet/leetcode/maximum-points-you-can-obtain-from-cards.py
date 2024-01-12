class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total_sum = sum(cardPoints)

        if k == len(cardPoints):
            return total_sum
        
        window = sum(cardPoints[:-(k+1)])
        left = 0
        right = len(cardPoints) - (k+1)
        ans = float("-inf")
        while right < len(cardPoints):
            window += cardPoints[right]

            ans = max(ans, total_sum - window)

            window -= cardPoints[left]

            right += 1
            left += 1
        
        return ans