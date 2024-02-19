# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getLength(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        temp = head
        while temp:
            n += 1
            temp = temp.next
        
        return n

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        total_length = self.getLength(head)
        k = k % total_length
        if k == 0:
            return head

        first, second = head, head
        for _ in range((total_length - k)-1):
            second = second.next
        
        third = second
        fourth = second.next

        while third and third.next:
            third = third.next
        
        third.next = first
        second.next = None
        head = fourth
        
        return head

