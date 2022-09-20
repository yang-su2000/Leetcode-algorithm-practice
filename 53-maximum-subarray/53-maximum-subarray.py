class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        csum = ans = -10001
        for i in nums:
            csum = max(i, csum + i)
            ans = max(ans, csum)
        return ans