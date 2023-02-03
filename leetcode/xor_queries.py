class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xor = [arr[0]]
        for i in range(1, len(arr)):
            xor.append(xor[-1] ^ arr[i])
        for i in queries:
            ii, jj = i
            if ii == jj:
                yield arr[jj]
            elif ii == 0:
                yield xor[jj]
            else:
                yield xor[jj] ^ xor[ii] ^ arr[ii]

        return []
