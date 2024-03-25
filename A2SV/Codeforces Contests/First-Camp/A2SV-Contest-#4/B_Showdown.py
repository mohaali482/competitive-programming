import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    def solution():
        s = input()
        def play(idx, first, second):
            nonlocal s
            if idx == len(s):
                return idx

            remaining = len(s) - idx
            if idx % 2 == 0:
                first_remaining = remaining // 2
                second_remaining = remaining - first_remaining
            else:
                second_remaining = (remaining // 2)+1
                first_remaining = remaining - second_remaining

            if first > second and first > (second + second_remaining):
                return idx
            elif second > first and second > (first + first_remaining):
                return idx

            if s[idx] == "0":
                return play(idx+1, first, second)
            if idx % 2 == 0: # First player
                if s[idx] == "1":
                    return play(idx+1, first+1, second)
                elif s[idx] == "?":
                    end1 = play(idx+1, first+1, second)
                    end2 = play(idx+1, first, second)
                    return min(end1, end2)
            else:
                if s[idx] == "1":
                    return play(idx+1, first, second+1)
                elif s[idx] == "?":
                    end1 = play(idx+1, first, second+1)
                    end2 = play(idx+1, first, second)
                    return min(end1, end2)

        return play(0, 0, 0)


        
    for _ in range(int(input())):
        print(solution())
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
