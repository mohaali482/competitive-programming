class Solution:
    def check(self, sDict, tDict):
        for key, value in tDict.items():
            if key not in sDict or sDict[key] < value:
                return False
        
        return True

    def minWindow(self, s: str, t: str) -> str:
        tDict = Counter(t)
        window = defaultdict(int)
        left = 0
        right = 0
        ans = float("inf")
        ansLeft = 0
        ansRight = 0
        while right < len(s):
            window[s[right]] += 1

            while left <= right and self.check(window, tDict):
                dist = (right - left) + 1
                if dist < ans:
                    ans = dist
                    ansLeft = left
                    ansRight = right
                
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                
                left += 1
            
            right += 1
        
        if ans == float("inf"):
            return ""
        
        return s[ansLeft:ansRight+1]