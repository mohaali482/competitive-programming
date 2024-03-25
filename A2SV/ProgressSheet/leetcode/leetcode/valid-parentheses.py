class Solution:
    def isValid(self, s: str) -> bool:
        valid = {")":"(", "}":"{", "]":"["}
        stack = []
        for i in s:
            if i in valid:
                if not stack:
                    return False
                
                if stack[-1] != valid[i]:
                    return False
                
                stack.pop()
            else:
                stack.append(i)
        
        return len(stack) == 0