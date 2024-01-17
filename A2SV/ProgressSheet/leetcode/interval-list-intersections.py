class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        first = 0
        second = 0
        ans = []
        while first < len(firstList) and second < len(secondList):
            firstRange = firstList[first]
            secondRange = secondList[second]
            if secondRange[0] <= firstRange[1] <= secondRange[1]:
                ans.append([max(firstRange[0], secondRange[0]), min(firstRange[1], secondRange[1])])
                first += 1
            elif firstRange[0] <= secondRange[1] <= firstRange[1]:
                ans.append([max(firstRange[0], secondRange[0]), min(firstRange[1], secondRange[1])])
                second += 1
            else:
                if firstRange[0] < secondRange[0]:
                    first += 1
                else:
                    second += 1

        return ans