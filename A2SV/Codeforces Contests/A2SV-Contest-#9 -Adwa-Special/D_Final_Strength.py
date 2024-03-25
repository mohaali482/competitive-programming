###############################################################
#                                                             #
#                   Author: Mohammed Ali Fenta                #
#                   Date  : 2024-03-23 09:53:29               #
#                                                             #
###############################################################
import sys, threading
from bisect import bisect_left


input = lambda: sys.stdin.readline().strip()
def lint():
    return list(map(int, input().split()))

def intp():
    return int(input())
    
def strp():
    return input()

def lstr():
    return list(input().split())

def main():
    def solution():
        n = intp()
        a = lint()
        array = [[a[i], i] for i in range(len(a))]
        def solve(arr):
            if len(arr) == 1:
                return arr
            mid = len(arr)//2

            left_sub = solve(arr[:mid])
            right_sub = solve(arr[mid:])
            right_items = [i[0] for i in right_sub]
            left_items = [i[0] for i in left_sub]

            for i in range(len(left_sub)):
                left_sub[i][0] += bisect_left(right_items, left_sub[i][0])

            for i in range(len(right_sub)):
                right_sub[i][0] += bisect_left(left_items, right_sub[i][0])

            res = []
            i = 0
            j = 0
            
            while i < len(left_sub) and j < len(right_sub):
                if left_sub[i][0] < right_sub[j][0]:
                    res.append(left_sub[i])
                    i += 1
                else:
                    res.append(right_sub[j])
                    j += 1

            
            res.extend(left_sub[i:])
            res.extend(right_sub[j:])
            return res
            

        ans = solve(array)
        for v, i in ans:
            a[i] = v
        
        print(*a)
    for _ in range(intp()):
        solution()



if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()