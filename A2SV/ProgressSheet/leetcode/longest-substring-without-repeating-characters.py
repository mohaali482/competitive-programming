class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        counter = defaultdict(int)
        i = 0
        j = 1
        counter[s[i]] += 1
        ans = 0
        while j < len(s):
            counter[s[j]] += 1

            while counter[s[j]] > 1:
                counter[s[i]] -= 1
                i += 1
            ans = max((j - i) + 1, ans)

            j += 1
        
        return ans
