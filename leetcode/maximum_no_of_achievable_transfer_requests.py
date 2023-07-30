class Solution:
    def validNetChange(self, changes):
        for num in changes:
            if num != 0:
                return False

        return True

    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        changes = [0] * n

        def backtrack(i, count, changes, requests):
            if i == len(requests):
                if self.validNetChange(changes):
                    return count
                return 0

            request = requests[i]
            changes[request[0]] -= 1
            changes[request[1]] += 1

            take = backtrack(i + 1, count + 1, changes, requests)

            changes[request[0]] += 1
            changes[request[1]] -= 1

            skip = backtrack(i + 1, count, changes, requests)

            return max(take, skip)

        return backtrack(0, 0, changes, requests)
