class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(set)
        for one, two in richer:
            graph[two].add(one)

        ans = [0] * len(quiet)

        def recurse(key):
            if ans[key] != 0:
                return (quiet[ans[key]], ans[key])
            if not key in graph:
                return (quiet[key], key)

            array = []
            array.append((quiet[key], key))
            for i in graph[key]:
                array.append(recurse(i))

            return min(array)

        for key in range(len(quiet)):
            wait = recurse(key)
            ans[key] = recurse(key)[1]

        return ans
