# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root.left is None and root.right is None:
            return [f"{root.val}"]
        ans = []
        if root.left:
            self.dfs(root.left, f"{root.val}", ans)
        if root.right:
            self.dfs(root.right, f"{root.val}", ans)
        return ans

    def dfs(self, node, path, ans):
        if node is None:
            return
        path += f"->{node.val}"

        if node.left:
            self.dfs(node.left, path, ans)
        if node.right:
            self.dfs(node.right, path, ans)
        if node.left is None and node.right is None:
            ans.append(path)
