class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = [(heights[i], names[i]) for i in range(len(names))]
        people.sort(reverse=True)
        return [name for _, name in people]