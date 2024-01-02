class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(char) for char in  str(int(''.join([str(digit) for digit in digits]))+1)]

        