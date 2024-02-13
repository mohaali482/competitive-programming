# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=ListNode())
        dummy2 = dummy.next
        dummy3 = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                dummy2.val = list1.val
                dummy2.next = ListNode()
                list1 = list1.next
            else:
                dummy2.val = list2.val
                dummy2.next = ListNode()
                list2 = list2.next
            dummy3 = dummy3.next
            dummy2 = dummy2.next
        
        while list1:
            dummy2.val = list1.val
            dummy2.next = ListNode()
            dummy3 = dummy3.next
            dummy2 = dummy2.next
            list1 = list1.next

        
        while list2:
            dummy2.val = list2.val
            dummy2.next = ListNode()
            dummy3 = dummy3.next
            dummy2 = dummy2.next
            list2 = list2.next
        
        dummy3.next = None
        return dummy.next