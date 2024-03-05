class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        ans = "z" * len(palindrome)
        for i in range(len(palindrome)):
            if palindrome[i] == "a":
                current = palindrome[:len(palindrome)-1-i] + 'b' + palindrome[len(palindrome)-i:]
                if current != current[::-1]:
                    ans = min(ans, current)
            else:
                current = palindrome[:i] + 'a' + palindrome[i+1:]
                if current != current[::-1]:
                    ans = min(ans, current)
                    break
        
        return ans
