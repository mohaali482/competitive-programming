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
        found = False
        def find(current):
            nonlocal counter, ans, found
            if found:
                return
            if current is None:
                return
            
            find(current.left)
            counter += 1
            if counter == k:
                ans = current.val
                found = True
                return
            
            find(current.right)
        find(root)
        return ans