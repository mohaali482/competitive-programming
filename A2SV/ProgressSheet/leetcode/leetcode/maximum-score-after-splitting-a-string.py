class Solution:
    def maxScore(self, s: str) -> int:
        left = []
        right = []
        totLeft = 0
        totRight = 0
        for i in range(len(s)):
            if s[i] == "0":
                totLeft += 1
            else:
                totRight += 1
            
            left.append(totLeft)
            right.append(totRight)
        
        ans = float("-inf")
        for i in range(len(s)-1):
            toRight = right[-1] - right[i]
            toLeft = left[i]

            ans = max(ans, toRight + toLeft)
        
        return ans