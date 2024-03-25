import sys, threading

input = lambda: sys.stdin.readline().strip()

def solve():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    def find(s, arr):
        print("Error", s, arr)
        if not arr:
            return False
        left = []
        right = []
        mid = (min(arr) + max(arr)) // 2
        _sum_left = 0
        _sum_right = 0
        for i in arr:
            if i <= mid:
                _sum_left += i
                left.append(i)
            else:
                _sum_right += i
                right.append(i)
        if _sum_left == s:
            return True
        elif _sum_right == s:
            return True
        elif _sum_left >= s and _sum_right >= s:
            return find(s, left) or find(s, right)
        elif _sum_left > s:
            return find(s, left)
        elif _sum_right > s:
            return find(s, right)
        
        return False

    for _ in range(q):
        s = int(input())
        if find(s, a):
            print("Yes")
        else:
            print("No")

def main():
    for _ in range(int(input())):
        solve()

    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
