class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        graph = {i: [] for i in range(numCourses)}

        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)

        def dfs(node):
            if len(graph[node]) == 0:
                return True
            if node in visited:
                return False

            visited.add(node)
            for child in graph[node]:
                if not dfs(child):
                    return False

            graph[node] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
