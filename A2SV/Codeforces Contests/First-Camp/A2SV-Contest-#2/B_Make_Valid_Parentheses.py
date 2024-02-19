string = input()
stack = []
ans = 0
for i in string:
    if i == "(":
        stack.append(i)
    else:
        if stack and stack[-1] == "(":
            stack.pop()
            ans += 2

print(ans)