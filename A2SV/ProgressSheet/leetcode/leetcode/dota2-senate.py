class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        game = deque(senate)
        dire = radiant = 0
        for each in senate:
            if each == "D":
                dire += 1
            else:
                radiant += 1
        bDire = bRadiant = 0
        while True:
            if dire == 0:
                return 'Radiant'
            if radiant == 0:
                return 'Dire'
            
            vote = game.popleft()
            if vote == 'D':
                if bDire > 0:
                    bDire -= 1
                    dire -= 1
                else:
                    bRadiant += 1
                    game.append(vote)
            else:
                if bRadiant > 0:
                    bRadiant -= 1
                    radiant -= 1
                else:
                    bDire += 1
                    game.append(vote)