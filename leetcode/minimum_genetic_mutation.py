class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        if endGene not in bank:
            return -1
        
        queue = deque()
        queue.append((startGene, 0))
        visited = set([startGene])
        while queue:
            gene, level = queue.popleft()
            if gene == endGene:
                return level
            
            for i in range(len(gene)):
                for c in "ACGT":
                    newGene = gene[:i] + c + gene[i+1:]
                    if newGene in bank and newGene not in visited:
                        queue.append((newGene, level + 1))
                        visited.add(newGene)
        
        return -1