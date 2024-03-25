# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        _max = max(nums)
        index = nums.index(_max)
        return TreeNode(_max, self.constructMaximumBinaryTree(nums[:index]), self.constructMaximumBinaryTree(nums[index+1:]))