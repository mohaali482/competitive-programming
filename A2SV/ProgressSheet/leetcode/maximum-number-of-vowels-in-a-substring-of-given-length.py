class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        if k > len(s):
            return 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        vowelCounter = 0

        for i in range(k-1):
            if s[i] in vowels:
                vowelCounter += 1
        left = 0
        right = k-1
        ans = vowelCounter
        
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
