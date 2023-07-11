class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        m = max(nums)
        v = [0] * (m + 1)
        for i in nums:
            v[i] += 1
        
        @cache
        def dp(i):
            nonlocal m, v
            if i < 0 or i > m:
                return 0
            return max(dp(i+1), v[i] * i + dp(i+2))
        
        return dp(0)