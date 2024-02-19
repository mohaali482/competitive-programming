for _ in range(int(input())):
    input()
    s = input()
    left = []
    right = []
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            left.append(i)
            right.append(j)
        i += 1
        j -= 1
    flag = True
    for i in range(len(left)-1):
        if left[i+1] - left[i] != 1:
            flag = False
            break
    flag2 = True
    for i in range(len(right)-1):
        if right[i+1] - right[i] != 1:
            flag2 = False
            break
    
    if flag or flag2:
        print("Yes")
    else:
        print("No")
