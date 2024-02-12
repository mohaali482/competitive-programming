# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        temp2 = temp
        while temp2 and temp2.next:
            temp2 = temp2.next.next
            temp = temp.next

        return temp

