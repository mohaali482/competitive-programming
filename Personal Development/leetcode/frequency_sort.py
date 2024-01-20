from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        a = Counter(s)
        c = [[a[i], i] for i in a]

        c.sort(reverse=True)

        st = ""
        for i in c:
            st += i[1] * i[0]

        return st
