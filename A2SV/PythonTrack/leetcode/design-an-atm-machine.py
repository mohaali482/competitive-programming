class ATM:

    def __init__(self):
        self.notes = {
            500: 0,
            200: 0,
            100: 0,
            50:  0,
            20:  0,
        }
        self.notesOrder = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(len(self.notesOrder)):
            self.notes[self.notesOrder[i]] += banknotesCount[i]


    def withdraw(self, amount: int) -> List[int]:
        ans = [0] * len(self.notesOrder)
        newNotes = {k: v for k, v in self.notes.items()}
        tot = 0
        or_amount = amount
        for i in range(len(ans)-1, -1, -1):
            if self.notesOrder[i] > amount or newNotes[self.notesOrder[i]] == 0:
                continue
            
            needed = amount // self.notesOrder[i]

            if needed > newNotes[self.notesOrder[i]]:
                needed = newNotes[self.notesOrder[i]]

            amount -= needed * self.notesOrder[i]
            tot += needed * self.notesOrder[i]
            ans[i] = needed
            newNotes[self.notesOrder[i]] -= needed
        
        if tot == or_amount:
            self.notes = newNotes
            return ans
        else:
            return [-1]
        

            


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)