class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        maxIndex = {}
        for i in range(len(s)):
            maxIndex[s[i]] = i + 1
        i = 0
        ans = []
        while i < len(s):
            counter = 0
            mx = maxIndex[s[i]]
            while i < mx:
                counter += 1
                mx = max(mx, maxIndex[s[i]])
                i += 1
            ans.append(counter)
        return ans