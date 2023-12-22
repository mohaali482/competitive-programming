arr = [
    [i for i in input().split()],
    [i for i in input().split()],
    [i for i in input().split()],
    [i for i in input().split()],
    [i for i in input().split()],
]
for i in range(len(arr)):
    found = False
    for j in range(len(arr[0])):
        if arr[i][j] == '1':
            found = True
            break

    if found:
        break

manhattan_distance = abs(i - 2) + abs(j - 2)
print(manhattan_distance)