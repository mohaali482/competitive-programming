k, n = map(int, input().split())
a = list(map(int, input().split()))
s = input()
tot = 0
j = 0
ch = s[0]
wind = []
while j < len(s):
    if s[j] == ch:
        wind.append(a[j])
    else:
        tot += sum(sorted(wind, reverse=True)[:n])
        ch = s[j]
        wind = [a[j]]

    j += 1
tot += sum(sorted(wind, reverse=True)[:n])
print(tot)