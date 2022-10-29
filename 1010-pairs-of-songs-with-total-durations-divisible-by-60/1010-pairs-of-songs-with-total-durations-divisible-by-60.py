class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        d = defaultdict(int)
        ans = 0
        for t in time:
            t %= 60
            ans += d[60 - t if t else 0]
            d[t] += 1
        return ans