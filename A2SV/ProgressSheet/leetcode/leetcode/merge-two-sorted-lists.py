# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def solve(current, left, right):
            if left is None:
                current.next = right
                return
            if right is None:
                current.next = left
                return
            
            if left.val <= right.val:
                current.next = left
                solve(current.next, left.next, right)
            else:
                current.next = right
                solve(current.next, left, right.next)
        dummy = ListNode(0)
        solve(dummy, list1, list2)
        return dummy.next