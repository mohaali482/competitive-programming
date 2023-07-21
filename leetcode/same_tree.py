# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if q is None and p is None:
            return True
        elif q is None and p is not None:
            return False
        elif q is not None and p is None:
            return False
        one = deque([p])
        two = deque([q])
        while one and two:
            node1 = one.popleft()
            node2 = two.popleft()
            if node1.val != node2.val:
                return False

            if node1.right is None and node2.right is not None:
                return False

            if node1.right is not None and node2.right is None:
                return False

            if node1.left is None and node2.left is not None:
                return False

            if node1.left is not None and node2.left is None:
                return False

            if node1.right:
                one.append(node1.right)
            if node2.right:
                two.append(node2.right)

            if node1.left:
                one.append(node1.left)
            if node2.left:
                two.append(node2.left)

        return True
