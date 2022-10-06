class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        cmax = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > cmax:
                ans += prices[i] - cmax
                cmax = prices[i]
            else:
                cmax = prices[i]
        return ans