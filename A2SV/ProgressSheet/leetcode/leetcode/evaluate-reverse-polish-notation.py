class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {"+", "-","/","*"}
        stack = []
        for i in tokens:
            if not i in ops:
                stack.append(i)
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(int(eval(str(op2) + i + str(op1))))

        return int(stack.pop())