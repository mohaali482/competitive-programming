class UndergroundSystem:

    def __init__(self):
        self.position = {}
        self.average = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.position[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        key = f"{self.position[id][0]}-{stationName}"
        time = t - self.position[id][1]

        if key in self.average:
            old = self.average[key]
            self.average[key] = [((old[0]*old[1]) + time) / (old[1] + 1), old[1] + 1]
        else:
            self.average[key] = [time, 1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = f"{startStation}-{endStation}"
        return self.average[key][0]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)