import bisect

import sys, threading
from itertools import accumulate

input = lambda: sys.stdin.readline().strip()

def main():
    n, _, A, B = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    def find(start, end):
        totalAvengers = bisect.bisect_right(a, end) - bisect.bisect_left(a, start)
        current = 0
        if totalAvengers > 0:
            current += B * totalAvengers * ((end-start)+1)
        else:
            current += A
        return current, totalAvengers

    def divide(start, end):
        if start == end:
            return find(start, end)[0]
        ans, totalAvengers = find(start, end)
        if totalAvengers == 0:
            return ans
        leftMin = divide(start, (start + end)//2)
        rightMin = divide(((start + end)//2)+1, end)
        return min(ans, leftMin+rightMin)
    
    print(divide(1, 2**n))
    


    
if __name__ == '__main__':
    
    main()
