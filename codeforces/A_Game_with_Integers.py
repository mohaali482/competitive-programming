t = int(input())
for _ in range(t):
    a = int(input())
    if (a - 1) % 3 == 0:
        print("First")
        continue
    elif (a+1) % 3 == 0:
        print("First")
        continue
    else:
        print("Second")