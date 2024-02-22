class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        Y = [0] * (n+1)
        N = [0] * (n+1)
        for i in range(n-1, -1, -1):
            if customers[i] == "Y":
                Y[i] = 1 + Y[i+1]
            else:
                Y[i] = Y[i+1]
                
        for i in range(1,n+1):
            if customers[i-1] == "N":
                N[i] = 1 + N[i-1]
            else:
                N[i] = N[i-1]

        _min = float("inf")
        _idx = -1
        for i in range(n+1):
            total = Y[i] + N[i]
            if total < _min:
                _min = total
                idx = i
        return idx