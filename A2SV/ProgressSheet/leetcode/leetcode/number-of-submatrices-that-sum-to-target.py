class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        prefix_sum = [[0]*(cols+1) for _ in range(rows + 1)]

        for r in range(rows):
            for c in range(cols):
                prefix_sum[r+1][c+1] = prefix_sum[r][c+1] + \
                                    prefix_sum[r+1][c] - prefix_sum[r][c] + \
                                    matrix[r][c]
        
        ans = 0
        for r1 in range(1, rows+1):
            for r2 in range(r1, rows+1):
                visited = defaultdict(int)
                visited[0] += 1

                for c in range(1, cols+1):
                    current = prefix_sum[r2][c] - prefix_sum[r1-1][c]

                    ans += visited[current - target]
                    visited[current] += 1

        return ans