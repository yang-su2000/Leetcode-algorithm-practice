class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        count = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] >= nums[i]:
                    continue
                val = dp[j] + 1
                if val > dp[i]:
                    dp[i] = val
                    count[i] = count[j]
                elif val == dp[i]:
                    count[i] += count[j]
        # print(dp, count)
        maxlen = max(dp)
        ans = 0
        for i in range(n):
            if dp[i] == maxlen:
                ans += count[i]
        return ans