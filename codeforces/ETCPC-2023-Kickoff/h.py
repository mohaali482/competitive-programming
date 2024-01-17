t = int(input())
for _ in range(t):
    ans = 0
    added = False
    a, b, c, d, e, f = map(int, input().split())
    c -= 1
    b_square = b**2 - 4*a*c
    e_square = e**2 - 4*d*f
    
    if b_square == 0:
        added = True
        ans += -b/(2*a)
    if e_square == 0:
        added = True
        ans += -e/(2*d)
    if b_square > 0:
        added = True
        e = b_square ** 0.5
        ans += (-b + e)/(2*a)
        ans += (-b - e)/(2*a)
    if e_square > 0:
        added = True
        sqr = e_square ** 0.5
        ans += (-e + sqr)/(2*d)
        ans += (-e - sqr)/(2*d)
    
    if added:
        print(ans)
    else:
        print("No Solution")
