class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2:
            return False
        target //= 2
        dp = [False] * (target + 1)
        dp[0] = True
        for i in nums:
            for j in range(target, i-1, -1):
                dp[j] = dp[j] or dp[j - i]
        return dp[-1]