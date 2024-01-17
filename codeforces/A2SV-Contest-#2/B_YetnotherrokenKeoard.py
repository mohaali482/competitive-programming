t = int(input())
for _ in range(t):
    a = input()
    stack = []
    cap = []
    small = []
    for i in a:
        if i != "B" and i != "b":
            if ord(i) >= 65 and ord(i) <= 90:
                cap.append(len(stack))
                stack.append(i)
            else:
                small.append(len(stack))
                stack.append(i)
        elif stack:
            if i == "B":
                if cap:
                    c = cap.pop()
                    stack[c] = ""
            elif i == "b":
                if small:
                    s = small.pop()
                    stack[s] = ""
    
    print(''.join(stack))
