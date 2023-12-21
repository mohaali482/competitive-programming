class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        dicti = {
            1: set("qwertyuiop"),
            2: set("asdfghjkl"),
            3: set("zxcvbnm")
        }
        ans = []
        for word in words:
            for row in dicti.keys():
                if word[0].lower() in dicti[row]:
                    break
            for c in set(word.lower()):
                if c not in dicti[row]:
                    break
            else:
                ans.append(word)
        
        return ans