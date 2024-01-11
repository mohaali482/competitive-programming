class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_freq = Counter(s1)
        i = 0
        j = len(s1)-1
        window = Counter(s2[:len(s1)-1])
    
        while j < len(s2):
            window[s2[j]] += 1

            if window == s1_freq:
                return True

            window[s2[i]] -= 1
            i += 1
            j += 1
        return False 