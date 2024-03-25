
import sys, threading

input = lambda: sys.stdin.readline().strip()


def main():
    num = input()
    i_num = int(num)
    current = []
    counter = defaultdict(int)
    arr = set()
    def solve(idx):
        if current:
            cur = int(''.join(current))
            if counter["4"] == counter["7"]:
                arr.add(cur)
        
        for i in range(idx, len(num)+2):
            current.append("4")
            counter["4"] += 1
            solve(i+1)
            current.pop()
            counter["4"] -= 1   

            current.append("7")
            counter["7"] += 1
            solve(i+1)
            current.pop()
            counter["7"] -= 1

    solve(0)
    arr = sorted(list(arr))
    # print(arr)
    left = bisect.bisect_left(arr, i_num)
    if left < len(arr) and arr[left] == i_num:
        print(arr[left])
    else:
        print(arr[left])

    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
