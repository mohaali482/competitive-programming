# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next:
            return head

        temp = ListNode()
        temp1 = ListNode()
        temp.next = temp1
        temp2 = head
        temp3 = temp2.next
        breakable = False
        while temp3:
            if breakable:
                break
            if temp2.val == temp3.val:
                while temp2.val == temp3.val:
                    if temp3.next:
                        temp3 = temp3.next
                    else:
                        breakable = True
                        break
                if temp3.next:
                    temp2 = temp3
                    temp3 = temp3.next
                elif temp2.val != temp3.val:
                    breakable = True
                    temp1.next = temp3
                else:
                    breakable = True
                    temp1.next = None
            else:
                temp1.next = temp2
                temp2 = temp3
                temp1 = temp1.next
                if temp3.next:
                    temp3 = temp3.next
                else:
                    temp1.next = temp3
                    breakable = True

        return temp.next.next
