# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        next = None
        temp = head
        while temp and temp.next:
            temp2 = temp.next
            temp.next = next
            next = temp
            temp = temp2
        
        temp.next = next
        return temp