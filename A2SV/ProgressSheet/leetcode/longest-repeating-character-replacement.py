class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        left = 0
        right = 0
        window = defaultdict(int)
        _max = 0
        _max_c = ''
        while right < len(s):
            window[s[right]] += 1
            
            if window[s[right]] > _max:
                _max = window[s[right]]
                _max_c = s[right]
            
            total = (right-left + 1) - _max

            if k - total >= 0:
                ans = max(ans, right-left + 1)
            else:
                if _max_c == s[left]:
                    _max -= 1
                if _max == 0:
                    _max_c = ''
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    window.pop(s[left])
                left += 1
            right += 1

        return ans
