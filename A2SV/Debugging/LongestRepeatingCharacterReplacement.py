class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        for i in range(ord('A'), ord('Z')+1):
            left = 0
            ops = k
            target = chr(i)

            for right in range(len(s)):
                if s[right] != target:
                    ops -= 1
                
                # Remove equals to "=" because we have to reduce our window
                #  if and only if the number of operations used are more than "k".
                while ops < 0 and s[right] != target:
                    if s[left] != target:
                        ops += 1
                    left += 1
                max_length = max(max_length, right - left + 1)
    
        return max_length
    

if __name__ == '__main__':
    assert Solution().characterReplacement("ABAB", 2) == 4
    assert Solution().characterReplacement("AABABBA", 1) == 4