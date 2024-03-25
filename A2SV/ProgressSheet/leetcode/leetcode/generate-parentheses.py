class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(parentheses, open, close):
            if open == close == n:
                ans.append(parentheses)
                return
            
            if open < n:
                backtrack(parentheses + "(", open + 1, close)

            if close < open:
                backtrack(parentheses + ")", open, close + 1)
        backtrack("", 0, 0)
        return ans