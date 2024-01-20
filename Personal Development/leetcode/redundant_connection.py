class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        rank = [1 for i in range(len(edges) + 1)]
        
        def find_parent(e):
            p = parent[e]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            
            return p
        
        def union(a, b):
            pa = find_parent(a)
            pb = find_parent(b)

            if pa == pb:
                return False
            
            ra = rank[pa]
            rb = rank[pb]

            if ra > rb:
                parent[pb] = pa
                rank[pa] += rb
            else:
                parent[pa] = pb
                rank[pb] += ra
            
            return True

        for a, b in edges:
            if not union(a, b):
                return [a, b]
