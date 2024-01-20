class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        totalShifts = [0] * (len(s)+1)
        for shift in shifts:
            start, end, direction = shift
            movement = 1 if direction == 1 else -1
            totalShifts[start] += movement
            totalShifts[end+1] -= movement
        
        for i in range(1, len(totalShifts)):
            totalShifts[i] = totalShifts[i] + totalShifts[i-1]
        
        ans = ['']*len(s)
        for i in range(len(s)):
            ans[i] = chr((ord(s[i]) - ord("a") + totalShifts[i]) % 26 + ord("a"))
        
        return ''.join(ans)