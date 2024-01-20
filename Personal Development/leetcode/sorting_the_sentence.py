class Solution:
    def sortSentence(self, s: str) -> str:
        a = s.split()
        b = {}
        for i in a:
            b[int(i[-1])] = i[:-1]
        st = [b[i] for i in range(1, len(a)+1)]
        return " ".join(st)
