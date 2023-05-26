class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        dp = [[None] * n for _ in range(n)]
        dsum = [piles[-1]]
        for i in range(n-2, -1, -1):
            dsum.append(piles[i] + dsum[-1])
        dsum = dsum[::-1]
        # print(dsum)
        
        def solve(i, m): # (x, stone)
            nonlocal n, dp, dsum
            if i >= n:
                return (0, 0)
            if i + 2*m >= n:
                return (n-i+1, dsum[i])
            if dp[i][m]:
                return dp[i][m]
            dx = 0
            dstone = 0
            for x in range(1, 2*m+1):
                x2, stone2 = solve(i+x, max(m, x))
                stone = dsum[i] - dsum[i+x]
                stone += solve(i+x+x2, max(m, x, x2))[1]
                if stone > dstone:
                    dstone = stone
                    dx = x
            dp[i][m] = (dx, dstone)
            return (dx, dstone)
        
        x, stone = solve(0, 1)
        return stone