class Node:
    def __init__(self, val: int, next = None):
        self.val = val
        self.next = next
    
    # def __str__(self):
    #     arr = []
    #     current = self
    #     while current:
    #         arr.append(str(current.val))
    #         current = current.next
    #     return ' '.join(arr)

class MyLinkedList:

    def __init__(self):
        self.head = Node(-1)

    def get(self, index: int) -> int:
        temp = self.head.next
        for i in range(index):
            if temp:
                temp = temp.next
            else:
                break
        if temp:
            return temp.val
        return -1

    def addAtHead(self, val: int) -> None:
        node = Node(val, self.head.next)
        self.head.next = node
        

    def addAtTail(self, val: int) -> None:
        node = Node(val)

        temp = self.head
        while temp.next:
            temp = temp.next
        
        temp.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        node = Node(val)
        temp = self.head
        for i in range(index):
            if temp:
                temp = temp.next
            else:
                return
        
        if temp:
            node.next = temp.next
            temp.next = node

    def deleteAtIndex(self, index: int) -> None:
        temp = self.head
        for i in range(index):
            if temp:
                temp = temp.next
            else:
                return
        
        if temp and temp.next:
            temp.next = temp.next.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)