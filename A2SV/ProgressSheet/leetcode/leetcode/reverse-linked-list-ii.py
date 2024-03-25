# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head

        current = dummy
        for i in range(left-1):
            current = current.next
        
        left_temp = current.next

        for i in range(right-left):
            temp2 = current.next
            current.next = left_temp.next
            left_temp.next = left_temp.next.next
            current.next.next = temp2
        
        return dummy.next
            