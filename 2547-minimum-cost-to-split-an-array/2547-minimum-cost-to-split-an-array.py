class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = k
        for i in range(1, n):
            cur = [0] * n
            l = 0
            for j in range(i, -1, -1):
                cur[nums[j]] += 1
                if cur[nums[j]] == 2:
                    l += 2
                elif cur[nums[j]] > 2:
                    l += 1
                dp[i] = min(dp[i], l + k + (dp[j-1] if j >= 1 else 0))
        return dp[-1]