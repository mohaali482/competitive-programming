n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
def check(ans):
    new_arr = []
    for i in range(len(ans)):
        temp = []
        for j in range(len(ans[0])):
            a = 0
            k = 0
            while k < n:
                a |= ans[k][j]
                k += 1
            k = 0
            while k < m:
                a |= ans[i][k]
                k += 1
            temp.append(a)
        new_arr.append(temp)
    for i in range(len(ans)):
        for j in range(len(ans[0])):
            if new_arr[i][j] != arr[i][j]:
                return False
    
    return True

def solution():
    ans = [[1 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                continue
            else:
                k = 0
                while k < n:
                    ans[k][j] = 0
                    k += 1
                k = 0
                while k < m:
                    ans[i][k] = 0
                    k += 1

    return ans

ans = solution()
if not check(ans):
    print("NO")
else:
    print("YES")
    for i in range(len(ans)):
        print(*ans[i])
                    