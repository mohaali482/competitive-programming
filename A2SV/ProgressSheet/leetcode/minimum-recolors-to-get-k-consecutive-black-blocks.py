class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white = Counter(blocks[:k-1])["W"]
        left = 0
        right = k - 1
        ans = float("inf")
        while right < len(blocks):
            if blocks[right] == "W":
                white += 1
            
            ans = min(ans, white)
            
            if blocks[left] == "W":
                white -= 1
            
            right += 1
            left += 1
        
        return ans
            