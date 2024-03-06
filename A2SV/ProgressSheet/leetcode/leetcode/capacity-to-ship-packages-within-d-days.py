class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        def getDays(weight):
            counter = 1
            current = weights[0]
            for i in range(1, len(weights)):
                if weights[i] + current <= weight:
                    current += weights[i]
                else:
                    current = weights[i]
                    counter += 1

            return counter

        while left <= right:
            mid = left + (right-left)//2
            current_days = getDays(mid)
            
            if current_days > days:
                left = mid+1
            else:
                right = mid-1
        
        return left