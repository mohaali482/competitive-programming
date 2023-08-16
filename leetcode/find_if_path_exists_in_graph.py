class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        graph = {i: set() for i in range(n)}
        for _from, to in edges:
            graph[_from].add(to)
            graph[to].add(_from)

        visited = set()
        queue = deque([source])
        while queue:
            node = queue.popleft()
            if node in visited:
                continue
            if node == destination:
                return True

            visited.add(node)
            queue.extend(graph[node])

        return False
