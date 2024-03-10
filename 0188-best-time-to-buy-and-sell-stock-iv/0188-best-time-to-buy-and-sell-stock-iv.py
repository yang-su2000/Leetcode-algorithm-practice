class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        minCosts = [1001 for _ in range(k)]
        maxProfits = [0 for _ in range(k)]
        for val in prices:
            for i in range(k):
                minCosts[i] = min(minCosts[i], val - (0 if i == 0 else maxProfits[i-1]))
                maxProfits[i] = max(maxProfits[i], val - minCosts[i])
        return maxProfits[-1]