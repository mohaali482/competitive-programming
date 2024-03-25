from collections import Counter

import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    def solution():
        n = int(input())
        a = list(map(int, input().split()))
        c = Counter()
        for i in a:
            m = str(i)
            c[int(m[-1])] += 1
        
        nums = sorted(list(c.keys()))
        for key in nums:
            if c[key] > 3:
                c[key] = 3
        _sum = 0
        _count = 0
        def solve():
            nonlocal _sum, _count
            if _count == 3 and str(_sum)[-1] == "3":
                return True
            
            if _count == 3:
                return
            
            for i in range(len(nums)):
                if c[nums[i]] > 0:
                    _sum += nums[i]
                    _count += 1
                    c[nums[i]] -= 1
                    if solve():
                        return True
                    _sum -= nums[i]
                    _count -= 1
                    c[nums[i]] += 1
            
            return False
        
        return solve()


        
    for _ in range(int(input())):
        if solution():
            print("YES")
        else:
            print("NO")
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
