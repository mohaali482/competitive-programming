class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        leng = len(s)
        max_size = 0
        se = set()
        while j < leng:
            while s[j] in se:
                se.remove(s[i])
                i += 1
            se.add(s[j])
            j += 1
            max_size = max(max_size, j-i)

        return max_size
