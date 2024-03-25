class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        store = defaultdict(lambda: [0])
        indexes = {}
        for i in range(len(nums)):
            indexes[i] = len(store[nums[i]])
            store[nums[i]].append(i)
        
        ignore = set()
        for k in store:
            if len(store[k]) > 2:
                for i in range(1, len(store[k])):
                    store[k][i] = store[k][i] + store[k][i-1]
            else:
                ignore.add(k)

        ans = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] not in ignore:
                first = (i * (indexes[i]+1)) - store[nums[i]][indexes[i]]
                second = store[nums[i]][-1] - store[nums[i]][indexes[i]-1] - (i * (len(store[nums[i]]) - (indexes[i]-1)))
                ans[i] = first + second
        
        return ans
