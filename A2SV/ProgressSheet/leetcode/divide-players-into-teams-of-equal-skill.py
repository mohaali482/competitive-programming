class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        ans = 0
        skill.sort()
        _sum = skill[0] + skill[-1]
        i = 0
        j = len(skill) - 1
        while i < j:
            c = skill[i] * skill[j]
            d = skill[i] + skill[j]
            if d != _sum:
                return -1
            ans += c

            i += 1
            j -= 1
        
        return ans