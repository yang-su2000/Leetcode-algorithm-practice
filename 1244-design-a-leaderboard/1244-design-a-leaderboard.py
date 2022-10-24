class Leaderboard:

    def __init__(self):
        self.d = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.d[playerId] += score

    def top(self, K: int) -> int:
        return sum(sorted(self.d.values())[-K:])

    def reset(self, playerId: int) -> None:
        del self.d[playerId]


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)