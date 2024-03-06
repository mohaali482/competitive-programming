# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, node):
        if node is None:
            return True, [float("inf"), float("-inf")], 0
        
        valid_left, left_range, left_sum = self.check(node.left)
        valid_right, right_range, right_sum = self.check(node.right)
        if valid_left and valid_right and left_range[1] < node.val < right_range[0]:
            total = left_sum + right_sum + node.val
            self.ans = max(self.ans, total)
            return True, [min(left_range[0], node.val), max(right_range[1], node.val)], total

        return False, [float('inf'), float('-inf')], None

    
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.check(root)
        return self.ans