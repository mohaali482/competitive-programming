class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []

        def allPath(graph, path):
            if path[-1] == len(graph) - 1:
                ans.append(path)
                return

            for i in range(len(graph[path[-1]])):
                allPath(graph, [*path, graph[path[-1]][i]])

        allPath(graph, [0])

        return ans
