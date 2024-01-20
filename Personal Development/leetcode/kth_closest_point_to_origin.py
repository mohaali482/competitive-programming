class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = [(math.sqrt(i[0] ** 2 + i[1] ** 2), i) for i in points]
        heapq.heapify(ans)
        answers = []
        for i in range(k):
            answers.append(heapq.heappop(ans)[1])

        return answers
