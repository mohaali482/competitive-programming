class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def check_arithmetic(arr: List[int]):
            arr.sort()
            difference = arr[1] - arr[0]
            flag = True
            for i in range(len(arr)-1):
                if arr[i+1] - arr[i] != difference:
                    flag = False
                    break

            return flag

        for j in range(len(l)):
            yield check_arithmetic(nums[l[j]: r[j]+1])
