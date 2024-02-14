class Node:
    def __init__(self, val: str, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev
    
class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = Node(homepage)
        self.current = self.history

    def visit(self, url: str) -> None:
        newHistory = Node(url)
        newHistory.prev = self.current
        self.current.next = newHistory
        self.current = self.current.next

    def back(self, steps: int) -> str:
        while self.current.prev and steps > 0:
            self.current = self.current.prev
            steps -= 1
        return self.current.val

    def forward(self, steps: int) -> str:
        while self.current.next and steps > 0:
            self.current = self.current.next
            steps -= 1
        return self.current.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)