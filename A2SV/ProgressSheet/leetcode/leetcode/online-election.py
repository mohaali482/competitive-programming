class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.ans = []
        self.times = times
        counter = defaultdict(int)
        _max = 0
        _max_person = 0
        for person in persons:
            counter[person] += 1
            if counter[person] >= _max:
                _max = counter[person]
                _max_person = person
            
            self.ans.append(_max_person)


    def q(self, t: int) -> int:
        return self.ans[bisect_right(self.times, t)-1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)