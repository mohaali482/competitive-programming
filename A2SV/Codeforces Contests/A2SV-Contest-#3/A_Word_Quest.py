t = int(input())
for _ in range(t):
    a = [[input()] for i in range(8)]
    at = zip(*a)
    print(''.join([''.join(row) for row in at]).replace(".", ""))