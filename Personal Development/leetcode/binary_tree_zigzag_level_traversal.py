# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        ans = []
        zig = True
        while queue:
            length = len(queue)
            arr = []
            if zig:
                for i in range(length):
                    node = queue.popleft()
                    arr.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                zig = False
            else:
                for i in range(length):
                    node = queue.pop()
                    arr.append(node.val)
                    if node.right:
                        queue.appendleft(node.right)
                    if node.left:
                        queue.appendleft(node.left)
                zig = True
            ans.append(arr)

        return ans
