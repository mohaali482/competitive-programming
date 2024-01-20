t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    
    if ''.join(sorted(s)) == ''.join(sorted("Timur")):
        print("yes")
    else:
        print("no")
