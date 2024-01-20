# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = [0]

        def good(root, max_path):
            if max_path == root.val:
                ans[0] += 1

            if root.left:
                good(root.left, max(max_path, root.left.val))
            if root.right:
                good(root.right, max(max_path, root.right.val))

        good(root, root.val)
        return ans[0]
