class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        currentChange = defaultdict(int)
        for bill in bills:
            if bill == 5:
                currentChange[bill] += 1
            elif bill == 10:
                currentChange[bill] += 1
                if currentChange[5] > 0:
                    currentChange[5] -= 1
                else:
                    return False
            else:
                currentChange[bill] += 1
                if currentChange[10] > 0:
                    currentChange[10] -= 1
                    if currentChange[5] > 0:
                        currentChange[5] -= 1
                    else:
                        return False
                elif currentChange[5] > 2:
                    currentChange[5] -= 3
                else:
                    return False
            
        return True
