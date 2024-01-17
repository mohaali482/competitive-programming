from collections import defaultdict

def solution(line):
    wining_cards, cards = line.split(" | ")
    cards = set([int(i) for i in cards.split(" ") if i.isdigit()])
    wining_cards = set([int(i) for i in wining_cards.split(" ")[2:] if i.isdigit()])
    total = len(cards.intersection(wining_cards))
    if total > 0:
        return 2 ** (total-1)
    else: 
        return 0

def solution2(line):
    wining_cards, cards = line.split(" | ")
    card = wining_cards.split(" ")
    card = wining_cards[:wining_cards.find(":")].split()[-1]
    cards = set([int(i) for i in cards.split(" ") if i.isdigit()])
    wining_cards = set([int(i) for i in wining_cards.split(" ")[2:] if i.isdigit()])
    total = len(cards.intersection(wining_cards))
    return int(card), total

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        total = len(lines)
        tot = {}
        for i in range(len(lines)):
            tot[i+1] = 1

        for line in lines:
            card, ret = solution2(line)
            total += ret * tot[card]
            for i in range(card+1, card+ret+1):
                tot[i] += 1 * tot[card]

        
        print(total)