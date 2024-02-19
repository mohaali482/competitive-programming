# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None
            
        temp = head
        temp2 = head
        for i in range(n):
            temp2 = temp2.next
        
        if not temp2:
            return temp.next
        
        while temp2 and temp2.next:
            temp2 = temp2.next
            temp = temp.next
        
        if temp and temp.next:
            temp.next = temp.next.next
        return head