class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        temp = deque()
        for i in range(len(deck)-1, -1, -1):
            if temp:
                temp.appendleft(temp.pop())
            temp.appendleft(deck[i])
        return temp