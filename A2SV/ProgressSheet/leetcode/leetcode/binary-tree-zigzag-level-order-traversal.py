# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        ans = []
        turn = False
        queue = deque([root])
        while queue:
            n = len(queue)
            current = []
            for i in range(n):
                node = queue.popleft()
                current.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if turn:
                ans.append(current[::-1])
            else:
                ans.append(current)
            turn = not turn
        
        return ans