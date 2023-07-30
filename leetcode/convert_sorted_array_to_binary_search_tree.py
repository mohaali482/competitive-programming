# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def construct(num):
            if not num:
                return
            if len(num) == 1:
                return TreeNode(num[0])

            root = TreeNode(num[len(num) // 2])
            root.left = construct(num[: len(num) // 2])
            root.right = construct(num[(len(num) // 2) + 1 :])
            return root

        return construct(nums)
