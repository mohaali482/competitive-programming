prefix_sum = [0]
for i in range(1, (10**6)+1):
    prefix_sum.append(prefix_sum[-1]+i**2)

with open("n.txt", "w") as file:
    file.write(str(prefix_sum))

t = int(input())
for _ in range(t):
    a = int(input())

    print(prefix_sum[int(a**0.5)])