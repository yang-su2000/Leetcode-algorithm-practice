class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        cur = 0
        ans = inf
        for r in range(len(nums)):
            cur += nums[r]
            while cur >= target:
                ans = min(ans, r - l + 1)
                cur -= nums[l]
                l += 1
        return ans if ans != inf else 0