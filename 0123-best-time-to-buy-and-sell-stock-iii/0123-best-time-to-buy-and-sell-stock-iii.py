class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxProfits = [0] * 2
        minCosts = [float('inf')] * 2
        for i in range(n):
            for j in range(2):
                minCosts[j] = min(minCosts[j], prices[i] - (maxProfits[j-1] if j else 0))
                maxProfits[j] = max(maxProfits[j], prices[i] - minCosts[j])
        return maxProfits[-1]