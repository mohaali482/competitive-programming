# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i in range(len(lists)):
            node = lists[i]
            if node:
                heapq.heappush(heap, (node.val, i, node))

        if not heap:
            return None

        list = ListNode()
        list.next = ListNode()
        temp = list.next
        while heap:
            val, _, node = heapq.heappop(heap)
            temp.val = val
            if node.next:
                heapq.heappush(heap, (node.next.val, _, node.next))
            if heap:
                temp.next = ListNode()
                temp = temp.next
            else:
                break

        return list.next
