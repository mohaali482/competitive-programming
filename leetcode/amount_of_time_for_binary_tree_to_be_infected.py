# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        nodes = {}
        q = deque([root])
        while q:
            node = q.popleft()
            if node.val not in nodes:
                nodes[node.val] = []
            if node.left:
                q.append(node.left)
                nodes[node.val].append(node.left.val)
                if node.left.val not in nodes:
                    nodes[node.left.val] = []
                nodes[node.left.val].append(node.val)
            if node.right:
                q.append(node.right)
                nodes[node.val].append(node.right.val)
                if node.right.val not in nodes:
                    nodes[node.right.val] = []
                nodes[node.right.val].append(node.val)
        visited = set()
        infections = {start: 0}
        qu = [start]
        _max = 0
        stack = [(start, 0)]

        while stack:
            key, time = stack.pop()
            if key not in visited:
                visited.add(key)
                value_list = nodes[key]

                for value in value_list:
                    if value not in infections:
                        stack.append((value, time + 1))
                        infections[value] = time + 1
                        _max = max(_max, time + 1)

        return _max
