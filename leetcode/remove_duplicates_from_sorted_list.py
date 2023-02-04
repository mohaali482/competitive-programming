# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        if not temp:
            return head
        if not temp.next:
            return head
        temp2 = temp.next

        if not temp2.next and temp2.val == temp.val:
            temp.next = None
            return head

        while temp2:
            if temp.val != temp2.val:
                temp = temp.next
                temp2 = temp2.next
            else:
                while temp2.val == temp.val:
                    if temp2.next:
                        temp2 = temp2.next
                    else:
                        break

                if temp2.val == temp.val:
                    temp.next = None
                    break
                else:
                    temp.next = temp2
                    temp = temp2
                    if temp2.next:
                        temp2 = temp2.next

        return head
