for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a_copy = a.copy()
    first_max = max(a_copy)
    first_max_index = -1
    for i in range(n):
        if a_copy[i] == first_max:
            a_copy[i] = 0
            first_max_index = i
            break
    
    second_max = max(a_copy)
    second_max_index = -1
    for i in range(n):
        if a_copy[i] == second_max:
            a_copy[i] = 0
            second_max_index = i
            break
    
    ans = [0] * n
    for i in range(n):
        if i == first_max_index:
            ans[i] = a[i] - second_max
        elif i == second_max_index:
            ans[i] = a[i] - first_max
        else:
            ans[i] = a[i] - first_max
    
    print(*ans)
