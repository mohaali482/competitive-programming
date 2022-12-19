class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        lis = []
        for point in points:
            x2, y2 = point
            key = (x2**2+y2**2)**.5
            lis.append(key)

        ans = zip(lis, points)
        ans.sort()
        answ = []
        for i in range(k):
            answ.append(list(ans[i])[1])

        return answ
