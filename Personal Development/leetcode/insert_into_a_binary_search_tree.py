    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
            def helper(node, val):
                if node is None:
                    return
                
                if node.val > val:
                    if node.left is None:
                        node.left = TreeNode(val)
                        return
                    return helper(node.left, val)
                if node.val < val:
                    if node.right is None:
                        node.right = TreeNode(val)
                        return
                    return helper(node.right, val)
            if root is None:
                return TreeNode(val)
            helper(root, val)
            return root
            