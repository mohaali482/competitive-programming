class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        len_num2 = len(nums2)
        nums = []
        for i in nums1:
            index = nums2.index(i)
            if index+1 >= len_num2:
                nums.append(-1)
            else:
                flag = False
                for j in range(index+1, len_num2):
                    if nums2[j] > i:
                        nums.append(nums2[j])
                        flag = True
                        break
                if not flag:
                    nums.append(-1)

        return nums
