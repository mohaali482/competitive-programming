class Solution:
    def sortSentence(self, s: str) -> str:
        words = [(i[-1], i[:-1]) for i in s.split()]
        words.sort()
        return ' '.join([word for _, word in words])