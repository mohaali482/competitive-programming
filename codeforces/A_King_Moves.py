a = input()
if a in {"a1", "h1", "a8", "h8"}:
    print(3)
elif a[1] == "1" or a[1] == "8" or a[0] == "h" or a[0] == "a":
    print(5)
else:
    print(8)
