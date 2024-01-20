"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(self, employees: List["Employee"], id: int) -> int:
        ans = 0
        graph = {}
        value = {}

        for employee in employees:
            graph[employee.id] = employee.subordinates
            value[employee.id] = employee.importance

        _sum = 0
        queue = deque()
        queue.append(id)
        while queue:
            node = queue.popleft()

            _sum += value[node]

            for subordinate in graph[node]:
                queue.append(subordinate)

        return _sum
