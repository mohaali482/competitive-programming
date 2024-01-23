a = input()
if a == a.upper() or (a[0].islower() and a[1:].isupper()) or (len(a) == 1 and a.islower()):
    ans = [''] * len(a)    
    for i in range(len(a)):
        if a[i].isupper():
            ans[i] = a[i].lower()
        else:
            ans[i] = a[i].upper()
    print(''.join(ans))
else:
    print(a)