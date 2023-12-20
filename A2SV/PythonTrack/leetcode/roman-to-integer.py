class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        total = 0
        i = len(s) - 1 
        while i > -1:
            if i-1 > -1 and roman_values[s[i-1]] < roman_values[s[i]]:
                total += roman_values[s[i]]
                total -= roman_values[s[i-1]]
                i -= 2
            else:
                total += roman_values[s[i]]
                i -= 1
        
        return total