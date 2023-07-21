class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        num = range(1, n + 1)
        ans = []

        def backtrack(i, combination):
            if len(combination) == k:
                ans.append(combination.copy())
                return
            if i >= n:
                return

            combination.append(num[i])
            backtrack(i + 1, combination)
            combination.pop()
            backtrack(i + 1, combination)

        backtrack(0, [])
        return ans
