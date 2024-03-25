class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        invalid = 0
        for i in s:
            if i == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    invalid += 1
            else:
                stack.append(i)
        
        return len(stack) + invalid