from collections import Counter
n, m = map(int, input().split())
matrice = [list(input()) for _ in range(n)]
transpose = zip(*matrice)
matriceCounter = [
    Counter(row) for row in matrice
]
transposeCounter = [
    Counter(row) for row in transpose
]
for i in range(n):
    for j in range(m):
        if matriceCounter[i][matrice[i][j]] != 1 or transposeCounter[j][matrice[i][j]] != 1:
            matrice[i][j] = ''

ans = ''.join([''.join(row) for row in matrice])
print(ans)