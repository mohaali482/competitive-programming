# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def find(node):
            ans = 0
            if low <= node.val <= high:
                ans += node.val

            if low < node.val and node.left:
                ans += find(node.left)
            if node.val < high and node.right:
                ans += find(node.right)
            
            return ans
        
        return find(root)