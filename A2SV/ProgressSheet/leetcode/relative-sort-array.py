class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        countSort = Counter(arr1)
        ans = []
        j = 0
        for i in arr2:
            ans.extend([i] * countSort[i])
            j += countSort[i]
        
        difference = set(arr1) - set(arr2)
        otherNumbers = []
        for num in difference:
            otherNumbers.extend([num] * countSort[num])
        otherNumbers.sort()
        ans.extend(otherNumbers)
        
        return ans