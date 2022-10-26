class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mincost = float('inf')
        maxprofit = 0
        for p in prices:
            mincost = min(mincost, p)
            maxprofit = max(maxprofit, p - mincost)
        return maxprofit