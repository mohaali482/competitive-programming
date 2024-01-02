class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = Counter(nums1)
        d2 = Counter(nums2)
        ans = []
        for i in d1:
            if i in d2:
                for j in range(min(d2[i], d1[i])):
                    ans.append(i)
        
        return ans