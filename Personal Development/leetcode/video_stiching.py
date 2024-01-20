class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        ans = 0
        end_time = 0
        i = 0
        while i < len(clips):
            if clips[i][0] > end_time:
                return -1

            _max = end_time
            while i < len(clips) and clips[i][0] <= end_time:
                _max = max(_max, clips[i][1])
                i += 1
            ans += 1
            end_time = _max

            if end_time >= time:
                return ans

        return -1
