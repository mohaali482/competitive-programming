class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        maxIndex = {}
        minIndex = {}
        for i in range(len(s)):
            maxIndex[s[i]] = i + 1
        i = 0
        chars = []
        ans = []
        while i < len(s):
            chars.append(s[i])
            counter = 0
            while chars:
                c = chars.pop()
                while i < maxIndex[c]:
                    if s[i] not in chars:
                        chars.append(s[i])
                    i += 1
                    counter += 1
            ans.append(counter)
        return ans