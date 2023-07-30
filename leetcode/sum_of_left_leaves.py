# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        leaves = 0
        while queue:
            node = queue.popleft()
            if node.left:
                if node.left.right is None and node.left.left is None:
                    leaves += node.left.val
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return leaves
