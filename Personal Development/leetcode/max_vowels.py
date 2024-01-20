class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i = 0
        j = k
        counter = 0
        vowels = 'aeiou'
        for m in range(j):
            if s[m] in vowels:
                counter += 1
        maxi = counter
        while j < len(s):
            if not s[i] in vowels and s[j] in vowels:
                counter = counter + 1
            elif not s[j] in vowels and s[i] in vowels:
                counter = counter - 1
            maxi = max(counter, maxi)
            i += 1
            j += 1

        return maxi
