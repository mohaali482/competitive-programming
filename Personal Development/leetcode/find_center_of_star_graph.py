class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        connections = {}
        _max = 0
        for one, two in edges:
            if not one in connections:
                connections[one] = 0
            if not two in connections:
                connections[two] = 0

            connections[one] += 1
            connections[two] += 1

            _max = max([one, two, _max])

        for key in connections:
            if connections[key] == _max - 1:
                return key

        return -1
