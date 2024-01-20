from collections import Counter
from functools import cmp_to_key

def solution():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    
    weights = {
        "A": 13,
        "K": 12,
        "Q": 11,
        "J": 10,
        "T": 9,
        "9": 8,
        "8": 7,
        "7": 6,
        "6": 5,
        "5": 4,
        "4": 3,
        "3": 2,
        "2": 1,
    }
    def compare(a, b):
        ca = Counter(a)
        cb = Counter(b)
        mxa = ca.most_common(1)[0][1]
        mxb = cb.most_common(1)[0][1]
        if mxa > mxb:
            return 1
        if mxa < mxb:
            return -1

        mxa1 = ca.most_common(2)[1][1]
        mxb1 = cb.most_common(2)[1][1]

        if mxa1 > mxb1:
            return 1
        if mxa1 < mxb1:
            return -1
        
        for i in range(len(a)):
            if weights[a[i]] > weights[b[i]]:
                return 1
            elif weights[a[i]] < weights[b[i]]:
                return -1
        
        return 0
        

        
    card_bid = {}
    cards = []
    for line in lines:
        line = line.split(" ")
        card_bid[line[0]] = int(line[1])
        cards.append(line[0])
    
    cards.sort(key=cmp_to_key(compare))
    total = 0
    for i in range(len(cards)):
        total += card_bid[cards[i]] * (i+1)
    
    return total


def solution2():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    
    weights = {
        "A": 13,
        "K": 12,
        "Q": 11,
        "T": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2,
        "J": 1,
    }
    def compare(a, b):
        ca = Counter(a)
        cb = Counter(b)
        caj = ca.pop("J") if "J" in ca else 0
        cbj = cb.pop("J") if "J" in cb else 0

        mxa = (ca.most_common(1)[0][1] if ca.most_common(1) else 0) + caj
        mxb = (cb.most_common(1)[0][1] if cb.most_common(1) else 0) + cbj
        if mxa > mxb:
            return 1
        if mxa < mxb:
            return -1

        mxa1 = ca.most_common(2)[1][1] if len(ca.most_common(2)) > 1 else 0
        mxb1 = cb.most_common(2)[1][1] if len(cb.most_common(2)) > 1 else 0

        if mxa1 > mxb1:
            return 1
        if mxa1 < mxb1:
            return -1
        
        for i in range(len(a)):
            if weights[a[i]] > weights[b[i]]:
                return 1
            elif weights[a[i]] < weights[b[i]]:
                return -1
        
        return 0
        
        
    card_bid = {}
    cards = []
    for line in lines:
        line = line.split(" ")
        card_bid[line[0]] = int(line[1])
        cards.append(line[0])
    
    cards.sort(key=cmp_to_key(compare))
    total = 0
    for i in range(len(cards)):
        total += card_bid[cards[i]] * (i+1)
    
    return total


if __name__ == "__main__":
    print(solution2())