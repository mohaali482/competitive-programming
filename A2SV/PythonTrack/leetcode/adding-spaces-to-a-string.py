class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ""
        i = 0
        j = 0
        while i < len(spaces) and j < len(s):
            if j < spaces[i]:
                ans += s[j]
            else:
                ans += " " + s[j]
                i += 1
            j += 1
        
        ans += s[j:]
        return ans