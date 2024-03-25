class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")
        for i in path:
            if len(i) > 0:
                if i == ".":
                    continue
                elif i != "..":
                    stack.append(i)
                elif i == ".." and stack:
                    stack.pop()
        return "/" + "/".join(stack)