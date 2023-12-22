class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        return min(sum(distance[min(start, destination): max(start, destination)]), sum(distance[:min(destination, start)]) + sum(distance[max(destination, start):]))