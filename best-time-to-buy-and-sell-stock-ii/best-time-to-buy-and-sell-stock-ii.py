class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        ans = 0
        for i in range(n-1):
            ans += max(prices[i+1] - prices[i], 0)
        return ans