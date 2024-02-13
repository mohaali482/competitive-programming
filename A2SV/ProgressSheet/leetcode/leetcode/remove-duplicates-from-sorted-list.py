# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        temp = head
        temp2 = head.next
        while temp2:
            while temp2 and temp.val == temp2.val:
                temp2 = temp2.next
            
            temp.next = temp2
            temp = temp.next
            if temp:
                temp2 = temp.next
            else:
                break
        
        return head