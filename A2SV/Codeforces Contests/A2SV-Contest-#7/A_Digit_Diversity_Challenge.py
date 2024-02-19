def solution():
    l, r = map(int, input().split())
    ans = 0
    for i in range(l, r+1):
        str_i = str(i)
        if len(set(str_i)) == len(str_i):
            return (i)
    return -1
print(solution())