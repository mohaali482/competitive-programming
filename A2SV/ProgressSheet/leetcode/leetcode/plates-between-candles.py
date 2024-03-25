class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candles = [i for i in range(len(s)) if s[i] == "|"]
        ans = []
        for start, end in queries:
            st = bisect_left(candles, start)
            en = bisect_right(candles, end) - 1
            if st >= en:
                ans.append(0)
                continue
            
            ans.append(((candles[en]-candles[st])-1) - (en - st - 1))
    
        return ans