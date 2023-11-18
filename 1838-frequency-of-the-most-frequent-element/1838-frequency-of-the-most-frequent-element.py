class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        l = 0
        for r in range(n):
            if r > 0:
                k -= (r - l) * (nums[r] - nums[r-1])
            while k < 0:
                k += nums[r] - nums[l]
                l += 1
            ans = max(ans, r - l + 1)
        return ans