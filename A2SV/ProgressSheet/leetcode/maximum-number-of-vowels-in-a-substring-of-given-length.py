class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        if k > len(s):
            return 0
        vowelCounter = 0
        left = 0
        right = 1
        vowels = {'a', 'e', 'i', 'o', 'u'}
        ans = 0
        if s[left] in vowels:
            vowelCounter += 1
            ans += 1
        
        while right < len(s):
            if s[right] in vowels:
                vowelCounter += 1
            
            if (right - left) + 1 > k:
                if s[left] in vowels:
                    vowelCounter -= 1
                left += 1
            
            ans = max(ans, vowelCounter)
            right += 1
        
        return ans
