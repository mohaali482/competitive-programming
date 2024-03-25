class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def play1wins(start, end, p1Score, p2Score, p1=True):
            if start > end:
                return p1Score >= p2Score
            
            if p1:
                return play1wins(start+1, end, p1Score+nums[start], p2Score, not p1) or \
                play1wins(start, end-1, p1Score+nums[end], p2Score, not p1)
            else:
                return play1wins(start+1, end, p1Score, p2Score+nums[start], not p1) and \
                play1wins(start, end-1, p1Score, p2Score+nums[end], not p1)
            
        return play1wins(0, len(nums)-1, 0, 0)
