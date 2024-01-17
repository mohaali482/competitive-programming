def solution():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    
    time = [int(i) for i in lines[0].split() if i.isdigit()]
    distance = [int(i) for i in lines[1].split() if i.isdigit()]

    total = 1
    for i in range(len(time)):
        tot = 0
        for j in range(1, time[i]+1):
            if distance[i] < (time[i]-j) * j:
                tot += 1
        
        print(tot, time[i], distance[i])
        total *= tot
    
    return total


if __name__ == "__main__":
    print(solution())