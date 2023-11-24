class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        l = 0
        r = n - 1
        ans = 0
        piles.sort()
        while l < r:
            l += 1
            r -= 1
            ans += piles[r]
            r -= 1
        return ans