class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        e = [0] * n
        for a, b in roads:
            e[a] += 1
            e[b] += 1
        ans = 0
        roads = set((a, b) for a, b in roads)
        for a in range(n):
            for b in range(a+1, n):
                if (a, b) in roads or (b, a) in roads:
                    ans = max(ans, e[a] + e[b] - 1)
                else:
                    ans = max(ans, e[a] + e[b])
        return ans