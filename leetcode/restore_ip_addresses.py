class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []

        def isValid(num):
            if len(num) == 0:
                return False
            if num.startswith("0") and len(num) > 1:
                return False
            if not (0 <= int(num) <= 255):
                return False
            return True

        def backtrack(i, address):
            if i == len(s) and len(address) == 4:
                ans.append(".".join(address))
                return
            for j in range(i, i + 4):
                if j > len(s):
                    break

                num = s[i:j]
                if isValid(num):
                    address.append(num)
                    backtrack(j, address)
                    address.pop()

        backtrack(0, [])
        return ans
