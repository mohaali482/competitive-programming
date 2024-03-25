# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def solve(node):
            if node is None:
                return []
            if node.left is None and node.right is None:
                return [str(node.val)]
            val = str(node.val)
            left = solve(node.left)
            right = solve(node.right)
            result = [val+i for i in left+right]
            return result
        total = 0
        for i in solve(root):
            total += int(i)
        
        return total