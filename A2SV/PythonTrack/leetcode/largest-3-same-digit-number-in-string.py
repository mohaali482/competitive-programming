class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = ""
        for i in range(10):
            if str(i)*3 in num:
                ans = str(i)*3
        
        return ans