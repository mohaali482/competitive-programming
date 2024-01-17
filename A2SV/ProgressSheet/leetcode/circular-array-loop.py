class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        child = {}
        for i in range(len(nums)):
            child[i] = (i+nums[i])%len(nums)

        def dfs(num):
            if num in self.visited:
                pos = nums[num] > 0
                for i in self.visited:
                    if pos and nums[i] < 0:
                        return False
                    elif not pos and nums[i] > 0:
                        return False
                
                return child[num] != num
            
            self.visited.add(num)
            return dfs(child[num])

        self.visited = set()
        for i in child:
            if dfs(i):
                return True
            self.visited = set()
        
        return False