t = int(input())
for _ in range(t):
    n = int(input())
    st = input()
    _max = 0
    for i in set(st):
        if ord(i) > _max:
            _max = ord(i)
    
    print(_max - 96)