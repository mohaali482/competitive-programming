class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        store = {}
        stack = []
        for i in nums2:
            while stack and stack[-1] < i:
                item = stack.pop()
                store[item] = i
            stack.append(i)
        
        ans = [-1] * len(nums1)
        for i in range(len(nums1)):
            if nums1[i] in store:
                ans[i] = store[nums1[i]]

        return ans