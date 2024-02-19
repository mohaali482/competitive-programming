class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for i in s:
            if i == ")":
                j = stack.pop()
                if j == "(":
                    stack.append(1)
                else:
                    while stack and stack[-1] != "(":
                        j += stack.pop()
                    stack.pop()
                    stack.append(2*j)
            else:
                stack.append(i)
        return sum(stack)