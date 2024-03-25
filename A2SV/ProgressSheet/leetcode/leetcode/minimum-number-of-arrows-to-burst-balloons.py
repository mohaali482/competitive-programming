class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        print(points)
        current = points[0][1]
        counter = 1
        for i in range(len(points)):
            if points[i][0] > current:
                counter += 1
                current = points[i][1]
        
        return counter