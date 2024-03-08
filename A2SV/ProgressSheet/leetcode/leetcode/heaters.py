class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        maximum = float("-inf")
        heaters.sort()
        for house in houses:
            pos = bisect_left(heaters, house)

            prev_heater_distance = float("inf")
            if pos > 0:
                prev_heater_distance = house - heaters[pos-1]
            
            next_heater_distance = float("inf")
            if pos < len(heaters):
                next_heater_distance = heaters[pos] - house

            min_distance = min(prev_heater_distance, next_heater_distance)

            maximum = max(maximum, min_distance)
        
        return maximum