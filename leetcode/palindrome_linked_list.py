# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True

        new_list = []
        while head:
            new_list.append(head.val)
            head = head.next

        i = 0
        j = len(new_list) - 1
        while i < j:
            if new_list[i] != new_list[j]:
                return False

            i += 1
            j -= 1

        return True
