# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        new_list = temp
        while 1:
            if list1 == list2 == None:
                break
            if list1 and list2:
                if list1.val >= list2.val:
                    new_list.next = list2
                    list2 = list2.next
                    new_list = new_list.next
                else:
                    new_list.next = list1
                    list1 = list1.next
                    new_list = new_list.next
            else:
                if list1:
                    new_list.next = list1
                    new_list = new_list.next
                    list1 = list1.next
                else:
                    new_list.next = list2
                    new_list = new_list.next
                    list2 = list2.next

        return temp.next
