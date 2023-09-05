class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()

        def dfs(node):
            visited.add(node)
            for child in rooms[node]:
                if child not in visited:
                    dfs(child)

        dfs(0)
        return len(visited) == len(rooms)
