class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] += 1
        tot = 0
        ans = 0
        for i in range(len(nums)):
            tot += nums[i]

            if tot%k in prefix:
                ans += prefix[tot%k]
            
            prefix[tot%k] += 1

        return ans