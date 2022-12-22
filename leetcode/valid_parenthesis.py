class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = {")": "(", "}": "{", "]": "["}
        try:
            for i in s:
                if not i in valid.keys():
                    stack.append(i)
                elif valid[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
        except:
            return False

        if not stack:
            return True

        return False
