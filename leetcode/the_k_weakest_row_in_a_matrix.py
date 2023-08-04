class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rows = []
        for i in range(len(mat)):
            heapq.heappush(rows, (mat[i].count(1), i))
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(rows)[1])

        return ans
