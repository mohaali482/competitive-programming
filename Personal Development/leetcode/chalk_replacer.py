class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        summ = [chalk[0]]
        for i in range(1, len(chalk)):
            summ.append(chalk[i] + summ[-1])
        k -= ((k//summ[-1])*summ[-1])

        for i in range(len(chalk)):
            if k - summ[i] < 0:
                return i
