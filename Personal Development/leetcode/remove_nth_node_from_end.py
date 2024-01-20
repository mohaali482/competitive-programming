# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        counter = 0
        while temp.next:
            counter += 1
            temp = temp.next
        counter += 1

        if counter == 1:
            head = None
            return head

        counter -= n
        temp = head

        if counter == 0:
            head = temp.next
            return head

        for i in range(counter - 1):
            temp = temp.next

        if temp.next:
            if temp.next.next:
                temp.next = temp.next.next
            else:
                temp.next = None
        return head
