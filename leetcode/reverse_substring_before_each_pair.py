class Solution:
    def reverseParentheses(self, s: str) -> str:
        ans = s
        ind = []
        for i in range(len(s)):
            if s[i] == "(":
                ind.append(i)
            elif s[i] == ")":
                j = ind.pop()
                ans = ans[:j] + ans[j: i+1][::-1] + ans[i+1:]

        ans = ans.replace('(', '')
        ans = ans.replace(')', '')

        return ans
