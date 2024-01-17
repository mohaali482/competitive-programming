class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        window = defaultdict(int)
        left = 0
        right = 0
        ans = 0
        while right < len(fruits):
            window[fruits[right]] += 1

            while len(window) > 2:
                window[fruits[left]] -= 1
                if window[fruits[left]] == 0:
                    del window[fruits[left]]
                
                left += 1
            ans = max(ans, (right-left)+1)
            right += 1
        
        return ans