t = int(input())
for _ in range(t):
    st = input()
    if len(st) == 1:
        if st == "v":
            print(0)
        else:
            print(1)
        continue

    ans = st.count("w")
    i = 0
    while i < len(st)-1:
        if st[i] == "v" and st[i+1] == "v":
            ans += 1
            i += 2
        else:
            i += 1

    print(ans)
