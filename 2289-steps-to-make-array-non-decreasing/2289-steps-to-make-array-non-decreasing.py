class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        n = len(nums)
        ls = []
        dp = [0] * n
        for i in range(n-1, -1, -1):
            while ls and nums[i] > nums[ls[-1]]:
                dp[i] = max(dp[i] + 1, dp[ls[-1]])
                ls.pop()
            ls.append(i)
        # print(dp, ls)
        return max(dp)
            