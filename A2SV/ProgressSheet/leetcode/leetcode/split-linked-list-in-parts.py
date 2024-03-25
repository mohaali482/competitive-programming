# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getLength(self, head: Optional[ListNode]) -> int:
        temp = head
        count = 0
        while temp:
            temp = temp.next
            count += 1
        
        return count

    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        total = self.getLength(head)
        n = ceil(total/k)
        ans = []
        temp = head
        ans.append(temp)
        count = 1
        while temp:
            if count == n:
                temp2 = temp.next
                temp.next = None
                
                total -= count
                divider = k-len(ans)
                if divider == 0:
                    break
                n = ceil(total/(divider))

                temp = temp2
                ans.append(temp)

                count = 1
            else:
                temp = temp.next
                count += 1
        if len(ans) != k:
            ans.extend([None] * (k-len(ans)))
        
        return ans