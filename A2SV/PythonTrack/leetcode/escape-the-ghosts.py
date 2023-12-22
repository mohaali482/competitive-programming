class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        return sum(map(abs,target)) < min([abs(target[0] - ghosts[i][0]) + abs(target[1] - ghosts[i][1]) for i in range(len(ghosts))])