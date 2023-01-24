# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counter = 0
        temp = head
        while temp.next:
            temp = temp.next
            counter += 1
        counter += 1

        half = counter // 2
        temp = head
        for i in range(half):
            temp = temp.next
        return temp
