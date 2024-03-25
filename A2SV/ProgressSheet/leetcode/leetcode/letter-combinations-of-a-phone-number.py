class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        nums = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        ans = []
        current = []
        def solve(index):
            if index == len(digits):
                ans.append(''.join(current))
                return
            
            for i in nums[digits[index]]:
                current.append(i)
                solve(index+1)
                current.pop()
            
        solve(0)
        return ans