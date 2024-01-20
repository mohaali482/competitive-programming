# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        ans = []
        stack = []
        node = root
        while True:
            if node is not None:
                stack.append(node)
                node = node.left
            elif stack:
                node = stack.pop()
                ans.append(node.val)
                node = node.right
            else:
                break

        return ans
