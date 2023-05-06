class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        dp = [1] * (n + 1)
        mod = int(1e9+7)
        for i in range(1, n+1):
            dp[i] = (dp[i-1] << 1) % mod
        # print(dp)
        l = 0
        r = -1
        while r+1 < n and nums[l] + nums[r+1] <= target:
            r += 1
        ans = 0
        if l <= r:
            ans += dp[r-l]
        l += 1
        # print(ans)
        while l < n:
            while l <= r and nums[l] + nums[r] > target:
                r -= 1
            if l <= r:
                ans = (ans + dp[r-l]) % mod
                # print(ans)
            else:
                break
            l += 1
        return ans
        