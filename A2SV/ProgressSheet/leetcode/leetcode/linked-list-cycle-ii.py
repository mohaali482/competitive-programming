# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        
        if fast != slow or fast.next is None:
            return None
        
        slow2 = head
        while slow2 != slow:
            slow2 = slow2.next
            slow = slow.next
        
        return slow
