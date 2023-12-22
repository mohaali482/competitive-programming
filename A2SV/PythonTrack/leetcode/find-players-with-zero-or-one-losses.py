class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        w = defaultdict(int)
        l = defaultdict(int)
        c = defaultdict(int)
        for match in matches:
            w[match[0]] += 1
            l[match[1]] += 1
            c[match[0]] += 1
            c[match[1]] += 1
        
        return [sorted([i for i in w if w[i] == c[i]]), sorted([i for i in l if l[i] == 1])]