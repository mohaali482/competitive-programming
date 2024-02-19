for _ in range(int(input())):
    n = int(input())
    if n <= 27:
        ans = "aa"
        n -= 2
        ans += chr(ord('a')-1 + n)
        print(ans)
    elif n <= 52:
        ans = "z"
        n -= 27
        ans += chr(ord('a')-1 + n)
        ans += "a"
        print(ans[::-1])
    else:
        ans = "zz"
        n -= 52
        ans += chr(ord('a') - 1 + n)
        ans = ans[::-1]
        print(ans)


    
    