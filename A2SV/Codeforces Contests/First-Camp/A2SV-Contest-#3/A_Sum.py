t = int(input())
for _ in range(t):
    _list = [int(i) for i in input().split()]
    _list.sort()
    if _list[0] + _list[1] == _list[2]:
        print("YES")
    else:
        print("NO")