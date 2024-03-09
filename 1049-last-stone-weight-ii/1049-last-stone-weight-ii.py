class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        def solve(ans):
            dp = defaultdict(int)
            dp[stones[0]] = 1
            dp[-stones[0]] = 1
            for i in stones[1:]:
                dp2 = defaultdict(int)
                for val, count in dp.items():
                    dp2[val + i] += count
                    dp2[val - i] += count
                dp = dp2
            # print(dp)
            return dp[ans] > 0
        
        for ans in range(101):
            for i in range(len(stones)):
                if stones[i] >= ans:
                    # print(ans, i)
                    if solve(ans):
                        return ans
        