class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def solve(current_s, current_set):
            if len(current_s) == 0:
                return ""
            
            for i in range(len(current_s)):
                if current_s[i].upper() not in current_set or current_s[i].lower() not in current_set:
                    left_slice = current_s[:i]
                    right_slice = current_s[i+1:]

                    left = solve(left_slice, set(left_slice))
                    right = solve(right_slice, set(right_slice))

                    if len(left) > len(right):
                        return left
                    elif len(left) < len(right):
                        return right
                    else:
                        return left
            
            return current_s
        
        return solve(s, set(s))