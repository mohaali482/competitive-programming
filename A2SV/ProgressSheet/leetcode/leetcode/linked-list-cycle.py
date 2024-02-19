# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tur = head
        rab = head
        while rab and rab.next and rab.next.next:
            tur = tur.next
            rab = rab.next.next
            if tur == rab:
                return True
        
        return False