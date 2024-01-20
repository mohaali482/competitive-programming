class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        j = 0
        while j < len(strs[0]):
            m = strs[0][j]
            for i in range(len(strs)):
                if j >= len(strs[i]) or strs[i][j] != m:
                    return ans
            
            ans += m
            j += 1
        
        return ans