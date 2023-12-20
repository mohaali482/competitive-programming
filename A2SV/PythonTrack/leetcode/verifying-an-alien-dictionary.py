class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        index = {order[i]: i for i in range(len(order))}
        def cmp(a, b):
            i = 0
            j = 0
            while i < len(a) and j < len(b):
                if index[a[i]] > index[b[j]]:
                    return 1
                elif index[a[i]] < index[b[j]]:
                    return -1
                i += 1
                j += 1
            if len(a[i:]) > len(b[j:]):
                return 1
            elif len(a[i:]) < len(b[j:]):
                return -1
            
            return 0
        
        sorted_words = sorted(words, key=cmp_to_key(cmp))
        for i in range(len(sorted_words)):
            if sorted_words[i] != words[i]:
                return False
            
        
        return True
