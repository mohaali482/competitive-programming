from string import ascii_uppercase

def validate(l, a):
    a = list(a)
    cc = list(set(ascii_uppercase) - set([i for i in l.keys() if l[i] > 0 and i != "?"]))

    for i in range(len(a)):
        if a[i] == "?":
            a[i] = cc.pop()
            l[a[i]] += 1
            l["?"] -= 1
    
    return a

def solution():
    a = list(input())
    if len(a) < 25:
        return -1
    
    i = 0
    j = 25
    counter = {k:0 for k in ascii_uppercase}
    counter["?"] = 0

    for m in range(25):
        counter[a[m]] += 1
    
    val = False
    
    while j < len(a):
        valid = True
        counter[a[j]] += 1


        for k, v in counter.items():
            if k != "?" and v > 1:
                valid = False
        
        if valid:
            a[i: j+1] = validate(counter, a[i: j+1])
            val = True

        counter[a[i]] -= 1
        i += 1
        j += 1
    
    if not val:
        return -1
    
    for i in range(len(a)):
        if a[i] == "?":
            a[i] = "A"
    return ''.join(a)

print(solution())
        