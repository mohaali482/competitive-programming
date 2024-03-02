class Solution:
    def get(self, n: int, k: int, root: int) -> str:
        if n == 1:
            return root
        power = pow(2, n-1)
        if k > power // 2:
            if root == 0:
                next = 1
            else:
                next = 0
            
            return self.get(n-1, k-power//2, next)
        else:
            if root == 0:
                next = 0
            else:
                next = 1
            
            return self.get(n-1, k, next)

    def kthGrammar(self, n: int, k: int) -> int:
        return self.get(n, k, 0)