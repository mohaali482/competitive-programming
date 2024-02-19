for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    right = n-1
    a_right = a[right]
    rightCount = 1
    while right > 0 and a[right] == a[right-1]:
        rightCount += 1
        right -= 1
    
    left = 0
    a_left = a[left]
    leftCount = 1
    while left < n-1 and a[left] == a[left+1]:
        leftCount += 1
        left += 1
    
    if a_right == a_left:
        right -= 1
        left += 1
        if left == n:
            print(0)
        else:
            print(right-left+1)
    else:
        if rightCount > leftCount:
            right -= 1
            print(right+1)
        else:
            left += 1
            print(n-left)
