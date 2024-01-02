t = int(input())
total = 0
for _ in range(t):
    a, b = map(int, input().split())
    if b - a > 1:
        total += 1
print(total)