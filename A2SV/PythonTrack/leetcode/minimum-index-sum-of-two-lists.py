class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = set(list1) & set(list2)
        v = {}
        for i in range(len(list1)):
            if list1[i] in common:
                v[list1[i]] = i
        for j in range(len(list2)):
            if list2[j] in common:
                v[list2[j]] += j
        ans = []
        min_value = min(v.values())
        for k in v:
            if v[k] == min_value:
                ans.append(k)
        
        return ans