n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

pointer_a = 0
pointer_b = 0

ans = [0] * m

while pointer_b < m:
    if pointer_a < n and a[pointer_a] < b[pointer_b]:
        pointer_a += 1
    else:
        ans[pointer_b] = pointer_a 
        pointer_b += 1

print(*ans)
