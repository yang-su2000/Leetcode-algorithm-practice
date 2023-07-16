class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        ans = 0
        # [1, 2, 3, 4, 5]
        # [-1, +2, -2, +3, -3, +4, -4, +5] == [-1, +5]
        # [7,1,5,3,6,4]
        
        
        
        
        # x
        #           +
        #     +
        #              +
        #        +
        # 
        #   +
        for i in range(n-1):
            current = prices[i]
            next = prices[i+1]
            if next > current:
                ans += next - current
        return ans