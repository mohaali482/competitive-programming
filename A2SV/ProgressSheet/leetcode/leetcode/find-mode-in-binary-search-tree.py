# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        visited = defaultdict(int)
        def dfs(node):
            if node is None:
                return 
            
            visited[node.val] += 1
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        max_value = max(visited.values())
        ans = []
        for i in visited:
            if visited[i] == max_value:
                ans.append(i)
        
        return ans