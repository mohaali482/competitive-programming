# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        visited = defaultdict(list)
        def dfs(node, row, col):
            if node is None:
                return
            
            visited[col].append((node.val, row))
            dfs(node.left, row+1, col-1)
            dfs(node.right, row+1, col+1)
        
        dfs(root, 0, 0)
        ans=[]
        for i in sorted(visited.keys()):
            lst=visited[i]
            lst.sort(key=lambda x:(x[1],x[0]))
            temp=[]
            for i in lst:
                temp.append(i[0])
            ans.append(temp)
        return ans