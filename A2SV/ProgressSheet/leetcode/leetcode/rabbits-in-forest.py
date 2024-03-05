class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = Counter(answers)
        ans = 0
        for key, value in counter.items():
            ans += ceil(value/(key+1)) * (key+1)
        return ans