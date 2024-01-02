class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        distance = defaultdict(list)
        for x, y in points:
            calc = (x**2 + y**2)**.5
            distance[calc].append([x, y])
        keys = sorted(distance.keys())
        for i in keys:
            j = 0
            while j < len(distance[i]) and len(ans) < k:
                ans.append(distance[i][j])
                j += 1
            if len(ans) == k:
                break
        return ans