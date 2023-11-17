class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        cur_sum = nums[0]
        for i in nums[1:]:
            cur_sum = max(i, cur_sum + i)
            ans = max(ans, cur_sum)
        return ans