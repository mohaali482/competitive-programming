class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i = 0
        j = len(people) - 1
        boats = 0
        counter = 0
        sum = 0
        while i <= j:
            if counter == 2:
                sum = 0
                counter = 0
                boats += 1
            if sum + people[j] <= limit:
                sum += people[j]
                counter += 1
                j -= 1

            elif sum + people[i] <= limit:
                sum += people[i]
                counter += 1
                i += 1
            else:
                counter = 0
                boats += 1
                sum = 0
        if sum != 0:
            boats += 1
        return boats
