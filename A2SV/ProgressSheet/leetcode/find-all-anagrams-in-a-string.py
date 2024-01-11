class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        cp = Counter(p)
        cs = Counter(s[:len(p)-1])
        left = 0
        right = len(p) - 1
        ans = []
        while right < len(s):
            cs[s[right]] += 1
            
            if cs == cp:
                ans.append(left)
            
            cs[s[left]] -= 1
            left += 1
            right += 1
        
        return ans

