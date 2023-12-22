class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        max_len = 0
        for word in s:
            if len(word) > max_len:
                max_len = len(word)
        ans = []
        i = 0
        while i < max_len:
            word = ""
            for j in s:
                if i >= len(j):
                    word += " "
                else:
                    word += j[i]
            space = len(word)-1
            while space > -1:
                if word[space] != " ":
                    break
                
                space -= 1
            ans.append(word[:space+1])
            i += 1
        
        return ans