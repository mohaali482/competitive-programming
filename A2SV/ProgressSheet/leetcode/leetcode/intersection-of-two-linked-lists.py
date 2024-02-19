# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a_count = 0
        tempa = headA
        while tempa:
            a_count += 1
            tempa = tempa.next
        
        b_count = 0
        tempb = headB
        while tempb:
            b_count += 1
            tempb = tempb.next
        
        tempa = headA
        tempb = headB
        if a_count > b_count:
            for i in range(a_count - b_count):
                tempa = tempa.next
        else:
            for i in range(b_count - a_count):
                tempb = tempb.next
        
        while tempa and tempb:
            if tempa is tempb:
                return tempa
            
            tempa = tempa.next
            tempb = tempb.next
        
        return None
        