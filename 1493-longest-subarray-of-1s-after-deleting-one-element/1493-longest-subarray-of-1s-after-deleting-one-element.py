class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero_count = 0
        ans = 0
        l = 0
        n = len(nums)
        for r in range(n):
            zero_count += (nums[r] == 0)
            while zero_count > 1:
                zero_count -= (nums[l] == 0)
                l += 1
            ans = max(ans, r - l)
        return ans