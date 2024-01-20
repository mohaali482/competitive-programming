class Solution:
    def bfs(self, graph, query):
        if query[0] not in graph or query[1] not in graph:
            return -1

        queue = deque()
        queue.append((query[0], 1))
        visited = set()
        while queue:
            node = queue.popleft()
            if node[0] == query[1]:
                return node[1]

            visited.add(node[0])
            for child in graph[node[0]]:
                if child[0] not in visited:
                    queue.append((child[0], child[1] * node[1]))

        return -1

    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        graph = defaultdict(list)
        ans = []
        for i in range(len(equations)):
            node1 = equations[i][0]
            node2 = equations[i][1]
            weight = values[i]
            graph[node1].append((node2, weight))
            graph[node2].append((node1, 1 / weight))

        for query in queries:
            ans.append(self.bfs(graph, query))

        return ans
