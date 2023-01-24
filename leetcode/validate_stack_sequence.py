class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = 0
        j = 0
        stack = []
        for i in pushed:
            if i != popped[j]:
                stack.append(i)
            else:
                stack.append(i)
                while stack:
                    if stack[-1] == popped[j]:
                        stack.pop()
                        j += 1
                    else:
                        break

        return not stack
