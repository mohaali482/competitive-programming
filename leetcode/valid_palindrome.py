import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        for i in string.punctuation:
            s = s.replace(i, "")
        s = s.lower()
        return s[::-1] == s
