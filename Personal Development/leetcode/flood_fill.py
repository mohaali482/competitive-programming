class Solution:
    movement = ((1, 0), (-1, 0), (0, 1), (0, -1))

    def isBound(self, image: List[List[int]], point: Tuple[int]):
        if point[0] >= len(image) or point[0] < 0:
            return False

        if point[1] >= len(image[0]) or point[1] < 0:
            return False

        return True

    def getNeighbors(self, image: List[List[int]], point: Tuple[int]):
        neighbors = []
        for x, y in self.movement:
            newPoint = (point[0] + x, point[1] + y)
            if (
                self.isBound(image, newPoint)
                and image[point[0]][point[1]] == image[newPoint[0]][newPoint[1]]
            ):
                neighbors.append(newPoint)

        return neighbors

    def dfs(self, image: List[List[int]], point: Tuple[int], color: int):
        if point in self.visited:
            return

        self.visited.add(point)
        for neighbor in self.getNeighbors(image, point):
            self.dfs(image, neighbor, color)
        image[point[0]][point[1]] = color

    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        self.visited = set()
        self.dfs(image, (sr, sc), color)

        return image
