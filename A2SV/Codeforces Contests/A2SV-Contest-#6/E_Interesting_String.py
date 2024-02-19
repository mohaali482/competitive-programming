from collections import Counter

def check()
def solution(t):
    popped = [t[-1]]
    counter = Counter(t)
    word_counter = Counter()

    right = 0
    
    window = Counter()
    letter_counter = 0
    _max = 0

    i = len(t)-1
    j = len(t)-1


    while j > -1 and t[j] == t[i]:
        letter_counter += 1
        j -= 1
        if counter[t[j]] % letter_counter == 0:
            _max = letter_counter
    
    while word_counter[t[i]] < _max:
        word_counter[t[right]] += 1
        right += 1
    
    previous_counter = Counter(t[j+1:])

    j = (i - _max)
    i = j

    while j > -1:
        letter_counter = 1
        _max = 1
        local_counter = 
        while counter[t[j]] % letter_counter == 0:
            letter_counter += 1
            _max = letter_counter
            j -= 1
        
        while word_counter[t[i]] < _max:
            word_counter[t[right]] += 1
            right += 1
        

    


T = int(input())
for _ in range(T):
    t = input()
    print(solution(t))