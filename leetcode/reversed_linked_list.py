# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            if not head.next:
                return head
            current = ListNode()
            current.val = head.next.val
            current.next = ListNode(val=head.val)
            head = head.next
        else:
            return head
        while head.next:
            current2 = ListNode()
            current2.val = head.next.val
            current2.next = current
            current = current2
            head = head.next
        return current
