# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def find(node):
            if node.left is None and node.right is None:
                return (0, node.val, node.val)
            
            _min = float("inf")
            _max = -1
            ans = 0
            if node.left:
                x = find(node.left)
                ans = max(x[0], ans)
                _min = min(x[1], _min)
                _max = max(x[2], _max)
            if node.right:
                x = find(node.right)
                ans = max(x[0], ans)
                _min = min(x[1], _min)
                _max = max(x[2], _max)
            
            return (max((ans, abs(_min - node.val), abs(_max - node.val))), min(_min, node.val), max(_max, node.val))
        
        return find(root)[0]
            