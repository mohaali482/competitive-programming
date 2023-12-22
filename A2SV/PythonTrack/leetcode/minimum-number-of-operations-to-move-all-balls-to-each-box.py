class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0]*len(boxes)
        for i in range(len(boxes)):
            curr = 0
            for j in range(len(boxes)):
                curr += abs(j-i) if boxes[j] == "1" else 0
            ans[i] = curr

        return ans