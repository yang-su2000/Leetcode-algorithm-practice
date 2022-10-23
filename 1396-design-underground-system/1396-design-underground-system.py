class UndergroundSystem:

    def __init__(self):
        self.routes = defaultdict(lambda: [0, 0])
        self.ins = defaultdict(tuple)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.ins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        in_station, in_t = self.ins[id]
        ls = self.routes[(in_station, stationName)]
        ls[0] += t - in_t
        ls[1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        ls = self.routes[(startStation, endStation)]
        return ls[0] / ls[1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)