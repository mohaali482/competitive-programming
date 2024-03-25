# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if node is None:
                return None
            start, end = sorted([p.val, q.val])
            if start <= node.val <= end:
                return node
            
            if max(q.val, p.val) < node.val:
                return dfs(node.left)
            else:
                return dfs(node.right)
        
        return dfs(root)