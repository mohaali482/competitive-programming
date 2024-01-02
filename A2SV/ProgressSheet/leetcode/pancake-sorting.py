class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        for i in range(len(arr),0,-1):
            pl = arr.index(i)
            if pl == i-1:
                continue
            if pl != 0:
                ans.append(pl+1)
                arr[:pl+1] = arr[:pl+1][::-1]
            ans.append(i)
            arr[:i] = arr[:i][::-1]
        return ans