# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isLeaf(self, node):
        return node.right == node.left == None

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        queue = deque([(root, root.val)])
        while queue:
            node, path_sum = queue.popleft()
            if self.isLeaf(node) and path_sum == targetSum:
                return True

            if node.left:
                queue.append((node.left, path_sum + node.left.val))
            if node.right:
                queue.append((node.right, path_sum + node.right.val))

        return False
