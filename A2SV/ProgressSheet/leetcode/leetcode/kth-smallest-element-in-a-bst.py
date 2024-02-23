# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = 0
        ans = 0
        def find(current):
            if current is None:
                return
            
            find(current.left)
            nonlocal counter, ans
            counter += 1
            if counter == k:
                ans = current.val
            
            find(current.right)
        find(root)
        return ans