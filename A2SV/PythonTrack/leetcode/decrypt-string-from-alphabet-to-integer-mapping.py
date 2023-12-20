class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = len(s) - 1
        ans = ""
        while i > -1:
            if s[i] == "#":
                number = int(s[i-2:i])
                i -= 3
            else:
                number = int(s[i])
                i -= 1
                
            ans += chr(96+number)
            
        
        return ans[::-1]