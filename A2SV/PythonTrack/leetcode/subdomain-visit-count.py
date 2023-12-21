class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counter = defaultdict(int)
        for domain in cpdomains:
            count, dom = domain.split()
            count = int(count)
            dd = dom.split(".")
            for d in range(len(dd)):
                counter[".".join(dd[d:])] += count
        
        ans = []
        for k, v in counter.items():
            ans.append(f"{v} {k}")


        return ans