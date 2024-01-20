# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        ans = []
        queue = deque([root])
        while queue:
            length = len(queue)
            _max = float("-inf")
            for i in range(length):
                node = queue.popleft()
                _max = max(_max, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(_max)
        return ans
