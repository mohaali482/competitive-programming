class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        if len(answerKey) == 1:
            return len(answerKey)
        left = 0
        right = 1
        t_counter = 0
        f_counter = 0
        ans = 1
        if answerKey[left] == "T":
            t_counter += 1
        else:
            f_counter += 1
        
        while right < len(answerKey):
            if answerKey[right] == "T":
                t_counter += 1
            else:
                f_counter += 1
            
            while min(t_counter, f_counter) > k:        
                if answerKey[left] == "T":
                    t_counter -= 1
                else:
                    f_counter -= 1
                
                left += 1
            
            ans = max(t_counter + f_counter, ans)
            right += 1
        
        return ans

