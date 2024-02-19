def solution():
    a, b = map(int, input().split())
    a, b = sorted([a, b])
    if a%2 != 0 and b%2 != 0:
        return "No"
    if a%2 == 0:
        aa = a//2
        bb = b*2
        aa, bb = sorted([aa, bb])
        if aa != a and bb != b:
            return "Yes"
    else:
        aa = a*2
        bb = b//2
        aa, bb = sorted([aa, bb])
        if aa != a and bb != b:
            return "Yes"
    
    return "No"

for _ in range(int(input())):
    print(solution())