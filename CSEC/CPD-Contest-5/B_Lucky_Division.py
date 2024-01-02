n = int(input())
def solution():
    ln = {"4", "7"}
    for i in range(1, n+1):
        nn = str(i)
        f = True
        for j in nn:
            if j not in ln:
                f = False
                break
        
        if f and n % i == 0:
            return "YES"
    
    return "NO"
print(solution())