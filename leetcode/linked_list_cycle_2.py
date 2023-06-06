# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next and head.next.next:
            tur = head
            rab = head
            found = False
            while rab and rab.next and rab.next.next:
                tur = tur.next
                rab = rab.next.next
                if tur == rab:
                    found = True
                    break
            if found:
                tur = head
                while tur and tur.next:
                    if rab == tur:
                        return rab
                    tur = tur.next
                    rab = rab.next
            return None
        else:
            return None
