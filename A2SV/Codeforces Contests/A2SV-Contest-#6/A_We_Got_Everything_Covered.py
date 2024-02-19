from string import ascii_lowercase

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(ascii_lowercase[:k] * n)