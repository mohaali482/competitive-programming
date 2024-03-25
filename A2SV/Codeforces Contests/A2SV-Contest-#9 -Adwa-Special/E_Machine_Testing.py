###############################################################
#                                                             #
#                   Author: Mohammed Ali Fenta                #
#                   Date  : 2024-03-23 11:07:53               #
#                                                             #
###############################################################
import sys, threading
from sys import stdin
from math import ceil


input = lambda : stdin.readline().strip()

def lint():
    return list(map(int, input().split()))

def intp():
    return int(input())
    
def strp():
    return input()

def lstr():
    return list(input().split())


input = lambda: sys.stdin.readline().strip()


def main():
    def solution():
        n = intp()
        h = lint()
        p = lint()
        if n == 1:
            print(0)
            return

        tot = 0
        def ask(idx):
            if idx == n-2:
                return ceil(h[idx+1] / p[idx])
            
            next = ask(idx+1)
            current = ceil(h[idx+1] / p[idx])
            if current < next:
                nonlocal tot
                tot += current
                h[idx+2] -= (current * p[idx+1])
                h[idx+2] = max(h[idx+2], 0)
            
            h[idx+1] -= current * p[idx]
            h[idx+1] = max(h[idx+1], 0)
            h[idx+1] += h[idx+2]
            
            
        
            return ceil(h[idx+1] / p[idx])
        need = ask(0)
        print(tot + need)

            

    
    for _ in range(intp()):
        solution()


if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()