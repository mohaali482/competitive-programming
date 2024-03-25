# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraverse(self, node: TreeNode) -> List[int]:
        if node is None:
            return []
        ans = self.inorderTraverse(node.left)
        ans.append(node.val)
        ans.extend(self.inorderTraverse(node.right))
        return ans
    
    def buildTree(self, arr: List[int]) -> TreeNode:
        if not arr:
            return None
        half = len(arr)//2
        root = TreeNode(arr[half])
        root.left = self.buildTree(arr[:half])
        root.right = self.buildTree(arr[half+1:])
        return root

    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = self.inorderTraverse(root)
        return self.buildTree(arr)
